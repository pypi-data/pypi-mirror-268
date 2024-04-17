from typing import List
from pyquiet.qir.Variable import QiVariable

###########################################
#        About Control Key Words.         #
###########################################


class ControlWords:
    def __init__(self) -> None:
        self.__ctrl = False
        # the control qubit is only one qubit.
        self.__qubits: List[QiVariable] = None

    def set_ctrl(self) -> None:
        self.__ctrl = True

    @property
    def ctrl(self) -> bool:
        return self.__ctrl

    def set_qubits(self, qubits: List[QiVariable]) -> None:
        self.__qubits = qubits

    @property
    def ctrl_qubits(self) -> List[QiVariable]:
        return self.__qubits
