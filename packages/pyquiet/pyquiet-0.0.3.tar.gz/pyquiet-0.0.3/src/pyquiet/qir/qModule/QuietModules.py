from typing import Union
from pyquiet.qir.qModule.StdInstructions import *
from pyquiet.qir.qModule.IntInstruction import *
from pyquiet.qir.qModule.FloatInstructions import *


class Module:
    def __init__(self, name, instructions):
        self.__module_name: str = name
        self.__module_instructions: list = instructions

    @property
    def module_name(self):
        return self.__module_name

    @property
    def instructions_name(self):
        return [instr for instr in self.__module_instructions]


class StdModule(Module):
    def __init__(self):
        module_name = "std"
        module_instructions = [
            "H",
            "X",
            "Y",
            "Z",
            "S",
            "T",
            "Sdag",
            "Tdag",
            "Rx",
            "Ry",
            "Rz",
            "Rxy",
            "CNOT",
            "CZ",
            "SWAP",
            "CP",
            "CRz",
            "U4",
        ]
        super().__init__(module_name, module_instructions)


class IntModule(Module):
    def __init__(self):
        module_name = "im"
        module_instructions = [
            "jump",
            "ld",
            "mov",
            "lnot",
            "land",
            "lor",
            "lxor",
            "add",
            "sub",
            "mul",
            "div",
            "addi",
            "subi",
            "muli",
            "divi",
            "bne",
            "beq",
            "bgt",
            "bge",
            "blt",
            "ble",
        ]
        super().__init__(module_name, module_instructions)


class FloatModule(Module):
    def __init__(self):
        module_name = "fm"
        module_instructions = [
            "ldd",
            "movd",
            "addd",
            "subd",
            "muld",
            "divd",
            "adddi",
            "subdi",
            "muldi",
            "divdi",
        ]
        super().__init__(module_name, module_instructions)


QuietModule = Union[StdModule, IntModule, FloatModule]
std = StdModule()
