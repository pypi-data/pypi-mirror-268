import copy
import random
from math import ceil, gcd
from typing import List

import numpy as np
# import torch
# from torch import Tensor
# import tensorflow as tf
from . import utils
# from .utils import torch,tf
# Tensor=torch.Tensor


class QueryTree:
    def __init__(self, size):
        self.pa = np.arange(size + 1, dtype="int64")

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        rex = self.find(x)
        rey = self.find(y)
        if rex < rey:
            self.pa[rey] = rex
        else:
            self.pa[rex] = rey

    def update_range(self, L, R, val=1):
        L += 1
        R += 1
        for i in range(L, R + 1):
            self.union(i, i - 1)

    def query(self, L, R):
        L += 1
        R += 1
        pL = self.find(L)
        pR = self.find(R)
        return pL == pR and pL != L and pR != R


class DataCeil:
    def __init__(self, data) -> None:
        self.data = data

    def __add__(self, other):
        raise NotImplementedError

    def __getitem__(self, key):
        return self.__class__(self.data[key])

    def __len__(self):
        return len(self.data)

    @classmethod
    def cat(cls, datas):
        raise NotImplementedError

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self)

    def get_data(self):
        raise NotImplementedError


def get_data_func(res_L, res_R):
    def datafunc(iv, islower):
        if islower:
            return (iv.begin, res_L, iv.data[2][:res_L-iv.begin])
        else:
            return (res_R, iv.end, iv.data[2][res_R-iv.end:])
    return datafunc


class DataListCeil(DataCeil):
    def __init__(self, data: List[int]) -> None:
        super().__init__(data)

    def __add__(self, other):
        return DataListCeil(self.data + other.data)

    @classmethod
    def cat(cls, datas: List[DataCeil]):
        res = DataListCeil([])
        for data in datas:
            if data is not None:
                res = res + data
        return res

    def get_data(self):
        return utils.torch.tensor(self.data)


class DataPytorchCeil(DataCeil):

    def __init__(self, data) -> None:
        super().__init__(data)

    def __add__(self, other):
        return DataPytorchCeil(utils.torch.cat([self.data, other.data], 0))

    @classmethod
    def cat(cls, datas: List[DataCeil]):
        return DataPytorchCeil(utils.torch.cat([_.data for _ in datas if _ is not None], 0))

    def get_data(self):
        return self.data


class DataTensorflowCeil(DataCeil):

    def __init__(self, data) -> None:
        super().__init__(data)

    def __add__(self, other):
        return DataTensorflowCeil(utils.tf.concat([self.data, other.data], axis=0))

    @classmethod
    def cat(cls, datas: List[DataCeil]):
        return DataTensorflowCeil(utils.tf.concat([_.data for _ in datas if _ is not None], axis=0))

    def get_data(self):
        return self.data


class Interval:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __add__(self, other):
        if isinstance(other, Interval):
            if self.right != other.left:
                raise ValueError("Can't concat!")
            self_class = type(self)
            ans = self_class(self.left, other.right)
            return ans
        else:
            raise TypeError("Interval only add with Interval.")

    def __str__(self) -> str:
        return f"[{self.left}, {self.right}]"

    def __repr__(self) -> str:
        return self.__str__()


class IntervalBox:
    def __init__(self, threshold: int, limit_L: int, limit_R: int) -> None:
        self.threshold = threshold
        self.limit_L = limit_L
        self.limit_R = limit_R
        self.L_box = dict()
        self.R_box = dict()

    def add(self, item: Interval):
        if item.left in self.R_box.keys():
            tmp_item1: Interval = self.R_box.pop(item.left)
            tmp_item2: Interval = self.L_box.pop(tmp_item1.left)
            assert tmp_item1 is tmp_item2
            item: Interval = tmp_item1 + item
        if item.right in self.L_box.keys():
            tmp_item1: Interval = self.L_box.pop(item.right)
            tmp_item2: Interval = self.R_box.pop(tmp_item1.right)
            assert tmp_item1 is tmp_item2
            item: Interval = item + tmp_item1
        self.L_box[item.left] = item
        self.R_box[item.right] = item

    def __len__(self):
        assert len(self.L_box) == len(self.R_box)
        return len(self.L_box)

    def random(self, random_ins: random.Random):
        index = random_ins.randint(0, len(self)-1)
        index = list(self.L_box.keys())[index]
        item: Interval = self.L_box[index]
        if item.left == self.limit_L:
            return item.right, item.right+1
        if item.right == self.limit_R:
            return item.left-1, item.left
        return (item.left-1, item.left) if random_ins.random() > 0.5 else (item.right, item.right+1)

    def check_full(self) -> bool:
        if len(self.L_box) != 1:
            return False
        if len(self.R_box) != 1:
            return False
        if self.limit_L not in self.L_box.keys():
            return False
        if self.limit_R not in self.R_box.keys():
            return False
        if self.L_box[self.limit_L] is not self.R_box[self.limit_R]:
            return False
        return True

    def __repr__(self) -> str:
        s = ",".join([str(self.L_box[x]) for x in self.L_box])
        return f"IntervalBox[{s}]"


class RandomSampleHelper:
    def __init__(self, size: int, threshold: int = 10, seed: int = 0) -> None:
        self.q_n = size
        self.threshold = threshold
        self.random_ins = random.Random(seed)
        self.seed = seed

    def __iter__(self):
        self.random_ins.seed(self.seed)
        self.all_q = [Interval(i, i+1) for i in range(self.q_n)]
        self.res_q = IntervalBox(self.threshold, 0, self.q_n)
        return self

    def __next__(self):
        if self.res_q.check_full() or self.q_n == 0:
            raise StopIteration
        if len(self.res_q) < self.threshold:
            random_sample = self.random_ins.sample(self.all_q, 1)[0]
            self.all_q.remove(random_sample)
            self.res_q.add(random_sample)
            return random_sample.left
        else:
            chs_index_L, chs_index_R = self.res_q.random(self.random_ins)
            chs_item = None
            for item in self.all_q:
                if item.left == chs_index_L and item.right == chs_index_R:
                    chs_item = item
            self.all_q.remove(chs_item)
            self.res_q.add(chs_item)
            return chs_item.left


class DataIndexHelper:
    def __init__(self, prefix_sum, sampler, window_size, window_stride, seed=0, enableScale=True):
        self.prefix_sum = copy.deepcopy(prefix_sum)
        self.sampler = sampler
        self.window_size = window_size if window_size is not None else 1
        self.window_stride = window_stride if window_stride is not None else 1
        if enableScale:
            self._cal_scale()
        self.seed = seed
        self.random_ins = np.random.RandomState(seed)

    def _cal_scale(self):
        scale = gcd(self.window_size, self.window_stride)
        for val in self.prefix_sum:
            scale = gcd(scale, val)
        self.window_size //= scale
        self.window_stride //= scale
        for i in range(len(self.prefix_sum)):
            self.prefix_sum[i] //= scale

    def _cal_data_index_by_partition_list(self, prefix_sum, order_list, wsize, wstride):
        self.random_ins.seed(self.seed)
        p_n = len(order_list)
        data_n = (prefix_sum[p_n] - prefix_sum[0] - wsize) // wstride + 1
        data_n = max(data_n, 0)
        segt = QueryTree(prefix_sum[p_n])
        segm = np.zeros(data_n, dtype="bool")
        for p_index in order_list:
            L = prefix_sum[p_index]
            R = prefix_sum[p_index+1]-1
            index_L = L // wstride - (wsize - L % wstride - 1) // wstride
            index_L = max(0, index_L)
            index_R = (R) // wstride + 1
            index_R = min(index_R, data_n)
            inner_L = ceil(L / wstride)
            inner_R = (R - wsize+1) // wstride

            p_data = np.arange(inner_L, inner_R+1)
            self.random_ins.shuffle(p_data)
            for data in p_data:
                segm[data] = True
                yield data
            if inner_L > inner_R:
                segt.update_range(L, R, 1)
            else:
                segt.update_range(L, (inner_L-1)*wstride+wsize-1, 1)
                segt.update_range((inner_R+1) * wstride, R, 1)
            index_list = np.arange(index_L, inner_L, 1)
            self.random_ins.shuffle(index_list)
            for index in index_list:
                data_L = index * wstride
                data_R = index * wstride + wsize
                if self.query_tree(segt, segm, index, data_L, data_R, 0, data_n-1):
                    segm[index] = True
                    yield index
            index_list = np.arange(inner_R+1, index_R, 1)
            self.random_ins.shuffle(index_list)
            for index in index_list:
                data_L = index * wstride
                data_R = index * wstride + wsize
                if self.query_tree(segt, segm, index, data_L, data_R, 0, data_n-1):
                    segm[index] = True
                    yield index

    def query_tree(self, segt: QueryTree, segm, index, begin: int, end: int, L_limit: int, R_limit: int):
        if index < L_limit or index > R_limit or segm[index]:
            return False
        return segt.query(begin, end-1)

    def __iter__(self):
        return self._cal_data_index_by_partition_list(
            self.prefix_sum,
            self.sampler,
            self.window_size,
            self.window_stride,
        )
