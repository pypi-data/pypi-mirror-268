from typing import Union
import numpy as np
from pyquiet.qir.Variable import QuietVariable
from pyquiet.qir.qModule.InstructionBase import InstructionBase
from pyquiet.qir.qModule.ControlWords import ControlWords


###########################################
#         One Qubit Operations            #
###########################################
class StdSingleQubitGate(InstructionBase):
    def __init__(
        self, operation: str, operand: QuietVariable, label: str = None
    ) -> None:
        super().__init__(operation, label)
        self.__trgt_qubit = operand
        self.__matrix = []
        self.__ctrl: ControlWords = None

    def __str__(self):
        return f"{self.opname} {self.qubit}"

    @property
    def matrix(self):
        if len(self.__matrix) == 0:
            raise ValueError(
                "The matrix of the quantum gate in Std module has not been initialized yet."
            )
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix: np.ndarray):
        self.__matrix = matrix

    def set_ctrl(self, c_word: ControlWords()) -> None:
        self.__ctrl = c_word

    @property
    def ctrl_word(self) -> ControlWords:
        if self.__ctrl is None:
            raise ValueError("The instruction has not inited by control word yet.")
        return self.__ctrl

    @property
    def qubit(self) -> QuietVariable:
        return self.__trgt_qubit


class H(StdSingleQubitGate):
    def __init__(self, operand: QuietVariable, label: str = None) -> None:
        super().__init__("H", operand, label)
        self.matrix = np.array(
            [[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]]
        )

    def __str__(self):
        return super().__str__()


class X(StdSingleQubitGate):
    def __init__(self, operand: QuietVariable, label: str = None) -> None:
        super().__init__("X", operand, label)
        self.matrix = np.array([[0, 1], [1, 0]])

    def __str__(self):
        return super().__str__()


class Y(StdSingleQubitGate):
    def __init__(self, operand: QuietVariable, label: str = None) -> None:
        super().__init__("Y", operand, label)
        self.matrix = np.array([[0, -1j], [1j, 0]])

    def __str__(self):
        return super().__str__()


class Z(StdSingleQubitGate):
    def __init__(self, operand: QuietVariable, label: str = None) -> None:
        super().__init__("Z", operand, label)
        self.matrix = np.array([[1, 0], [0, -1]])

    def __str__(self):
        return super().__str__()


class T(StdSingleQubitGate):
    def __init__(self, operand: QuietVariable, label: str = None) -> None:
        super().__init__("T", operand, label)
        self.matrix = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])

    def __str__(self):
        return super().__str__()


class S(StdSingleQubitGate):
    def __init__(self, operand: QuietVariable, label: str = None) -> None:
        super().__init__("S", operand, label)
        self.matrix = np.array([[1, 0], [0, 1j]])

    def __str__(self):
        return super().__str__()


class Sdag(StdSingleQubitGate):
    def __init__(self, operand: QuietVariable, label: str = None) -> None:
        super().__init__("Sdag", operand, label)
        self.matrix = np.array([[1, 0], [0, 1j]]).T.conjugate()

    def __str__(self):
        return super().__str__()


class Tdag(StdSingleQubitGate):
    def __init__(self, operand: QuietVariable, label: str = None) -> None:
        super().__init__("Tdag", operand, label)
        self.matrix = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]]).T.conjugate()

    def __str__(self):
        return super().__str__()


###########################################
#         Two Qubits Operations           #
###########################################


class StdTwoQubitGate(InstructionBase):
    def __init__(
        self,
        operation: str,
        control_qubit: QuietVariable,
        trgt_qubit: QuietVariable,
        label: str = None,
    ) -> None:
        super().__init__(operation, label)
        self.__control_qubit = control_qubit
        self.__trgt_qubit = trgt_qubit
        self.__matrix = []
        self.__ctrl: ControlWords = None

    def __str__(self):
        return f"{self.opname} {self.c_qubit}, {self.t_qubit}"

    @property
    def c_qubit(self):
        return self.__control_qubit

    @property
    def t_qubit(self):
        return self.__trgt_qubit

    @property
    def matrix(self):
        if len(self.__matrix) == 0:
            raise ValueError(
                "The matrix of the quantum gate in Std module has not been initialized yet."
            )
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix: np.ndarray):
        self.__matrix = matrix

    def set_ctrl(self, c_word: ControlWords) -> None:
        self.__ctrl = c_word

    @property
    def ctrl_word(self) -> ControlWords:
        if self.__ctrl is None:
            raise ValueError("The instruction has not inited by control word yet.")
        return self.__ctrl


class CNOT(StdTwoQubitGate):
    def __init__(
        self, control_qubit: QuietVariable, trgt_qubit: QuietVariable, label: str = None
    ) -> None:
        super().__init__("CNOT", control_qubit, trgt_qubit, label)
        self.matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

    def __str__(self):
        return super().__str__()


class CZ(StdTwoQubitGate):
    def __init__(
        self, control_qubit: QuietVariable, trgt_qubit: QuietVariable, label: str = None
    ) -> None:
        super().__init__("CZ", control_qubit, trgt_qubit, label)
        self.matrix = np.array(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]]
        )

    def __str__(self):
        return super().__str__()


class SWAP(StdTwoQubitGate):
    def __init__(
        self, control_qubit: QuietVariable, trgt_qubit: QuietVariable, label: str = None
    ) -> None:
        super().__init__("SWAP", control_qubit, trgt_qubit, label)
        self.matrix = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])

    def __str__(self):
        return super().__str__()


###########################################
#         1Q Rotation Operations          #
###########################################
class Std1QRotationGate(StdSingleQubitGate):
    def __init__(
        self, operation: str, operand: QuietVariable, args: list, label: str = None
    ) -> None:
        #! the int and double types are not defined yet
        if len(args) == 0:
            raise ValueError("Rotation of 1Q gate must have an angle.")
        super().__init__(operation, operand, label)
        self.__rotations = args

    def __str__(self):
        rotations = ",".join([str(x) for x in self.__rotations])
        return f"{self.opname}({rotations}) {self.qubit}"

    @property
    def angle(self):
        return self.__rotations


class Rx(Std1QRotationGate):
    def __init__(self, operand: QuietVariable, args: list, label: str = None) -> None:
        if len(args) != 1:
            raise ValueError("Rx gate can only have one angle.")
        super().__init__("Rx", operand, args, label)

        """self.matrix = np.array(
            [
                [
                    np.cos(self.angle[0] / 2),
                    -1j * np.sin(self.angle[0] / 2),
                ],
                [
                    -1j * np.sin(self.angle[0] / 2),
                    np.cos(self.angle[0] / 2),
                ],
            ]
        )"""

    def __str__(self):
        return super().__str__()


class Ry(Std1QRotationGate):
    def __init__(self, operand: QuietVariable, args: list, label: str = None) -> None:
        if len(args) != 1:
            raise ValueError("Ry gate can only have one angle.")
        super().__init__("Ry", operand, args, label)
        """self.matrix = np.array(
            [
                [np.cos(self.angle[0] / 2), -np.sin(self.angle[0] / 2)],
                [np.sin(self.angle[0] / 2), np.cos(self.angle[0] / 2)],
            ]
        )"""

    def __str__(self):
        return super().__str__()


class Rz(Std1QRotationGate):
    def __init__(self, operand: QuietVariable, args: list, label: str = None) -> None:
        if len(args) != 1:
            raise ValueError("Rz gate can only have one angle.")
        super().__init__("Rz", operand, args, label)
        """self.matrix = np.array(
            [
                [np.exp(-1j * self.angle[0] / 2), 0],
                [0, np.exp(1j * self.angle[0] / 2)],
            ]
        )"""

    def __str__(self):
        return super().__str__()


class Rxy(Std1QRotationGate):
    def __init__(self, operand: QuietVariable, args: list, label: str = None) -> None:
        if len(args) != 2:
            raise ValueError("Rxy gate can only have two angles.")
        super().__init__("Rxy", operand, args, label)
        """self.matrix = np.array(
            [
                [
                    np.cos(self.angle[0] / 2),
                    -1j * np.exp(-1j * self.angle[1]) * np.sin(self.angle[0] / 2),
                ],
                [
                    -1j * np.exp(1j * self.angle[1]) * np.sin(self.angle[0] / 2),
                    np.cos(self.angle[0] / 2),
                ],
            ]
        )"""

    def __str__(self):
        return super().__str__()


class U4(Std1QRotationGate):
    def __init__(self, operand: QuietVariable, args: list, label: str = None) -> None:
        if len(args) != 4:
            raise ValueError("U4 gate can only have four angles.")
        super().__init__("U4", operand, args, label)
        ### we compute the matrix in the frontend!
        """self.matrix = np.array(
            [
                [
                    np.exp(1j * (self.angle[0] - self.angle[1] / 2 - self.angle[3] / 2))
                    * np.cos(self.angle[2] / 2),
                    -np.exp(
                        1j * (self.angle[0] - self.angle[1] / 2 + self.angle[3] / 2)
                    )
                    * np.sin(self.angle[2] / 2),
                ],
                [
                    np.exp(1j * (self.angle[0] + self.angle[1] / 2 - self.angle[3] / 2))
                    * np.sin(self.angle[2] / 2),
                    np.exp(1j * (self.angle[0] + self.angle[1] / 2 + self.angle[3] / 2))
                    * np.cos(self.angle[2] / 2),
                ],
            ]
        )"""
        """self.matrix = (
            np.exp(1j * self.angle[0])
            * np.array(
                [
                    [np.exp(-1j * self.angle[1] / 2), 0],
                    [0, np.exp(1j * self.angle[1] / 2)],
                ]
            )
            * np.array(
                [
                    [np.cos(self.angle[2] / 2), -np.sin(self.angle[2] / 2)],
                    [np.sin(self.angle[2] / 2), np.cos(self.angle[2] / 2)],
                ]
            )
            * np.array(
                [
                    [np.exp(-1j * self.angle[3] / 2), 0],
                    [0, np.exp(1j * self.angle[3] / 2)],
                ]
            )
        )"""

    def __str__(self):
        return super().__str__()


###########################################
#         2Q Rotation Operations          #
###########################################
class Std2QRotationGate(StdTwoQubitGate):
    def __init__(
        self,
        operation: str,
        control_qubit: QuietVariable,
        trgt_qubit: QuietVariable,
        args: list,
        label: str = None,
    ) -> None:
        super().__init__(operation, control_qubit, trgt_qubit, label)
        self.__rotations = args

    def __str__(self):
        rotations = ",".join([str(x) for x in self.__rotations])
        return f"{self.opname}({rotations}) {self.c_qubit}, {self.t_qubit}"

    @property
    def angle(self):
        return self.__rotations


class CP(Std2QRotationGate):
    def __init__(
        self,
        control_qubit: QuietVariable,
        trgt_qubit: QuietVariable,
        args: list,
        label: str = None,
    ) -> None:
        if len(args) != 1:
            raise ValueError("CP gate can only have one angle.")
        super().__init__("CP", control_qubit, trgt_qubit, args, label)
        """self.matrix = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, np.exp(1j * self.angle[0])],
            ]
        )"""

    def __str__(self):
        return super().__str__()


class CRz(Std2QRotationGate):
    def __init__(
        self,
        control_qubit: QuietVariable,
        trgt_qubit: QuietVariable,
        args: list,
        label: str = None,
    ) -> None:
        if len(args) != 1:
            raise ValueError("CRz gate can only have one angle.")
        super().__init__("CRz", control_qubit, trgt_qubit, args, label)
        """self.matrix = np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, np.exp(-1j * self.angle[0] / 2), 0],
                [0, 0, 0, np.exp(1j * self.angle[0] / 2)],
            ]
        )"""

    def __str__(self):
        return super().__str__()


QuietStdInstruction = Union[
    H, X, Y, Z, S, T, Sdag, Tdag, CNOT, CZ, SWAP, Rx, Ry, Rz, Rxy, U4, CP, CRz
]
