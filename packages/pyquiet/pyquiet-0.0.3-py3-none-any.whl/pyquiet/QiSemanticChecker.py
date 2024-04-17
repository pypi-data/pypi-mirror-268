import numpy as np
from pyquiet.qir.qbody.VariableDecl import VariableDecl
from typing import Union

from pyquiet.qir import (
    FunctionCall,
    QiDefineGate,
    QiVariable,
    QiList,
    DoubleType,
    IntType,
    QubitType,
    QiProgram,
)
from pyquiet.qir.qbody import QiFunction
from pyquiet.qir.qModule.ClassicalInsnBase import ArithmeticOpBase, BranchOpBase
from pyquiet.qir.qModule.FloatInstructions import Ldd, Movd, QuietFmInstruction
from pyquiet.qir.qModule.IntInstruction import (
    Land,
    Ld,
    Lnot,
    Lor,
    Lxor,
    Mov,
    QuietImInstruction,
)
from pyquiet.qir.qModule.StdInstructions import (
    Std1QRotationGate,
    Std2QRotationGate,
    StdSingleQubitGate,
    StdTwoQubitGate,
)


def check_type(var, types):
    try:
        if isinstance(var, types):
            return True
        else:
            return False
    except:
        if hasattr(types, "__origin__") and types.__origin__ == Union:
            for t in types.__args__:
                if isinstance(var, t):
                    return True
    return False


class QiSemanticChecker:
    def __init__(self, checking_prog: QiProgram = None) -> None:
        self.__prog: QiProgram = checking_prog

    def __qubit_var_check(self, qubit, insn, func: QiFunction):
        if not isinstance(qubit, QiVariable):
            raise SyntaxError(
                f"{insn} ==> The variable of Quantum Gate must be a QiVariable"
            )
        if not isinstance(qubit.type, QubitType):
            raise SyntaxError(
                f"{insn} ==> The variable of Quantum Gate must be a Qubit Type variable."
            )
        qi_var = func.var_list().get_variable(qubit.name)
        if qubit.is_vector and isinstance(qi_var, QiVariable):
            raise SyntaxError(
                f"{insn} ==> The variable {qubit.name} is not a QiList, but user add the index."
            )

    def __qubit_type_check(self, qubit, insn, func):
        if not isinstance(qubit.type, QubitType):
            raise SyntaxError(
                f"{insn} ==> The variable of Quantum Gate must be a Qubit Type variable."
            )
        if isinstance(qubit, QiVariable):
            qi_var = func.var_list().get_variable(qubit.name)
            if qubit.is_vector and isinstance(qi_var, QiVariable):
                raise SyntaxError(
                    f"{insn} ==> The variable {qubit.name} is not a QiList, but user add the index."
                )

    def __rotation_param_check(self, params, insn, func: QiFunction):
        for param in params:
            if isinstance(param, QiVariable):
                if isinstance(param.type, QubitType):
                    raise SyntaxError(
                        f"{insn} ==> The param variable must be a Int or Double type."
                    )
                param_var = func.var_list().get_variable(param.name)
                if param.is_vector and isinstance(param_var, QiVariable):
                    raise SyntaxError(
                        f"{insn} ==> The variable {param.name} is not a QiList, but user add the index."
                    )
            elif not (isinstance(param, int) or isinstance(param, float)):
                raise SyntaxError(
                    f"{insn} ==> The param value must be a Int or Double type."
                )
            else:
                raise SyntaxError(
                    f"{insn} ==> The param variable must QiVariable or int / float value."
                )

    def __integer_insn_variable_type_check(
        self, var: QiVariable, insn, func: QiFunction
    ):
        if not isinstance(var, QiVariable):
            raise SyntaxError(
                f"{insn} ==> The variable of Integer instruction must be a QiVariable"
            )
        if not isinstance(var.type, IntType):
            raise SyntaxError(
                f"{insn} ==> The variable of Integer instruction must be a Int Type variable."
            )
        param_var = func.var_list().get_variable(var.name)
        if var.is_vector and isinstance(param_var, QiVariable):
            raise SyntaxError(
                f"{insn} ==> The variable {var.name} is not a QiList, but user add the index."
            )

    def __float_insn_variable_type_check(self, var: QiVariable, insn, func: QiFunction):
        if not isinstance(var, QiVariable):
            raise SyntaxError(
                f"{insn} ==> The variable of float instruction must be a QiVariable"
            )
        if not isinstance(var.type, DoubleType):
            raise SyntaxError(
                f"{insn} ==> The variable of Float instruction must be a Double Type variable."
            )
        param_var = func.var_list().get_variable(var.name)
        if var.is_vector and isinstance(param_var, QiVariable):
            raise SyntaxError(
                f"{insn} ==> The variable {var.name} is not a QiList, but user add the index."
            )

    def check_defined_gate_matrix(self):
        gates = self.__prog.gate_section.infos
        for gate in gates:
            if np.log(np.size(gate.matrix)) / np.log(4) % 1 != 0:
                raise SyntaxError(f"{gate} -->  The matrix size must be 4^n.")

    def check_include_files_suffix(self):
        files = self.__prog.file_section.file_name_list()
        for file in files:
            if not file.endswith(".qi"):
                raise SyntaxError(f"{file} --> The file suffix must be .qi.")

    def check_module_insn_supported(self, insn):
        if insn.opname not in self.__prog.supported_instructions():
            raise SyntaxError(
                f"{insn} --> The instruction is not supported.Please using appropriate modules."
            )

    def check_quantum_insn_variable_type(self, insn, func):
        # The type of quantum insn variable must be QiVariable.
        if isinstance(insn, QiDefineGate):
            if len(insn.qubits) == 1:
                self.__qubit_type_check(insn.qubits[0], insn, func)
            else:
                for qubit in insn.qubits:
                    self.__qubit_var_check(qubit, insn, func)
        elif isinstance(insn, (StdSingleQubitGate, StdTwoQubitGate)):
            if isinstance(insn, StdSingleQubitGate):
                self.__qubit_type_check(insn.qubit, insn, func)
            elif isinstance(insn, StdTwoQubitGate):
                self.__qubit_var_check(insn.c_qubit, insn, func)
                self.__qubit_var_check(insn.t_qubit, insn, func)

    def check_quantum_insn_params_type(self, insn, func):
        if isinstance(insn, Std1QRotationGate):
            self.__rotation_param_check(insn.angle, insn, func)
        elif isinstance(insn, Std2QRotationGate):
            self.__rotation_param_check(insn.angle, insn, func)

    def check_integer_insn_variable_type(self, insn, func):
        if check_type(insn, QuietImInstruction):
            if isinstance(insn, Ld):
                self.__integer_insn_variable_type_check(insn.dst, insn, func)
            elif isinstance(insn, Mov):
                self.__integer_insn_variable_type_check(insn.dst, insn, func)
                self.__integer_insn_variable_type_check(insn.src, insn, func)
            elif (
                isinstance(insn, Land)
                or isinstance(insn, Lor)
                or isinstance(insn, Lxor)
            ):
                self.__integer_insn_variable_type_check(insn.dst, insn, func)
                self.__integer_insn_variable_type_check(insn.src1, insn, func)
                self.__integer_insn_variable_type_check(insn.src2, insn, func)
            elif isinstance(insn, Lnot):
                self.__integer_insn_variable_type_check(insn.dst, insn, func)
                self.__integer_insn_variable_type_check(insn.src, insn, func)
            elif isinstance(insn, ArithmeticOpBase):
                self.__integer_insn_variable_type_check(insn.dst, insn, func)
                self.__integer_insn_variable_type_check(insn.src1, insn, func)
                if isinstance(insn.src2, QiVariable):
                    self.__integer_insn_variable_type_check(insn.src2, insn, func)
            elif isinstance(insn, BranchOpBase):
                self.__integer_insn_variable_type_check(insn.src1, insn, func)
                self.__integer_insn_variable_type_check(insn.src2, insn, func)

    def check_float_insn_variable_type(self, insn, func):
        if check_type(insn, QuietFmInstruction):
            if isinstance(insn, Ldd):
                self.__float_insn_variable_type_check(insn.dst, insn, func)
            elif isinstance(insn, Movd):
                self.__float_insn_variable_type_check(insn.dst, insn, func)
                self.__float_insn_variable_type_check(insn.src, insn, func)
            elif isinstance(insn, ArithmeticOpBase):
                self.__float_insn_variable_type_check(insn.dst, insn, func)
                self.__float_insn_variable_type_check(insn.src1, insn, func)
                if isinstance(insn.src2, QiVariable):
                    self.__float_insn_variable_type_check(insn.src2, insn, func)

    def check_function_call_params(self, insn):
        # check the inputs list and outputs list size.
        if isinstance(insn, FunctionCall):
            if insn.opname != "measure":
                if len(insn.inputs) != len(insn.func().get_input_args()):
                    raise SyntaxError(
                        f"{insn} --> The num of input args used in FunctionCall is not equal to declaration."
                    )
                # check the each args type in inputs list.
                # There exits two case of func_call input args.
                for i in range(len(insn.inputs)):
                    # * 1. if the inputs of function call is a number value.
                    if isinstance(insn.inputs[i], int):
                        if not isinstance(
                            insn.func().get_input_args()[i].type, IntType
                        ):
                            raise SyntaxError(
                                f"{insn} --> The type of input args used in FunctionCall is not equal to declaration."
                            )
                    elif isinstance(insn.inputs[i], float):
                        if not isinstance(
                            insn.func().get_input_args()[i].type, DoubleType
                        ):
                            raise SyntaxError(
                                f"{insn} --> The type of input args used in FunctionCall is not equal to declaration."
                            )
                    # * 2. if the inputs of function call is a variable.
                    elif isinstance(insn.inputs[i], QiVariable):
                        if type(insn.inputs[i].type) != type(
                            insn.func().get_input_args()[i].type
                        ):
                            raise SyntaxError(
                                f"{insn} --> The type of input args used in FunctionCall is not equal to declaration."
                            )
                    elif isinstance(insn.inputs[i], QiList):
                        if not isinstance(insn.func().get_input_args()[i].var, QiList):
                            raise SyntaxError(
                                f"{insn} --> The type of input args used in FunctionCall is not equal to declaration."
                            )
                        if type(insn.inputs[i].type) != type(
                            insn.func().get_input_args()[i].type
                        ):
                            raise SyntaxError(
                                f"{insn} --> The type of input args used in FunctionCall is not equal to declaration."
                            )
                    else:
                        raise SyntaxError(
                            f"{insn} --> The input args of FunctionCall is not a number value or variable."
                        )
                # check the each args type in outputs list.
                if len(insn.outputs) != len(insn.func().get_output_args()):
                    raise SyntaxError(
                        f"{insn} --> The num of output args used in FunctionCall is not equal to declaration."
                    )
                # The type of output args must be variable.
                for i in range(len(insn.outputs)):
                    if isinstance(insn.outputs[i], QiVariable):
                        if type(insn.outputs[i].type) != type(
                            insn.func().get_output_args()[i].type
                        ):
                            raise SyntaxError(
                                f"{insn} --> The type of output args used in FunctionCall is not equal to declaration."
                            )
                    elif isinstance(insn.outputs[i], QiList):
                        if type(insn.outputs[i].type) != type(
                            insn.func().get_output_args()[i].type
                        ):
                            raise SyntaxError(
                                f"{insn} --> The type of output args used in FunctionCall is not equal to declaration."
                            )
                    else:
                        raise SyntaxError(
                            f"{insn} --> The output args of FunctionCall is not a variable."
                        )
            else:
                if len(insn.inputs) != 1:
                    raise SyntaxError(
                        f"{insn} --> The num of input args used in FunctionCall is not equal to declaration."
                    )
                if not isinstance(insn.inputs[0], (QiVariable, QiList)):
                    raise SyntaxError(
                        f"{insn} --> The input args of FunctionCall is not a variable."
                    )
                if not isinstance(insn.inputs[0].type, QubitType):
                    raise SyntaxError(
                        f"{insn} --> The input args of FunctionCall is not a Qubit Type variable."
                    )
                if len(insn.outputs) != 1:
                    raise SyntaxError(
                        f"{insn} --> The num of output args used in FunctionCall is not equal to declaration."
                    )
                if not isinstance(insn.outputs[0], (QiVariable, QiList)):
                    raise SyntaxError(
                        f"{insn} --> The output args of FunctionCall is not a variable."
                    )
                if isinstance(insn.inputs[0], QiList) and isinstance(
                    insn.outputs[0], QiList
                ):
                    if (
                        isinstance(insn.inputs[0].size, int)
                        and isinstance(insn.outputs[0].size, int)
                        and insn.inputs[0].size != insn.outputs[0].size
                    ):
                        raise SyntaxError(
                            f"{insn} --> The size of input args and output args used in FunctionCall is not equal."
                        )

    def check_semantic(self, prog: QiProgram):
        # * 0. set the program.
        self.__prog = prog

        # * 1. check the include files.
        self.check_include_files_suffix()

        # * 2. check the gate defined matrix.
        self.check_defined_gate_matrix()

        # * 3. check the all instructions
        for func in self.__prog.body_section.functions:
            for insn in func.body:
                # * 3.0 check the module insn supported.
                if isinstance(insn, FunctionCall):
                    if not self.__prog.body_section.has_func(insn.opname):
                        raise SyntaxError(
                            f"{insn} --> The function call is not defined in the program."
                        )
                elif isinstance(insn, VariableDecl):
                    ## 讨论1
                    continue
                else:
                    ## indluding std and define gate
                    self.check_module_insn_supported(insn)

                # * 3.1 check the variable type of quantum insn.
                self.check_quantum_insn_variable_type(insn, func)

                # * 3.2 check the params type of quantum insn.
                self.check_quantum_insn_params_type(insn, func)

                # * 3.3 check the variable type of integer module insn.
                self.check_integer_insn_variable_type(insn, func)

                # * 3.4 check the variable type of double module insn.
                self.check_float_insn_variable_type(insn, func)

                # * 3.5 check the params of function call.
                self.check_function_call_params(insn)
