from enum import Enum
from threading import Lock
from typing import Union, List, Optional
import re
import uuid
import importlib

from dolphindb import session as Session
from dolphindb.settings import DT_VOID, DT_BOOL, DT_CHAR, DT_SHORT, DT_INT, DT_LONG
from dolphindb.settings import DT_DATE, DT_MONTH, DT_TIME, DT_MINUTE, DT_SECOND, DT_DATETIME, DT_TIMESTAMP, DT_NANOTIME, DT_NANOTIMESTAMP
from dolphindb.settings import DT_FLOAT, DT_DOUBLE, DT_SYMBOL, DT_STRING, DT_UUID, DT_DATEMINUTE, DT_DATEHOUR, DT_ANY
from dolphindb.settings import DT_IPADDR, DT_INT128, DT_DECIMAL32, DT_DECIMAL64, DT_BLOB, ARRAY_TYPE_BASE

try:
    global torch
    torch = __import__("torch")
except ModuleNotFoundError:
    torch = None

try:
    global tf
    tf = __import__("tensorflow")
except ModuleNotFoundError:
    tf = None


def _generate_tablename(tableName=None):
    if tableName is None:
        return "TMP_TBL_" + uuid.uuid4().hex[:8]
    else:
        return tableName + "_TMP_TBL_" + uuid.uuid4().hex[:8]


def _release_table(sess: Session, tbName: str):
    sess.run(f"{tbName} = NULL; undef `{tbName};")


class ExitStatus(object):
    pass


class DATA_CATEGORY(Enum):
    NOTHING = 0
    LOGICAL = 1
    INTEGRAL = 2
    FLOATING = 3
    TEMPORAL = 4
    LITERAL = 5
    SYSTEM = 6
    MIXED = 7
    BINARY = 8
    COMPLEX = 9
    ARRAY = 10
    DENARY = 11


class MODE_TYPE(Enum):
    PYTORCH = 'pytorch'
    TENSORFLOW = 'tensorflow'


def import_framework(framework):
    if framework == MODE_TYPE.PYTORCH:
        global torch
        if torch is None:
            torch = importlib.import_module('torch')
    elif framework == MODE_TYPE.TENSORFLOW:
        global tf
        if tf is None:
            tf = importlib.import_module("tensorflow")
    else:
        raise ValueError("The value of mode must be pytorch or tensorflow.No AI framework was imported.")
    
    
def getCategory(data_type):
    if data_type in [
        DT_TIME, DT_SECOND, DT_MINUTE, DT_DATE,
        DT_DATEHOUR, DT_DATEMINUTE, DT_DATETIME, DT_MONTH,
        DT_NANOTIME, DT_NANOTIMESTAMP, DT_TIMESTAMP,
    ]:
        return DATA_CATEGORY.TEMPORAL
    elif data_type in [DT_INT, DT_LONG, DT_SHORT, DT_CHAR]:
        return DATA_CATEGORY.INTEGRAL
    elif data_type in [DT_BOOL]:
        return DATA_CATEGORY.LOGICAL
    elif data_type in [DT_DOUBLE, DT_FLOAT]:
        return DATA_CATEGORY.FLOATING
    elif data_type in [DT_STRING, DT_SYMBOL]:
        return DATA_CATEGORY.LITERAL
    elif data_type in [DT_INT128, DT_UUID, DT_IPADDR, DT_BLOB]:
        return DATA_CATEGORY.BINARY
    elif data_type in [DT_ANY]:
        return DATA_CATEGORY.MIXED
    elif data_type in [DT_VOID]:
        return DATA_CATEGORY.NOTHING
    elif data_type in [DT_DECIMAL32, DT_DECIMAL64]:
        return DATA_CATEGORY.DENARY
    elif data_type >= ARRAY_TYPE_BASE:
        return DATA_CATEGORY.ARRAY
    else:
        return DATA_CATEGORY.SYSTEM


def _check_category(data):
    category = getCategory(data)
    if category == DATA_CATEGORY.ARRAY:
        return _check_category(data-ARRAY_TYPE_BASE)
    elif category in [DATA_CATEGORY.INTEGRAL, DATA_CATEGORY.FLOATING, DATA_CATEGORY.LOGICAL]:
        return 1
    else:
        return 0


class LOAD_MODE(Enum):
    UNKNOWN = 0
    PIVOTBY = 1
    SQLDS = 2


class GROUP_FLAG(Enum):
    CONTEXTBY = 0
    GROUPBY = 1
    PIVOTBY = 2
    DEFAULT = 1


class SORT_TYPE(Enum):
    DESC = 0
    ASC = 1


class HINT_TYPE(Enum):
    HINT_LOCAL = 1
    HINT_HASH = 32
    HINT_SNAPSHOT = 64
    HINT_KEEPORDER = 128
    HINT_SEQ = 512
    HINT_NOMERGE = 1024
    HINT_PRELOAD = 4096
    HINT_EXPLAIN = 32768
    HINT_SORT = 524288
    HINT_VECTORIZED = 4194304
    HINT_PYTORCH_TENSOR = 33554432


class SequentialSession:
    def __init__(self, s: Session) -> None:
        self.s = s
        self.mutex = Lock()

    def run(self, *args, **kwargs):
        with self.mutex:
            return self.s.run(*args, **kwargs)


def make_MetaSQL(ddbSession: Session, sql: str):
    pattern = r"\blimit\b"
    matches = re.search(pattern, sql, flags=re.IGNORECASE)
    if matches:
        raise ValueError("sql must not contain LIMIT or TOP clause.")
    pattern = r"\btop\b"
    matches = re.search(pattern, sql, flags=re.IGNORECASE)
    if matches:
        raise ValueError("sql must not contain LIMIT or TOP clause.")

    res = ddbSession.run(f"objectComponent(<{sql}>)")

    select_clause = res["select"]
    from_clause = res["from"]
    where_clause = res["where"]
    groupby_clause = res["groupBy"]
    groupflag_clause = GROUP_FLAG[res["groupFlag"]] if res["groupFlag"] is not None else None
    csort_clause = [x["sortColumn"] for x in res["csort"]]
    ascsort_clause = [int(x["isAscending"]) for x in res["csort"]]
    having_clause = res["having"]
    orderby_clause = [x["sortColumn"] for x in res["orderBy"]]
    ascorder_clause = [int(x["isAscending"]) for x in res["orderBy"]]
    hint_clause = res["hint"]
    exec_flag = res["exec"]
    if exec_flag:
        raise ValueError("sql must not use EXEC clause.")

    return MetaSQL(
        select_clause,
        from_clause,
        where=where_clause,
        groupBy=groupby_clause,
        groupFlag=groupflag_clause,
        csort=csort_clause,
        ascSort=ascsort_clause,
        having=having_clause,
        orderBy=orderby_clause,
        ascOrder=ascorder_clause,
        hint=hint_clause
    )


def _check_1_0(val):
    if val == 0:
        return "false"
    else:
        return "true"


class MetaSQL:
    def __init__(
        self,
        select: Union[List[str], str],
        table: str,
        where: Union[List[str], str, None] = None,
        groupBy: Union[List[str], str, None] = None,
        groupFlag: Union[int, GROUP_FLAG, None] = None,
        csort: Union[List[str], str, None] = None,
        ascSort: Union[int, SORT_TYPE, None] = None,
        having: Union[List[str], str, None] = None,
        orderBy: Union[List[str], str, None] = None,
        ascOrder: Union[int, SORT_TYPE, None] = None,
        limit: Optional[int] = None,
        hint: Optional[HINT_TYPE] = None,
    ):
        self.select = select
        self.table = table
        self.where = where
        self.groupby = groupBy
        self.groupflag = groupFlag
        self.csort = csort
        self.ascsort = ascSort
        self.having = having
        self.orderby = orderBy
        self.ascorder = ascOrder
        self.limit = limit
        self.hint = hint

    def __return_attr(self, name):
        if hasattr(self, f"_{name}"):
            val = self.__getattribute__(f"_{name}")
            if isinstance(val, list):
                if len(val) == 0:
                    return ""
                res_list = [str(_) for _ in val]
                return f"[{','.join(res_list)}]"
            return val
        return ""

    @property
    def select(self):
        return self.__return_attr("select")

    @select.setter
    def select(self, value: Union[List[str], str]):
        if isinstance(value, str):
            self._select = [value]
        elif isinstance(value, list):
            self._select = [str(_) if _ != "< * >" else 'sqlCol("*")' for _ in value]
        else:
            raise TypeError("select must be str or List[str].")

    @property
    def table(self):
        return self.__return_attr("table")

    @table.setter
    def table(self, value: str):
        if isinstance(value, str):
            self._table = value
        else:
            raise TypeError("table must be str.")

    @property
    def where(self):
        return self.__return_attr("where")

    @where.setter
    def where(self, value: Union[List[str], str, None] = None):
        if value is None:
            self._where = []
        elif isinstance(value, str):
            self._where = [value]
        elif isinstance(value, list):
            self._where = [str(_) for _ in value]
        else:
            raise TypeError("where must be List[str], str or None.")

    def add_where(self, values: List[str]):
        self._where = values + self._where

    @property
    def groupby(self):
        return self.__return_attr("groupby")

    @groupby.setter
    def groupby(self, value: Union[List[str], str, None] = None):
        if value is None:
            self._groupby = []
        elif isinstance(value, str):
            self._groupby = [value]
        elif isinstance(value, list):
            self._groupby = [str(_) for _ in value]
        else:
            raise TypeError("groupby must be List[str], str or None.")

    @property
    def groupflag(self):
        return self.__return_attr("groupflag")

    @groupflag.setter
    def groupflag(self, value: Union[int, GROUP_FLAG, None] = None):
        if value is None:
            self._groupflag = GROUP_FLAG.DEFAULT.value
        elif isinstance(value, int):
            self._groupflag = value
        elif isinstance(value, GROUP_FLAG):
            self._groupflag = value.value
        else:
            raise TypeError("groupflag must be GROUP_FLAG, int or None")

    @property
    def csort(self):
        return self.__return_attr("csort")

    @csort.setter
    def csort(self, value: Union[List[str], str, None] = None):
        if value is None:
            self._csort = []
        elif isinstance(value, str):
            self._csort = [value]
        elif isinstance(value, list):
            self._csort = [str(_) for _ in value]
        else:
            raise TypeError("csort must be List[str], str or None.")

    @property
    def ascsort(self):
        return self.__return_attr("ascsort")

    @ascsort.setter
    def ascsort(self, value: Union[List[Union[SORT_TYPE, int]], SORT_TYPE, int, None] = None):
        if value is None:
            self._ascsort = []
        elif isinstance(value, SORT_TYPE):
            self._ascsort = [_check_1_0(int(value.value))]
        elif isinstance(value, int):
            self._ascsort = [_check_1_0(value)]
        elif isinstance(value, list):
            self._ascsort = [_check_1_0(int(_.value)) if isinstance(_, SORT_TYPE) else _check_1_0(_) for _ in value]
        else:
            raise TypeError("ascsort must be List[SORT_TYPE|int], SORT_TYPE, int or None.")

    @property
    def having(self):
        return self.__return_attr("having")

    @having.setter
    def having(self, value: Union[List[str], str, None] = None):
        if value is None:
            self._having = []
        elif isinstance(value, str):
            self._having = [value]
        elif isinstance(value, list):
            self._having = [_ for _ in value]
        else:
            raise TypeError("having must be List[str], str or None.")

    @property
    def orderby(self):
        return self.__return_attr("orderby")

    @orderby.setter
    def orderby(self, value: Union[List[str], str, None] = None):
        if value is None:
            self._orderby = []
        elif isinstance(value, str):
            self._orderby = [value]
        elif isinstance(value, list):
            self._orderby = [_ for _ in value]
        else:
            raise TypeError("orderby must be List[str], str or None")

    @property
    def ascorder(self):
        return self.__return_attr("ascorder")

    @ascorder.setter
    def ascorder(self, value: Union[List[Union[SORT_TYPE, int]], SORT_TYPE, int, None] = None):
        if value is None:
            self._ascorder = []
        elif isinstance(value, SORT_TYPE):
            self._ascorder = [_check_1_0(int(value.value))]
        elif isinstance(value, int):
            self._ascorder = [_check_1_0(value)]
        elif isinstance(value, list):
            self._ascorder = [_check_1_0(int(_.value)) if isinstance(_, SORT_TYPE) else _check_1_0(_) for _ in value]
        else:
            raise TypeError("ascsort must be List[SORT_TYPE|int], SORT_TYPE, int or None.")

    @property
    def limit(self):
        return self.__return_attr("limit")

    @limit.setter
    def limit(self, value: Optional[int]):
        if value is None:
            self._limit = ""
        elif isinstance(value, int):
            self._limit = value
        else:
            raise TypeError("limit must be int or None.")

    @property
    def hint(self):
        return self.__return_attr("hint")

    @hint.setter
    def hint(self, value: Union[HINT_TYPE, int, None] = None):
        if value is None:
            self._hint = 0
        elif isinstance(value, int):
            self._hint = value
        elif isinstance(value, HINT_TYPE):
            self._hint = value.value
        else:
            raise TypeError("hint must be int or None.")

    def add_hint(self, value: Union[HINT_TYPE, int]):
        if isinstance(value, HINT_TYPE):
            self._hint += value.value
        elif isinstance(value, int):
            self._hint += value
        else:
            raise TypeError("hint must be HINT_TYPE or int.")

    def run(self, ddbSession: Session):
        params = [
            self.select,
            self.table,
            self.where,
            self.groupby,
            str(self.groupflag),
            self.csort,
            self.ascsort,
            self.having,
            self.orderby,
            self.ascorder,
            str(self.limit),
            str(self.hint),
        ]
        params = ",".join([str(_) for _ in params])
        return ddbSession.run(
            f"sql({params})"
        )
