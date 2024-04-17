import copy
import time
from queue import Empty, Full, Queue
from threading import Event, Thread
from typing import List

import numpy as np

from dolphindb import session as Session

from .config import FORCEPARTITION, TIMEOUT, TRY_MAX_TIME
from .helper import DataListCeil, DataPytorchCeil, DataTensorflowCeil
from .utils import (GROUP_FLAG, LOAD_MODE, ExitStatus, MetaSQL, MODE_TYPE,
                    _check_category, _generate_tablename, _release_table)

from . import utils


class DataSource(object):
    prefix_sum: List[int]

    def __getitem__(self, index):
        raise NotImplementedError

    def start(self, sampler):
        raise NotImplementedError

    def join(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError

    def get_next_data(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.prefix_sum) - 1

    def data_len(self):
        return self.prefix_sum[-1] - self.prefix_sum[0]


class DataMockSource(DataSource):
    def __init__(self, cnts, offset=0) -> None:
        self.offset = offset
        self.cnts = cnts
        self.q_size = 10
        self.exit_flag = Event()
        plen = len(cnts)
        raw_prefix_sum = [0] * (plen + 1)
        real_prefix_sum = [0] * (plen + 1)
        raw_prefix_sum[0] = -offset
        for i in range(plen):
            raw_prefix_sum[i+1] = raw_prefix_sum[i] + cnts[i]
            real_prefix_sum[i+1] = max(0, raw_prefix_sum[i+1])
        self.prefix_sum = real_prefix_sum
        self.res_prefix_sum = raw_prefix_sum

    def __getitem__(self, index):
        data_start = self.res_prefix_sum[index] + self.offset
        data_end = self.res_prefix_sum[index+1] + self.offset
        real_len = self.prefix_sum[index+1] - self.prefix_sum[index]
        if real_len == 0:
            return DataListCeil([_ for _ in range(data_start, data_end)])[0:0]
        return DataListCeil([_ for _ in range(data_start, data_end)])[-real_len:]

    def start(self, sampler):
        if hasattr(self, "back_thread"):
            raise RuntimeError("DataSource can not start twice.")
        self.sampler = sampler
        self.q = Queue(self.q_size)
        self.exit_flag.clear()
        self.back_thread = Thread(target=self._prepare_data)
        self.back_thread.start()

    def join(self):
        if not hasattr(self, "back_thread"):
            raise RuntimeError("DataSource has not started.")
        self.back_thread.join()
        del self.back_thread
        del self.q

    def __del__(self):
        self.exit()

    def exit(self):
        if hasattr(self, "back_thread") and not self.exit_flag.is_set():
            self.exit_flag.set()
            self.join()

    def _prepare_data(self):
        try:
            for index in self.sampler:
                data = self[index]
                put_flag = False
                while not put_flag and not self.exit_flag.is_set():
                    try:
                        self.q.put(data, timeout=TIMEOUT)
                        put_flag = True
                    except Full:
                        pass
                if self.exit_flag.is_set():
                    break
        except Exception as e:
            put_flag = False
            while not put_flag and not self.exit_flag.is_set():
                try:
                    self.q.put(e, timeout=TIMEOUT)
                    put_flag = True
                except Full:
                    pass

    def get_next_data(self):
        get_flag = False
        res = ExitStatus()
        while not get_flag and not self.exit_flag.is_set():
            try:
                res = self.q.get(timeout=TIMEOUT)
                get_flag = True
                if isinstance(res, Exception):
                    raise res
                self.q.task_done()
            except Empty:
                pass
        return res


class DataRealSource(DataSource):
    def __init__(
        self, sess: Session, sqls: List[MetaSQL],
        sql_mode, func_name: str,
        *,
        input_cols=None, target_cols=None, exclude_cols=None,
        offset: int = 0, q_size: int = 10, data_mode: MODE_TYPE = MODE_TYPE.PYTORCH, device: str = "cpu",
        verbose: bool = False,
    ) -> None:
        self.s = sess
        self.sqls = sqls
        self.mode = LOAD_MODE.UNKNOWN
        self.forcePartition = FORCEPARTITION
        self.func_name = func_name
        self.verbose = verbose
        self.release_list = []
        ds_names = [self._check_sql(sql) for sql in sqls]
        self.sql_mode = sql_mode
        self.offset = offset
        self.data_mode = data_mode
        self.device = device
        self.input_cols = input_cols
        self.target_cols = target_cols
        self.exclude_cols = exclude_cols
        self.q_size = q_size

        self.exit_flag = Event()

        all_partitions = []
        raw_prefix_sum = [-offset]
        real_prefix_sum = [0]
        for ds, counts in ds_names:
            if self.mode == LOAD_MODE.SQLDS:
                if counts is None:
                    continue
                for i, count in enumerate(counts):
                    all_partitions.append((ds, i, count))
                    raw_prefix_sum.append(raw_prefix_sum[-1] + count)
                    real_prefix_sum.append(max(raw_prefix_sum[-1], 0))
            elif self.mode == LOAD_MODE.PIVOTBY:
                assert isinstance(ds, tuple)
                all_partitions.append((ds[0], ds[1], counts))
                raw_prefix_sum.append(raw_prefix_sum[-1] + counts)
                real_prefix_sum.append(max(raw_prefix_sum[-1], 0))
        self.prefix_sum = real_prefix_sum
        self.all_partitions = all_partitions

    def __getitem__(self, index):
        temp_name = _generate_tablename("DataLoader")
        get_data_flag = False
        ds_name, ds_p_index, ds_p_len = self.all_partitions[index]
        for _ in range(TRY_MAX_TIME):
            if get_data_flag:
                break
            if self.mode == LOAD_MODE.SQLDS:
                load_data_scripts = f"{temp_name} = select * from {ds_name}[{ds_p_index}];"
            elif self.mode == LOAD_MODE.PIVOTBY:
                temp_name = ds_name
                load_data_scripts = ds_p_index
            self.s.run(load_data_scripts)
            self._generate_colnames(temp_name)
            get_data_flag, data, ndim = self._get_data_with_tbName(temp_name)
        _release_table(self.s, temp_name)
        if not get_data_flag:
            raise RuntimeError('Error Occured with sql query, please check your sql and network.')
        self.ndim = ndim
        real_len = self.prefix_sum[index+1] - self.prefix_sum[index]
        if real_len == 0:
            data = data[0:0]
        elif real_len != ds_p_len:
            data = data[-real_len:]
        return data

    def start(self, sampler):
        if hasattr(self, "back_thread"):
            raise RuntimeError("DataSource can not start twice.")
        self.sampler = sampler
        self.q = Queue(self.q_size)
        self.exit_flag.clear()
        self.back_thread = Thread(target=self._prepare_data)
        self.back_thread.start()

    def join(self):
        if not hasattr(self, "back_thread"):
            raise RuntimeError("DataSource has not started.")
        self.back_thread.join()
        del self.back_thread
        del self.q

    def __del__(self):
        for ds_name in self.release_list:
            try:
                _release_table(self.s, ds_name)
            except Exception:
                pass
        self.exit()

    def exit(self):
        if hasattr(self, "back_thread") and not self.exit_flag.is_set():
            self.exit_flag.set()
            self.join()

    def _prepare_data(self):
        try:
            for index in self.sampler:
                data = self[index]
                put_flag = False
                while not put_flag and not self.exit_flag.is_set():
                    try:
                        self.q.put(data, timeout=TIMEOUT)
                        put_flag = True
                    except Full:
                        pass
                if self.exit_flag.is_set():
                    break
        except Exception as e:
            put_flag = False
            while not put_flag and not self.exit_flag.is_set():
                try:
                    self.q.put(e, timeout=TIMEOUT)
                    put_flag = True
                except Full:
                    pass

    def get_next_data(self):
        get_flag = False
        res = ExitStatus()
        while not get_flag and not self.exit_flag.is_set():
            try:
                res = self.q.get(timeout=TIMEOUT)
                get_flag = True
                if isinstance(res, Exception):
                    raise res
                self.q.task_done()
            except Empty:
                pass
        if self.data_mode == MODE_TYPE.PYTORCH:
            return DataPytorchCeil(res)
        else:
            return DataTensorflowCeil(res)

    def _check_sql(self, sql: MetaSQL):
        counts = None
        try:
            ds_name = _generate_tablename("tds_api")
            self.release_list.append(ds_name)
            if sql.groupflag == GROUP_FLAG.PIVOTBY.value:
                self.mode = self.mode if self.mode != LOAD_MODE.UNKNOWN else LOAD_MODE.PIVOTBY
                sql_tmp = copy.deepcopy(sql)
                sql_tmp.groupflag = GROUP_FLAG.GROUPBY.value
                sql_tmp.select = sql_tmp._groupby[:-1]
                sql_tmp.groupby = sql_tmp._groupby[:-1]
                counts = self.s.run(f"exec count(*) from (eval({sql_tmp.run(self.s)}))")
                ds_name = (ds_name, f"{ds_name} = eval({sql.run(self.s)});")
                if self.verbose:
                    print(f"PIVOTBY: {ds_name} = eval({sql.run(self.s)});")
            else:
                self.mode = self.mode if self.mode != LOAD_MODE.UNKNOWN else LOAD_MODE.SQLDS
                if self.forcePartition:
                    self.s.run(f"{ds_name} = sqlDS({sql.run(self.s)}, true);")
                    if self.verbose:
                        print(f"SQLDS: {ds_name} = sqlDS({sql.run(self.s)}, true);")
                else:
                    self.s.run(f"{ds_name} = sqlDS({sql.run(self.s)}, false);")
                    if self.verbose:
                        print(f"SQLDS: {ds_name} = sqlDS({sql.run(self.s)}, false);")
                sql_count = copy.deepcopy(sql)
                sql_count.select = "< count(*) as count >"
                counts = self.s.run(f"{self.func_name}({sql_count.run(self.s)})")
        except Exception as e:
            raise RuntimeError("Error Occurred when creating sqlDS, please check your sql and other arguments.\n" + str(e))
        return ds_name, counts

    def _get_data_with_tbName(self, temp_name):
        get_data_script = f"select {self.all_cols} from {temp_name};"
        try:
            data_array = self.s.run(get_data_script, pickleTableToList=True)
            data_array = self._convertFormat(data_array)
            data_array = np.array(data_array)
            ndim, data = self._transform_tensor_from_array(data_array)
            return True, data, ndim
        except Exception as e:
            print(f"Error Occured when executing sql: {e}")
            time.sleep(3)
            return False, None, None

    def _convertFormat(self, data):
        res = []
        for item in data:
            typestr = repr(type(item.dtype))
            if typestr.find("datetime") == -1:
                res.append(item)
            else:
                res.append(item.astype(np.int64))
        return res

    def _transform_tensor_from_array(self, array):
        ndim = array.ndim
        if ndim == 2:
            array = array.T
        elif ndim == 3:
            array = np.transpose(array, (1, 0, 2))
        else:
            raise RuntimeError(f"Please check your sql, expected data ndim=2/3, but get {ndim}.")

        if self.data_mode == MODE_TYPE.PYTORCH:
            ans = utils.torch.tensor(array, device=self.device)
        elif self.data_mode == MODE_TYPE.TENSORFLOW:
            with utils.tf.device(self.device):
                ans = utils.tf.convert_to_tensor(array)
        return ndim, ans

    def _generate_colnames(self, temp_name):
        if hasattr(self, "schema"):
            return
        schema = self.s.run(f"schema({temp_name})")["colDefs"]
        all_cols = list(schema[schema["typeInt"].apply(_check_category) == 1]["name"].values)
        if self.sql_mode == "INPUT":
            if self.input_cols is not None:
                all_cols = [x for x in all_cols if x in self.input_cols]
            elif self.exclude_cols is not None:
                all_cols = [x for x in all_cols if x not in self.exclude_cols]
        elif self.sql_mode == "TARGET":
            all_cols = [x for x in all_cols if x in self.target_cols]
        if len(all_cols) == 0:
            raise RuntimeError("No valid columns for data. Check inputCols/targetCols/excludeCols is valid.")
        self.all_cols = ",".join(all_cols)
        self.schema = schema
