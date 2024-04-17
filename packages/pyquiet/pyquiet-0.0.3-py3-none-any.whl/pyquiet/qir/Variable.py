from typing import Union
from pyquiet.qir.Type import QuietType


class QiVariable:
    def __init__(self, type: QuietType, var_name: str) -> None:
        self.__var_type = type
        self.__var_name = var_name
        # The variable in QiList is also a QiVariable, but it must be initialized with index.
        self.__index = None

    def __str__(self) -> str:
        if self.__index is None:
            return self.__var_name
        return f"{self.__var_name}[{self.__index}]"

    @property
    def name(self):
        return self.__var_name

    @property
    def type(self):
        return self.__var_type

    @property
    def is_vector(self):
        if self.__index is None:
            return False
        return True

    @property
    def index(self):
        if not self.is_vector:
            raise RuntimeError("Only vector variable has the index.")
        return self.__index

    def set_index(self, index):
        # The index can be assigned only once.
        if self.__index:
            raise ValueError("The index of value can be assigned only once.")
        self.__index = index


class QiList:
    def __init__(self, type: QuietType, var_name: str, length) -> None:
        self.__var_type = type
        self.__var_name = var_name
        # Using 0 to indicate the length of variable is not confirmed.
        self.__size = length

    def __str__(self) -> str:
        return self.__var_name

    def var(self, id):
        # if isinstance(id, int) & id >= self.__size:
        #    raise IndexError("The index of List Variable should less than List size.")
        variable = QiVariable(self.__var_type, self.__var_name)
        variable.set_index(id)
        return variable

    @property
    def size(self):
        return self.__size

    @property
    def name(self):
        return self.__var_name

    @property
    def type(self):
        return self.__var_type


QuietVariable = Union[QiVariable, QiList]
