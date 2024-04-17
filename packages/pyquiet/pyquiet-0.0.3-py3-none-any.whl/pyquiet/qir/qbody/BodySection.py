from typing import Dict

from pyquiet.qir.qbody.Function import QiFunction


class QiBodySection:
    def __init__(self) -> None:
        self.__table: Dict[str, QiFunction] = {}
        # The measure operation is pre-defined in quiet-s.
        measure = QiFunction("measure")
        self.try_emplace(measure)

    def try_emplace(self, function: QiFunction):
        if self.__table.get(function.func_name) != None:
            raise ValueError("The Function has been already defined.")
        self.__table[function.func_name] = function

    def get_func(self, func_name: str) -> QiFunction:
        if func_name in self.__table.keys():
            return self.__table[func_name]
        raise ValueError("The Function has not been defined yet.")

    def has_func(self, func_name: str):
        if func_name in self.__table.keys():
            return True
        return False

    @property
    def functions(self):
        return [func for func in self.__table.values()]

    def __len__(self):
        # The measure function is pre-defined in quiet-s and not count it.
        return len(self.__table) - 1
