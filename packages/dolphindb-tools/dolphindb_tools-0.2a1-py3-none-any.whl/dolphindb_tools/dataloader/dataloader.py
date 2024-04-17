import copy
import random
from queue import Empty, Full, Queue
from threading import Event, Thread
from typing import List, Optional, Union


from dolphindb import session as Session

from .config import TIMEOUT
from .datamanager import DataManager
from .datasource import DataRealSource
from .helper import DataIndexHelper, RandomSampleHelper
from .utils import (MetaSQL, SequentialSession, _generate_tablename,
                    make_MetaSQL, MODE_TYPE, import_framework)
from . import utils


class DDBDataLoader(object):
    """The DDBDataLoader class is used to import data stored in DolphinDB for
    machine learning.

    Args:
        ddbSession (Session): Session connection used to obtain data,
        including contextual information required for training.

        sql (str): metacode of SQL statements to extract data for training.
        Currently TOP, LIMIT, GROUP BY and CONTEXT BY clauses are not supported.

        targetCol (Union[List[str], str]): a list of str, indicating the column
        name corresponding to y in the iteration.

    Kwargs:
        batchSize (int, optional): batch size that specifies the number of
        messages in each batch of data. Defaults to 1.

        shuffle (bool, optional): whether to randomly shuffle the data.
        Defaults to False.

        windowSize (Union[List[int], int, None], optional): the size of the
        sliding window. If not specified, sliding window will not be used.
        Defaults to None.
        - If an integer (int) is specified, e.g., windowSize=3, the sliding
        window size of x is 3 and the sliding window size of y is 1.
        - If a list with 2 integers is specified, e.g., windowSize=[4, 2],
        the sliding window size of x is 4 and the sliding window size of y is 2.

        windowStride (Union[List[int], int, None], optional): sliding step of
        the window. This parameter only takes effect when windowSize is specified.
        Defaults to None.
        - If an integer (int) is specified, e.g., windowStride=2, the sliding
        step of x is 2 and the sliding step of y is 1.
        - If a list with 2 integers is specified, e.g., windowStride=[3, 1],
        the sliding step for x is 3 and the sliding step for y is 1.

        inputCol (Optional[Union[List[str], str]], optional): a list of str,
        indicating the column name corresponding to x in the iteration. If not
        specified, it indicates all columns. Defaults to None.

        excludeCol (Optional[Union[List[str], str]], optional): a list of str,
        indicating the column names excluded by x in the iteration. Defaults to None.

    Note:
        - If inputCol is specified, x is the column corresponding to inputCol,
        and y is the column corresponding to targetCol. excludeCol will not take effect.

        - If inputCol is unspecified and excludeCol is specified, x is all columns
        excluding excludeCol, and y is the column corresponding to targetCol.

        - If neither inputCol or excludeCol is specified, x indicates all columns,
        and y is the column corresponding to targetCol.

    Kwargs:
        repartitionCol (str, optional): column used to further split the grouped
        query into subqueries. Defaults to None.

        repartitionScheme (List[str], optional): a list of str indicating the partition
        values. Data is further filtered and split based on the list element and
        repartitionCol column. Defaults to None.

        groupCol (str, optional): column used to divide the query into groups.
        Defaults to None.

        groupScheme (List[str], optional): a list of str indicating the group values.
        Data is further filtered and split based on the list element and groupCol
        column. Defaults to None.

    Note:
        - The parameters repartitionCol and repartitionScheme can be used if a single
        partition has a large amount of data that cannot be directly processed.
        By filtering the data based on the value of repartitionScheme, the data can be
        split into multiple subpartitions, each of which will be ordered in the
        repartitionScheme. For example, if repartitionCol is date(TradeTime) and
        repartitionScheme is ["2020.01.01", "2020.01.02", "2020.01.03"], the data will
        be subdivided into three partitions, each partition corresponding to a date value.

        - Different from repartitionCol/repartitionScheme, no cross-group data will be
        generated if groupCol/groupScheme is used. For example, if groupCol is Code
        and groupScheme is ["`000001.SH", "`000002.SH", "`000003. SH"], the data will be
        divided into three groups, each group corresponding to a stock code.

    Kwargs:
        seed (Optional[int], optional): random seed, which only takes effect within
        the DDBDataLoader object. Defaults to None, meaning no random seed is specified.

        dropLast (bool, optional): whether to discard the last batch of messages
        that is less than batchSize when batchSize cannot divide the size of the
        query result. Defaults to False, meaning that the last batch that is less
        than batchSize will not be discarded.

        offset (int, optional): a non-negative integer indicating the number of rows
        y is offset from x. If windowSize is specified, the default value is the
        window size of x. If windowSize is not specified, the default value is 0,
        meaning that the training data are all in the same row.

        mode (str, optional): the deep learning framework used by DDBDataLoader.
        Its value can be "pytorch" (default) or "tensorflow".

        device (Optional[str], optional): device on which the tensor will be created.
        Set this to "cuda" or device name supported by torch.device and tf.device
        to create tensors on the GPU.

        prefetchBatch (int, optional): the number of batches preloaded in the
        background. Defaults to 1.

        prepartitionNum (int, optional): the number of preloaded partitions for
        each data source. The worker thread will preload the partition into memory
        in the background. Defaults to 2. Note that too many preloaded partitions
        may result in insufficient memory.

        groupPoolSize (int, optional): the number of data sources selected for data
        preparation if groupCol and groupScheme are specified. If a selected source
        is used, a new one will be added until all data sources are used.
        Defaults to 3.
    """
    def __init__(
        self,
        ddbSession: Session,
        sql: str,
        targetCol: Union[List[str], str],
        batchSize: int = 1,
        shuffle: bool = False,
        windowSize: Union[List[int], int, None] = None,
        windowStride: Union[List[int], int, None] = None,
        *,
        inputCol: Optional[Union[List[str], str]] = None,
        excludeCol: Optional[Union[List[str], str]] = None,
        repartitionCol: str = None,
        repartitionScheme: List[str] = None,
        groupCol: str = None,
        groupScheme: List[str] = None,
        seed: Optional[int] = None,
        dropLast: bool = False,
        offset: int = None,
        mode: str = "pytorch",
        device: Optional[str] = None,
        prefetchBatch: int = 1,
        prepartitionNum: int = 2,
        groupPoolSize: int = 3,
        **kwargs
    ):
        if not isinstance(ddbSession, Session):
            raise TypeError("The type of ddbSession must be dolphindb.Session.")
        self.s: Session = SequentialSession(ddbSession)

        if groupCol is not None and not isinstance(groupCol, str):
            raise TypeError("The type of groupCol must be str.")
        self.group_col = groupCol
        self.group_scheme = groupScheme

        if repartitionCol is not None and not isinstance(repartitionCol, str):
            raise TypeError("The type of repartitionCol must be str.")
        self.repartition_col = repartitionCol
        self.repartition_scheme = repartitionScheme

        if not isinstance(mode, str):
            raise TypeError("The type of mode must be str.")

        if mode == MODE_TYPE.PYTORCH.value:
            self.mode = MODE_TYPE.PYTORCH
            import_framework(MODE_TYPE.PYTORCH)
        elif mode == MODE_TYPE.TENSORFLOW.value:
            self.mode = MODE_TYPE.TENSORFLOW
            import_framework(MODE_TYPE.TENSORFLOW)
        else:
            raise ValueError("The value of mode must be 'pytorch' or 'tensorflow'.")

        self.device = device

        if not isinstance(prefetchBatch, int):
            raise TypeError("The type of prefetchBatch must be int.")
        if prefetchBatch <= 0:
            raise ValueError("The value of prefetchBatch must be greater than 0.")
        self.prefetch = prefetchBatch

        if not isinstance(prepartitionNum, int):
            raise TypeError("The type of prepartitionNum must be int.")
        if prepartitionNum <= 0:
            raise ValueError("The value of prepartitionNum must be greater than 0.")
        self.prepartition_num = prepartitionNum

        if not isinstance(groupPoolSize, int):
            raise TypeError("The type of groupPoolSize must be int.")
        if groupPoolSize <= 0:
            raise ValueError("The value of groupPoolSize must be greater than 0.")
        self.grouppool_size = groupPoolSize

        if not isinstance(sql, str):
            raise TypeError("The type of sql must be str.")
        sql = make_MetaSQL(ddbSession, sql)
        sqls = self._take_group_effect(groupCol, groupScheme, sql)
        self.sqls = self._take_repartition_effect(repartitionCol, repartitionScheme, sqls)

        if windowSize is None:
            self.window_size = [None, None]
        elif isinstance(windowSize, int):
            self.window_size = [windowSize, 1]
        elif isinstance(windowSize, list):
            if len(windowSize) != 2:
                raise ValueError("windowSize must be an int or a list with 2 int.")
            self.window_size = windowSize
        else:
            raise ValueError("windowSize must be an int or a list with 2 int.")

        if windowStride is None:
            self.window_stride = [None, None]
        elif isinstance(windowStride, int):
            self.window_stride = [windowStride, 1]
        elif isinstance(windowStride, list):
            if len(windowStride) != 2:
                raise ValueError("windowStride must be an int or a list with 2 int.")
            self.window_stride = windowStride
        else:
            raise ValueError("windowStride must be an int or a list with 2 int.")

        if offset is None:
            if self.window_size[0] is not None:
                offset = self.window_size[0]
            else:
                offset = 0
        if not isinstance(offset, int):
            raise TypeError("The type of offset must be int.")
        if offset < 0:
            raise ValueError("The value of offset must be no less than 0.")
        self.offset = offset

        if not isinstance(batchSize, int):
            raise TypeError("The type of batchSize must be int.")
        if batchSize <= 0:
            raise ValueError("The value of batchSize must be greater than 0.")
        self.batch_size = batchSize

        self.shuffle = shuffle
        self.drop_last = dropLast

        if inputCol is not None:
            if isinstance(inputCol, str):
                inputCol = [inputCol]
            if not isinstance(inputCol, list):
                raise TypeError("The type of inputCol must be str or list of str.")
        self.input_cols = inputCol

        if isinstance(targetCol, str):
            targetCol = [targetCol]
        if not isinstance(targetCol, list):
            raise TypeError("The type of targetCol must be str or list of str.")
        self.target_cols = targetCol

        if excludeCol is not None:
            if isinstance(excludeCol, str):
                excludeCol = [excludeCol]
            if not isinstance(excludeCol, list):
                raise TypeError("The type of excludeCol must be str or list of str.")
        self.exclude_cols = excludeCol if excludeCol is not None else []

        if "verbose" in kwargs:
            self.verbose = bool(kwargs["verbose"])
        else:
            self.verbose = False

        self.seed = seed
        self.random_ins = random.Random(seed)
        self._define_helper_func()
        self.release_flag = False
        self.dms = self.sqls

    def _take_group_effect(self, group_col, group_scheme, sql: MetaSQL):
        if group_col is None and group_scheme is None:
            return [sql]
        if not (group_col and group_scheme):
            raise ValueError("Both groupCol and groupScheme must be specified simultaneously.")
        if not isinstance(group_col, str):
            raise TypeError("The type of groupCol must be str.")
        if not isinstance(group_scheme, list):
            raise TypeError("The type of groupScheme must be list of str.")
        res_sqls = []
        for scheme in group_scheme:
            scheme = str(scheme)
            res_sql = copy.deepcopy(sql)
            res_sql.add_where([f"< {group_col} = {scheme} >"])
            res_sqls.append(res_sql)
        return res_sqls

    def _take_repartition_effect(self, repartition_col, repartition_scheme, sqls):
        if repartition_col is None and repartition_scheme is None:
            return [[sql] for sql in sqls]
        if not (repartition_col and repartition_scheme):
            raise ValueError("Both repartitionCol and repartitionScheme must be specified simultaneously.")
        if not isinstance(repartition_col, str):
            raise TypeError("The type of repartitionCol must be str.")
        if not isinstance(repartition_scheme, list):
            raise TypeError("The type of repartitionScheme must be list of str.")
        res_sqls = [[] for _ in range(len(sqls))]
        for i, sql in enumerate(sqls):
            for scheme in repartition_scheme:
                res_sql = copy.deepcopy(sql)
                res_sql.add_where([f"< {repartition_col} = {scheme} >"])
                res_sqls[i].append(res_sql)
        return res_sqls

    def _define_helper_func(self):
        self.func_name = _generate_tablename("UTIL_HELPER")
        self.s.run("""
            def """ + f"{self.func_name}" + """(sql){
                tmp = sqlDS(sql, true);
                length = size tmp;
                if(length == 0){return NULL}
                counts = array(LONG, length);
                for(i in 0..(length-1)){
                    counts[i] = exec * from tmp[i]
                }
                return counts
            }
        """)

    def __del__(self):
        try:
            self.release()
        except Exception:
            pass

    def release(self):
        if not self.release_flag:
            self.s.run(f"undef('{self.func_name}', DEF);")
            self.release_flag = True

    def __iter__(self):
        if self.seed is None:
            new_seed = self.random_ins.randint(0, 10000)
            self.random_ins.seed(new_seed)
            self.new_seed = new_seed
        else:
            self.random_ins.seed(self.seed)
        self.queue = Queue(self.prefetch)
        self.dm_queue = Queue(1)
        self.back_thread = Thread(target=self._prepare_next_batch)
        self.back_thread.start()
        return self._get_next_batch_data()

    def _get_next_batch_data(self):
        while True:
            ndata = self.queue.get()
            self.queue.task_done()
            if ndata is None:
                break
            elif isinstance(ndata, Exception):
                raise ndata
            x, y = ndata
            if self.mode == MODE_TYPE.PYTORCH:
                if self.window_size[0] is None:
                    x = utils.torch.squeeze(x, dim=1)
                if self.window_size[1] is None:
                    y = utils.torch.squeeze(y, dim=1)
            elif self.mode == MODE_TYPE.TENSORFLOW:
                if self.window_size[0] is None:
                    x = utils.tf.squeeze(x, axis=1)
                if self.window_size[1] is None:
                    y = utils.tf.squeeze(y, axis=1)
            yield x, y
        self.back_thread.join()

    def _prepare_next_batch(self):
        try:
            dm_pool_size = self.grouppool_size
            dms = copy.deepcopy(self.dms)
            exit_flag = Event()
            self.dm_thread = Thread(target=self._prepare_next_data_manager, args=(dms, exit_flag))
            self.dm_thread.start()
            dm_iter = self._get_next_data_manager(len(self.dms), exit_flag)

            generators = [next(dm_iter) for _ in range(min(len(self.dms), dm_pool_size))]

            data_rows = [[], []]
            all_flag = True
            while len(generators) != 0:
                ndata = []
                try:
                    if self.shuffle:
                        random_generator = self.random_ins.choice(generators)
                    else:
                        random_generator = generators[0]
                    data_row = [next(dm[0]) for dm in random_generator]
                    for i, data in enumerate(data_row):
                        data_rows[i].append(data)
                        if self.mode == MODE_TYPE.PYTORCH:
                            if len(data_rows[i]) >= self.batch_size:
                                ndata.append(utils.torch.stack([_ for _ in data_rows[i]]))
                                data_rows[i] = []
                        elif self.mode == MODE_TYPE.TENSORFLOW:
                            if len(data_rows[i]) >= self.batch_size:
                                ndata.append(utils.tf.stack([_ for _ in data_rows[i]]))
                                data_rows[i] = []
                    if len(ndata) > 0:
                        self.queue.put(ndata)
                except StopIteration:
                    for dm in random_generator:
                        dm[1].exit()
                    generators.remove(random_generator)
                    if all_flag:
                        try:
                            new_generator = next(dm_iter)
                            generators.append(new_generator)
                        except StopIteration:
                            all_flag = False
            if len(data_rows[0]) and not self.drop_last:
                ndata = []
                if self.mode == MODE_TYPE.PYTORCH:
                    for data in data_rows:
                        ndata.append(utils.torch.stack([_.data for _ in data]))
                elif self.mode == MODE_TYPE.TENSORFLOW:
                    for data in data_rows:
                        ndata.append(utils.tf.stack([_.numpy() for _ in data]))
                self.queue.put(ndata)
            self.queue.put(None)
            self.dm_thread.join()
        except Exception as e:
            exit_flag.set()
            self.queue.put(e)
            self.dm_thread.join()

    def _prepare_next_data_manager(self, dms, exit_flag: Event):
        if self.seed is None:
            seed = self.new_seed
        else:
            seed = self.seed
        try:
            while len(dms) > 0 and not exit_flag.is_set():
                if self.shuffle:
                    sql_sample = self.random_ins.sample(dms, k=1)[0]
                else:
                    sql_sample = dms[0]
                dms.remove(sql_sample)
                dm_pair = self._create_data_manager(sql_sample, seed)
                dm = self._start_data_manager(dm_pair, exit_flag)

                put_flag = False
                while not put_flag and not exit_flag.is_set():
                    try:
                        self.dm_queue.put(dm, timeout=TIMEOUT)
                        put_flag = True
                    except Full:
                        pass
        except Exception as e:
            put_flag = False
            while not put_flag and not exit_flag.is_set():
                try:
                    self.dm_queue.put(e, timeout=TIMEOUT)
                    put_flag = True
                except Full:
                    pass

    def _get_next_data_manager(self, all_len, exit_flag: Event):
        while all_len and not exit_flag.is_set():
            get_flag = False
            while not get_flag and not exit_flag.is_set():
                try:
                    dm = self.dm_queue.get(timeout=TIMEOUT)
                    get_flag = True
                    if isinstance(dm, Exception):
                        raise dm
                    else:
                        yield dm
                    self.dm_queue.task_done()
                    all_len -= 1
                except Empty:
                    pass

    def _create_data_manager(self, sqls, seed):
        input_window_size = self.window_size[0] if self.window_size[0] is not None else 1
        target_window_size = self.window_size[1] if self.window_size[1] is not None else 1
        input_window_stride = self.window_stride[0] if self.window_stride[0] is not None else 1
        target_window_stride = self.window_stride[1] if self.window_stride[1] is not None else 1

        ds_input = DataRealSource(
            self.s, sqls,
            "INPUT", self.func_name,
            input_cols=self.input_cols,
            target_cols=self.target_cols,
            exclude_cols=self.exclude_cols,
            offset=0, data_mode=self.mode, device=self.device,
            q_size=self.prepartition_num,
            verbose=self.verbose,
        )
        ds_target = DataRealSource(
            self.s, sqls,
            "TARGET", self.func_name,
            input_cols=self.input_cols,
            target_cols=self.target_cols,
            exclude_cols=self.exclude_cols,
            offset=self.offset, data_mode=self.mode, device=self.device,
            q_size=self.prepartition_num,
            verbose=self.verbose,
        )
        data_num_input = (ds_input.data_len() - input_window_size) // input_window_stride + 1
        data_num_target = (ds_target.data_len() - target_window_size) // target_window_stride + 1

        if self.shuffle and data_num_input <= data_num_target:
            p_sampler = [_ for _ in RandomSampleHelper(len(ds_input), seed=seed)]
            index_list = DataIndexHelper(
                ds_input.prefix_sum, p_sampler,
                self.window_size[0], self.window_stride[0],
                seed=seed,
            )
        elif self.shuffle:
            p_sampler = [_ for _ in RandomSampleHelper(len(ds_target), seed=seed)]
            index_list = DataIndexHelper(
                ds_target.prefix_sum, p_sampler,
                self.window_size[1], self.window_stride[1],
                seed=seed,
            )
        else:
            index_list = [_ for _ in range(min(data_num_input, data_num_target))]
        return [
            (ds_input, index_list, self.window_size[0], self.window_stride[0]),
            (ds_target, index_list, self.window_size[1], self.window_stride[1]),
        ]

    def _start_data_manager(self, dm_pair, exit_flag: Event):
        dms = []
        for dm_msg in dm_pair:
            ds, index, wsize, wstride = dm_msg
            dm = DataManager(ds, index, wsize, wstride, exit_flag=exit_flag)
            dm.start()
            dms.append([iter(dm), dm])
        return dms
