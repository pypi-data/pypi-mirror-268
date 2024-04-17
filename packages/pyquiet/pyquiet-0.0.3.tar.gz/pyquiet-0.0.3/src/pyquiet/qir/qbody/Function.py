from typing import Dict, List

from pyquiet.qir.qbody.VariableDecl import VariableDecl


class QiLabelTable:
    def __init__(self) -> None:
        self.__labels: Dict[str, int] = {}

    def record(self, label: str, order: int):
        if label in self.__labels:
            raise ValueError(
                "The label of instruction in a function body must be unique."
            )
        self.__labels[label] = order

    def index(self, label: str) -> int:
        if self.__labels[label] is None:
            raise ValueError("The label of instruction does not exist.")
        return self.__labels[label]

    def labels(self) -> List[str]:
        return [label for label in self.__labels.keys()]


class FunctionVariables:
    def __init__(self) -> None:
        self.__table: Dict[str, VariableDecl] = {}

    def try_emplace(self, decl: VariableDecl):
        var_name = decl.var.name
        if self.__table.get(var_name) != None:
            raise ValueError("The variable has been already declared.")
        self.__table[var_name] = decl

    def get_variable(self, var_name: str):
        if var_name not in self.__table:
            print("var name is:  ", var_name)
            print(self.__table)
            raise ValueError("The Variable has not been declared yet.")
        return self.__table[var_name].var

    @property
    def table(self):
        return self.__table


class QiFunction:
    """
    The QiFunction is consist of function declaration and function body.
    The QiFunction can be identified by its function name.
        * func name: str

    The function declaration is consist of input args and output args.
        * input args: []
        * output args: []

    The function body is consist of a list of instructions.
        * function body: []
    """

    def __init__(self, name: str = None) -> None:
        # The function name is public element.
        self.func_name: str = name

        # * 1. About Function Declaration
        self.__input_args: List[VariableDecl] = []
        self.__output_args: List[VariableDecl] = []

        # The private elements.
        # * 2. About Function Body
        self.__func_body = []
        self.__label_table = QiLabelTable()
        self.__func_vars = FunctionVariables()

    @property
    def declaration(self) -> str:
        inputs = ", ".join([str(arg) for arg in self.__input_args])
        o_args = ", ".join([str(arg) for arg in self.__output_args])
        outputs = f"-> {o_args}"
        if len(self.__output_args) == 0:
            outputs = ""
        return f"{self.func_name}({inputs}) {outputs}:"

    @property
    def instrs(self) -> str:
        body = ""
        for instr in self.__func_body:
            body = f"{body}\n {instr}"
        return body

    @property
    def body(self):
        return self.__func_body

    def init_input_args(self, args: List[VariableDecl] = None):
        if args is not None:
            for arg in args:
                self.__func_vars.try_emplace(arg)
            self.__input_args = args

    def init_output_args(self, args: List[VariableDecl] = None):
        if args is not None:
            for arg in args:
                self.__func_vars.try_emplace(arg)
            self.__output_args = args

    def get_input_args(self) -> List[VariableDecl]:
        return self.__input_args

    def get_output_args(self) -> List[VariableDecl]:
        return self.__output_args

    def push_instr(self, instr):
        if instr.label is not None:
            index = len(self.__func_body)
            self.__label_table.record(instr.label, index)
        if isinstance(instr, VariableDecl):
            self.__func_vars.try_emplace(instr)
        self.__func_body.append(instr)

    def var_list(self) -> FunctionVariables:
        return self.__func_vars

    def label_table(self) -> QiLabelTable:
        return self.__label_table

    def __str__(self) -> str:
        return f"{self.declaration} \n {self.instrs}"
