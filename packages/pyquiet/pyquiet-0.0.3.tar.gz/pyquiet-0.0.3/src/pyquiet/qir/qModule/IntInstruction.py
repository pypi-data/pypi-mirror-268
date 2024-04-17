from typing import Union
from pyquiet.qir.Variable import QiVariable, QuietVariable
from pyquiet.qir.qModule.InstructionBase import InstructionBase
from pyquiet.qir.qModule.ClassicalInsnBase import ArithmeticOpBase, BranchOpBase


###########################################
#       Data Transfer Instructions        #
###########################################
class Ld(InstructionBase):
    def __init__(
        self, d_operand: QuietVariable, s_operand: int, label: str = None
    ) -> None:
        super().__init__("ld", label)
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


class Mov(InstructionBase):
    def __init__(
        self, d_operand: QuietVariable, s_operand: QuietVariable, label: str = None
    ):
        super().__init__("mov", label)
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
#            Logic Instructions           #
###########################################
class Lnot(InstructionBase):
    def __init__(
        self, d_operand: QiVariable, s_operand: QiVariable, label: str = None
    ) -> None:
        super().__init__("lnot", label)
        self.__dst_operand = d_operand
        self.__src_operand = s_operand

    def __str__(self):
        return f"{self.opname} {self.__dst_operand}, {self.__dst_operand}"

    @property
    def src(self) -> QuietVariable:
        return self.__src_operand

    @property
    def dst(self) -> QuietVariable:
        return self.__dst_operand


class Land(InstructionBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("land", label)
        self.__dst_operand = d_operand
        self.__src_operand1 = s_operand1
        self.__src_operand2 = s_operand2

    def __str__(self):
        return f"{self.opname} {self.__dst_operand}, {self.__src_operand1}, {self.__src_operand2}"

    @property
    def src1(self) -> QuietVariable:
        return self.__src_operand1

    @property
    def src2(self) -> QuietVariable:
        return self.__src_operand2

    @property
    def dst(self) -> QuietVariable:
        return self.__dst_operand


class Lor(InstructionBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("lor", label)
        self.__dst_operand = d_operand
        self.__src_operand1 = s_operand1
        self.__src_operand2 = s_operand2

    def __str__(self):
        return f"{self.opname} {self.__dst_operand}, {self.__src_operand1}, {self.__src_operand2}"

    @property
    def src1(self) -> QuietVariable:
        return self.__src_operand1

    @property
    def src2(self) -> QuietVariable:
        return self.__src_operand2

    @property
    def dst(self) -> QuietVariable:
        return self.__dst_operand


class Lxor(InstructionBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("lxor", label)
        self.__dst_operand = d_operand
        self.__src_operand1 = s_operand1
        self.__src_operand2 = s_operand2

    def __str__(self):
        return f"{self.opname} {self.__dst_operand}, {self.__src_operand1}, {self.__src_operand2}"

    @property
    def src1(self) -> QuietVariable:
        return self.__src_operand1

    @property
    def src2(self) -> QuietVariable:
        return self.__src_operand2

    @property
    def dst(self) -> QuietVariable:
        return self.__dst_operand


###########################################
#         Arithmetic Instructions         #
###########################################


class Add(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("add", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Sub(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("sub", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Mul(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("mul", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Div(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__("div", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Addi(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: int,
        label: str = None,
    ) -> None:
        super().__init__("addi", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Subi(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: int,
        label: str = None,
    ) -> None:
        super().__init__("subi", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Muli(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: int,
        label: str = None,
    ) -> None:
        super().__init__("muli", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


class Divi(ArithmeticOpBase):
    def __init__(
        self,
        d_operand: QuietVariable,
        s_operand1: QuietVariable,
        s_operand2: int,
        label: str = None,
    ) -> None:
        super().__init__("divi", d_operand, s_operand1, s_operand2, label)

    def __str__(self):
        return super().__str__()


###########################################
#       Branch and Jump Instruction       #
###########################################


class Jump(InstructionBase):
    def __init__(self, dest_operand_label: str, insn_label: str = None) -> None:
        super().__init__("jump", insn_label)
        self.__label = dest_operand_label

    def __str__(self):
        return f"{super().__str__()} {self.__label}"

    @property
    def destination_label(self) -> str:
        return self.__label


class Bne(BranchOpBase):
    def __init__(
        self,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        d_operand: str,
        label: str = None,
    ) -> None:
        super().__init__("bne", s_operand1, s_operand2, d_operand, label)

    def __str__(self):
        return super().__str__()


class Beq(BranchOpBase):
    def __init__(
        self,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        d_operand: str,
        label: str = None,
    ) -> None:
        super().__init__("beq", s_operand1, s_operand2, d_operand, label)

    def __str__(self):
        return super().__str__()


class Bgt(BranchOpBase):
    def __init__(
        self,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        d_operand: str,
        label: str = None,
    ) -> None:
        super().__init__("bgt", s_operand1, s_operand2, d_operand, label)

    def __str__(self):
        return super().__str__()


class Bge(BranchOpBase):
    def __init__(
        self,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        d_operand: str,
        label: str = None,
    ) -> None:
        super().__init__("bge", s_operand1, s_operand2, d_operand, label)

    def __str__(self):
        return super().__str__()


class Blt(BranchOpBase):
    def __init__(
        self,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        d_operand: str,
        label: str = None,
    ) -> None:
        super().__init__("blt", s_operand1, s_operand2, d_operand, label)

    def __str__(self):
        return super().__str__()


class Ble(BranchOpBase):
    def __init__(
        self,
        s_operand1: QuietVariable,
        s_operand2: QuietVariable,
        d_operand: str,
        label: str = None,
    ) -> None:
        super().__init__("ble", s_operand1, s_operand2, d_operand, label)

    def __str__(self):
        return super().__str__()


QuietImInstruction = Union[
    Jump,
    Ld,
    Mov,
    Lnot,
    Land,
    Lor,
    Lxor,
    Add,
    Sub,
    Mul,
    Div,
    Addi,
    Subi,
    Muli,
    Divi,
    Bne,
    Beq,
    Bgt,
    Bge,
    Blt,
    Ble,
]
