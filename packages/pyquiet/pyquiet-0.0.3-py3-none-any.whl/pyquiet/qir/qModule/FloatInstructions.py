from pyquiet.qir.qModule.ClassicalInsnBase import (
    InstructionBase,
    ArithmeticOpBase,
    QuietVariable,
)
from typing import Union


###########################################
#       Data Transfer Instructions        #
###########################################
class Ldd(InstructionBase):
    def __init__(
        self, d_operand: QuietVariable, s_operand: float, label: str = None
    ) -> None:
        super().__init__("ldd", label)
        self.__d_operand = d_operand
        self.__s_operand = s_operand

    def __str__(self):
        return f"{super().__str__()} {self.__d_operand}, {self.__s_operand}"

    @property
    def imm(self):
        return self.__s_operand

    @property
    def dst(self) -> QuietVariable:
        return self.__d_operand


class Movd(InstructionBase):
    def __init__(
        self, d_operand: QuietVariable, s_operand: QuietVariable, label: str = None
    ):
        super().__init__("movd", label)
        self.__d_operand = d_operand
        self.__s_operand = s_operand

    def __str__(self):
        return f"{super().__str__()} {self.__d_operand}, {self.__s_operand}"

    @property
    def src(self) -> QuietVariable:
        return self.__s_operand

    @property
    def dst(self) -> QuietVariable:
        return self.__d_operand


###########################################
#         Arithmetic Instructions         #
###########################################
class Addd(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("addd", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Subd(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("subd", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Muld(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("muld", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Divd(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("divd", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Adddi(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: float,
        label: str = None,
    ) -> None:
        super().__init__("adddi", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Subdi(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: float,
        label: str = None,
    ) -> None:
        super().__init__("subdi", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Muldi(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: float,
        label: str = None,
    ) -> None:
        super().__init__("muldi", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Divdi(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: float,
        label: str = None,
    ) -> None:
        super().__init__("divdi", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


QuietFmInstruction = Union[
    Ldd, Movd, Addd, Subd, Muld, Divd, Adddi, Subdi, Muldi, Divdi
]
