
import bisect
import copy
from queue import Empty, Full, Queue
from threading import Event, Thread

from intervaltree import IntervalTree

from .config import TIMEOUT
from .datasource import DataSource
from .helper import DataCeil, get_data_func
from .utils import ExitStatus


class DataManager(object):
    def __init__(
        self, data_source: DataSource, sampler,
        window_size=None, window_stride=None,
        exit_flag: Event = None
    ) -> None:
        self.window_size = window_size if window_size is not None else 1
        self.window_stride = window_stride if window_stride is not None else 1
        self.data_source = data_source

        self.t = IntervalTree()
        self.markd = dict()
        self.is_foreign = exit_flag is not None
        self.exit_flag = exit_flag if exit_flag is not None else Event()
        self.prefix_sum = data_source.prefix_sum
        self.sampler = copy.deepcopy(sampler)

        self._cal_p_index_list()

    def clear(self):
        self.t.clear()
        self.markd.clear()
        if not self.is_foreign:
            self.exit_flag.clear()

    def start(self):
        if hasattr(self, "back_thread"):
            raise RuntimeError("DataManager can not start twice.")
        self.clear()
        self.q = Queue(4)
        self.back_thread = Thread(target=self._prepare_data)
        self.back_thread.start()

    def join(self):
        if not hasattr(self, "back_thread"):
            raise RuntimeError("DataManager has not started.")
        self.back_thread.join()
        del self.back_thread
        del self.q

    def __del__(self):
        self.exit()

    def exit(self):
        if hasattr(self, "back_thread") and not self.exit_flag.is_set():
            if not self.is_foreign:
                self.exit_flag.set()
            self.data_source.exit()
            self.join()

    def _prepare_data(self):
        try:
            for index in self.sampler:
                data = self[index]
                if isinstance(data, ExitStatus):
                    break
                put_flag = False
                while not put_flag and not self.exit_flag.is_set():
                    try:
                        self.q.put(data, timeout=TIMEOUT)
                        put_flag = True
                    except Full:
                        pass
                if self.exit_flag.is_set():
                    break
            self.q.put(None)
            if self.exit_flag.is_set():
                self.data_source.exit()
        except Exception as e:
            put_flag = False
            self.data_source.exit()
            while not put_flag and not self.exit_flag.is_set():
                try:
                    self.q.put(e, timeout=TIMEOUT)
                    put_flag = True
                except Full:
                    pass

    def __iter__(self):
        return self._get_next_index_data()

    def _get_next_index_data(self):
        done_flag = False
        while not done_flag:
            get_flag = False
            while not get_flag and not self.exit_flag.is_set():
                try:
                    res = self.q.get(timeout=TIMEOUT)
                    get_flag = True
                    if res is None:
                        done_flag = True
                        break
                    elif isinstance(res, Exception):
                        raise res
                    else:
                        yield res
                    self.q.task_done()
                except Empty:
                    pass

    def __getitem__(self, index):
        index_L = index * self.window_stride
        index_R = index_L + self.window_size - 1
        p_i, p_j = self.get_block_by_range(index_L, index_R)
        data = []
        if p_i == p_j:
            data = self._query_by_index(p_i, index_L, index_R+1)
            if isinstance(data, ExitStatus):
                return data
            self.remove(index)
            self.markd[index] = 1
            return data.get_data()
        for i in range(p_i, p_j+1):
            if self.prefix_sum[i+1] == self.prefix_sum[i]:
                continue
            tmp_L = max(self.prefix_sum[i], index_L)
            tmp_R = min(self.prefix_sum[i+1], index_R+1)
            tmp_data = self._query_by_index(i, tmp_L, tmp_R)
            if isinstance(tmp_data, ExitStatus):
                return tmp_data
            data.append(tmp_data)
        data = data[0].__class__.cat(data)
        self.remove(index)
        self.markd[index] = 1
        return data.get_data()

    def _query_by_index(self, index, index_L, index_R):
        p_index_L = self.prefix_sum[index]
        p_index_R = self.prefix_sum[index+1]
        if self._check_in_memory(index_L, index_R):
            return self._query_by_index_L_R(index_L, index_R)
        else:
            data: DataCeil = self.data_source.get_next_data()
            if isinstance(data, ExitStatus):
                return data
            self._merge_cache(p_index_L, p_index_R, data)
            data = self._query_by_index_L_R(index_L, index_R)
            return data

    def _cal_p_index_list(self):
        def cal_res_list(sampler):
            res_set = set()
            for index in sampler:
                index_L = index * self.window_stride
                index_R = index_L + self.window_size - 1
                p_i, p_j = self.get_block_by_range(index_L, index_R)
                for i in range(p_i, p_j+1):
                    if i not in res_set:
                        res_set.add(i)
                        if self.prefix_sum[i+1] - self.prefix_sum[i] != 0:
                            yield i

        self.data_source.start(cal_res_list(copy.deepcopy(self.sampler)))

    def dslen(self):
        return len(self.prefix_sum) - 1

    def datalen(self):
        return self.prefix_sum[-1] - self.prefix_sum[0]

    def remove(self, index):
        L = index * self.window_stride
        R = L + self.window_size
        wsize, wstride = self.window_size, self.window_stride
        data_n = (self.datalen() - wsize) // wstride + 1
        index_L = L // wstride - (wsize - L % wstride - 1) // wstride
        index_L = max(0, index_L)
        index_R = (R) // wstride + 1
        index_R = min(index_R, data_n)

        res_L, res_R = R - wstride, L + wstride
        for tmp_index in range(index-1, index_L-1, -1):
            tmp_L = tmp_index * wstride
            res_L = tmp_L + wsize
            if tmp_index not in self.markd:
                break
        for tmp_index in range(index+1, index_R, 1):
            tmp_R = tmp_index * wstride + wsize
            res_R = tmp_R - wsize
            if tmp_index not in self.markd:
                break
        if res_L < res_R:
            self.t.chop(res_L, res_R, get_data_func(res_L, res_R))

    def _merge_cache(self, index_L, index_R, data):
        res_L = sorted(self.t[:index_L])
        if len(res_L) > 0:
            if res_L[-1].end == index_L:
                data_L = res_L[-1].data
                index_L = res_L[-1].begin
                del self.t[index_L]
                data = data_L[2] + data
        res_R = sorted(self.t[index_R:])
        if len(res_R) > 0:
            if res_R[0].begin == index_R:
                data_R = res_R[0].data
                index_R = res_R[0].end
                del self.t[res_R[0].begin]
                data = data + data_R[2]
        if index_L < index_R:
            self.t[index_L:index_R] = (index_L, index_R, data)

    def _query_by_index_L_R(self, index_L, index_R):
        res = sorted(self.t[index_L:index_R])
        if len(res) == 0:
            return None
        res_L = index_L - res[0].begin
        res_R = res[0].end - index_R
        if res_L == 0 and res_R == 0:
            ans = res[0].data[2]
        elif res_L == 0:
            ans = res[0].data[2][:-res_R]
        elif res_R == 0:
            ans = res[0].data[2][res_L:]
        else:
            ans = res[0].data[2][res_L:-res_R]
        return ans

    def _check_in_memory(self, begin, end):
        res = sorted(self.t[begin:end])
        if len(res) == 0:
            return False
        elif res[0].begin <= begin and res[-1].end >= end:
            return True
        else:
            return False

    def get_block_by_range(self, index_L, index_R):
        p_i = bisect.bisect_left(self.prefix_sum, index_L+1)-1
        p_j = bisect.bisect_left(self.prefix_sum, index_R+1)-1
        return p_i, p_j
