from __future__ import annotations
from pyquiet.qir.qModule.InstructionBase import InstructionBase
from pyquiet.qir.Variable import QuietVariable


class ArithmeticOpBase(InstructionBase):
    def __init__(
        self,
        operation: str,
        dst_operand: QuietVariable,
        src_operand1: QuietVariable,
        src_operand2: QuietVariable | int | float,
        label: str = None,
    ) -> None:
        super().__init__(operation, label)
        self.__d_operand = dst_operand
        self.__s_operand1 = src_operand1
        self.__s_operand2 = src_operand2

    @property
    def src1(self) -> QuietVariable:
        return self.__s_operand1

    @property
    def src2(self):
        return self.__s_operand2

    @property
    def dst(self) -> QuietVariable:
        return self.__d_operand

    def __str__(self) -> str:
        return f"{self.opname} {self.__d_operand}, {self.__s_operand1}, {self.__s_operand2}"


class BranchOpBase(InstructionBase):
    def __init__(
        self,
        operation: str,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        dst_label: str,
        label: str = None,
    ) -> None:
        super().__init__(operation, label)

        self.__src_operand1 = s_operand1
        self.__src_operand2 = s_operand2
        self.__dst_label = dst_label

    @property
    def src1(self) -> QuietVariable:
        return self.__src_operand1

    @property
    def src2(self) -> QuietVariable:
        return self.__src_operand2

    @property
    def dst_label(self) -> str:
        return self.__dst_label

    def __str__(self) -> str:
        return f"{self.opname} {self.__src_operand1}, {self.__src_operand2}, {self.__dst_label}"
