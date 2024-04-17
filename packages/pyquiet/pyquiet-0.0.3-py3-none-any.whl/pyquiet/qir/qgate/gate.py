import math
from typing import List
from pyquiet.qir.Variable import QuietVariable
from pyquiet.qir.qModule.InstructionBase import InstructionBase
from pyquiet.qir.qModule.ControlWords import ControlWords
from pyquiet.qir.qutils import gen_np_square_matrix


class QiDefineInfo:
    def __init__(self, op_name: str, matrix: list) -> None:
        self.__name = op_name
        # form the matrix
        if int(math.log(len(matrix), 4)) % 1 != 0 & len(matrix) == 0:
            raise ValueError("Matrix size must be 4^n and not be equal to 0.")
        self.__matrix = gen_np_square_matrix(matrix)

    @property
    def operation(self) -> str:
        return self.__name

    @property
    def matrix(self) -> list:
        return self.__matrix

    def __str__(self) -> str:
        return f"{self.__name} {self.__matrix}"


class QiDefineGate(InstructionBase):
    def __init__(self, qi_define: QiDefineInfo, label: str = None) -> None:
        super().__init__(qi_define.operation, label)
        self.__matrix = qi_define.matrix
        # check the operands and store them
        self.__qubits: List[QuietVariable] = None
        # control words.
        self.__ctrl: ControlWords = None

    def operands(self, operands: List[QuietVariable]):
        qubits_num = math.log(len(self.__matrix), 2)
        if len(operands) != qubits_num:
            raise ValueError(
                "The number of operands must be equal to log4 of matrix size."
            )
        self.__qubits = operands

    @property
    def qubits(self):
        return self.__qubits

    @property
    def matrix(self):
        return self.__matrix

    def set_ctrl(self, c_word: ControlWords) -> None:
        self.__ctrl = c_word

    @property
    def ctrl_word(self) -> ControlWords:
        if self.__ctrl is None:
            raise ValueError("The instruction has not inited by control word yet.")
        return self.__ctrl

    def __str__(self) -> str:
        qubits = ",".join(str(qubit) for qubit in self.__qubits)
        return f"{self.opname} {qubits}"
