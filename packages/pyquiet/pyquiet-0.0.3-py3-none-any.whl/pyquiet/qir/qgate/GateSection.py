from typing import Dict, List
from pyquiet.qir.qgate.gate import QiDefineInfo


class QiGateSection:
    def __init__(self) -> None:
        self.__table: Dict[str, QiDefineInfo] = {}

    def try_emplace(self, qi_define: QiDefineInfo):
        if self.__table.get(qi_define.operation) != None:
            raise ValueError("The QiDefineGate has been already defined.")
        self.__table[qi_define.operation] = qi_define

    def info(self, gate_name: str):
        info = self.__table.get(gate_name)
        if info == None:
            raise ValueError("The quantum gate is not defined yet.")
        return info

    @property
    def gate_names(self) -> List[str]:
        names = [name for name in self.__table.keys()]
        return names

    @property
    def infos(self) -> List[QiDefineInfo]:
        infos = [gate for gate in self.__table.values()]
        return infos

    def __len__(self):
        return len(self.__table)
