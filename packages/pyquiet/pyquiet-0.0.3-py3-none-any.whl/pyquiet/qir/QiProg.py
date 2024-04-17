from typing import List
from pyquiet.qir.qModule.QuietModules import QuietModule, std
from pyquiet.qir.qbody import QiBodySection, QiFunction
from pyquiet.qir.qfile import QiFileSection, QiFile
from pyquiet.qir.qgate import QiGateSection, QiDefineInfo


class QiProgram:
    """
       QiProgram is the intermediate representation of a `qi` file.
    It can be transformed from a quiet AST(CST), and extract the more essential information.

    A Quiet program is composed of four sections:
    * Modules Section: Load different instruction modules to limit the module instruction set.
    * File Section: Include other `qi` files.
    * Gate Section: Define the quantum gates in matrix form.
    * Body Section: Describe the program codes with functions.
    """

    def __init__(self, file_name) -> None:
        self.file = file_name
        self.__instr_modules = [std]
        self.__file_section: QiFileSection = QiFileSection()
        self.__gate_section: QiGateSection = QiGateSection()
        # In fact , the gate section is not essential.
        self.__body_section: QiBodySection = QiBodySection()

        self.__main: QiFunction = None

    def load_instr_module(self, instr_module: QuietModule):
        module_names = [module.module_name for module in self.__instr_modules]
        if instr_module.module_name in module_names:
            raise Warning("The Module has already load.")
        else:
            self.__instr_modules.append(instr_module)

    def add_include_file(self, include_instr: QiFile):
        self.__file_section.try_emplace(include_instr)

    def add_define_gate(self, define_instr: QiDefineInfo):
        names = std.instructions_name
        if define_instr.operation in names:
            raise ValueError(
                "The name of quantum gate user defined has been already used in std module."
            )
        # check the name of defined gate whether has already been defined and added to the QiDefineTable.
        self.__gate_section.try_emplace(define_instr)

    def add_define_function(self, define_func: QiFunction):
        # catch the main function.
        self.__body_section.try_emplace(define_func)
        if define_func.func_name == "main":
            self.__main = define_func

    def main_func(self) -> QiFunction:
        if self.__main is None:
            raise ValueError("There is no main function in QiProg.")
        return self.__main

    def supported_instructions(self) -> List[str]:
        # First process the define gate.
        instructions = [info.operation for info in self.__gate_section.infos]
        for module in self.__instr_modules:
            instructions.extend(module.instructions_name)
        return instructions

    @property
    def instr_modules(self):
        return self.__instr_modules

    @property
    def file_section(self):
        return self.__file_section

    @property
    def gate_section(self):
        return self.__gate_section

    @property
    def body_section(self):
        return self.__body_section
