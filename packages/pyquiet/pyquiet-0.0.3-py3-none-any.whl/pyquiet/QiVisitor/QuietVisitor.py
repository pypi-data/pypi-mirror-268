import numpy
from pathlib import Path

from pyquiet.antlr.QuietParserVisitor import QuietParserVisitor
from pyquiet.antlr.QuietParser import QuietParser
from pyquiet.qir.Type import QubitType, IntType, DoubleType
from pyquiet.qir.Variable import QiList, QiVariable
from pyquiet.qir.qModule.ControlWords import ControlWords
from pyquiet.qir.qModule.QuietModules import FloatModule, IntModule
from pyquiet.qir.qModule.FloatInstructions import (
    Adddi,
    Divdi,
    Ldd,
    Movd,
    Addd,
    Muldi,
    Subd,
    Muld,
    Divd,
    Subdi,
)
from pyquiet.qir.qModule.IntInstruction import (
    Mov,
    Ld,
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
    Blt,
    Ble,
    Bgt,
    Bge,
    Jump,
)
from pyquiet.qir.qModule.StdInstructions import (
    Sdag,
    T,
    Tdag,
    S,
    X,
    Y,
    Z,
    H,
    CNOT,
    CZ,
    SWAP,
    U4,
    Rx,
    Ry,
    Rz,
    Rxy,
    CP,
    CRz,
)
from pyquiet.qir.qbody import QiFunction, VariableDecl, FunctionCall
from pyquiet.qir.QiProg import QiProgram

from pyquiet.qir.qfile.file import QiFile
from pyquiet.qir.qgate.gate import QiDefineGate, QiDefineInfo


class QuietVisitor(QuietParserVisitor):
    def __init__(self, file_name: str = "default", qi_path: Path = Path().cwd()):
        super().__init__()
        self.__prog = QiProgram(file_name)
        self.__qi_path = qi_path
        self.__current_function: QiFunction = None

    # Visit a parse tree produced by QuietParser#prog.
    def visitProg(self, ctx: QuietParser.ProgContext):
        self.visitChildren(ctx)
        return self.__prog

        # Visit a parse tree produced by QuietParser#usingModules.

    def visitUsingModules(self, ctx: QuietParser.UsingModulesContext):
        if ctx is None:
            return None
        modulenames = ctx.Id()
        for i in range(len(modulenames)):
            assert modulenames[i].getText() in [
                "im",
                "fm",
                "std",
            ], "QUIET-s do not has this module"
            if modulenames[i].getText() == "im":
                module = IntModule()
            elif modulenames[i].getText() == "fm":
                module = FloatModule()
            elif modulenames[i].getText() == "std":
                continue
            self.__prog.load_instr_module(module)

    # Visit a parse tree produced by QuietParser#fileSecContent.
    def visitFileSecContent(self, ctx: QuietParser.FileSecContentContext):
        if ctx is None:
            return None
        for inc_ctx in ctx.includeStatement():
            self.__prog.add_include_file(self.visitIncludeStatement(inc_ctx))

    # Visit a parse tree produced by QuietParser#includeStatement.
    def visitIncludeStatement(self, ctx: QuietParser.IncludeStatementContext):
        if ctx is None:
            raise ValueError("The include statement is None.")
        name = self.visitFilename(ctx.filename())
        # using the default qi file path to construct the path object.
        file = self.__qi_path / name
        return QiFile(file)

    # Visit a parse tree produced by QuietParser#filename.
    def visitFilename(self, ctx: QuietParser.FilenameContext):
        if ctx is None:
            raise ValueError("The filename is None.")
        id = ctx.Id()
        dot = ctx.Dot()
        ret = id[0].getText()
        if dot is not None:
            for i in range(len(dot)):
                ret += dot[i].getText() + id[i + 1].getText()
        return ret

    # Visit a parse tree produced by QuietParser#gateSecContent.
    def visitGateSecContent(self, ctx: QuietParser.GateSecContentContext):
        if ctx is None:
            return None
        for def_ctx in ctx.gateDefinition():
            self.__prog.add_define_gate(self.visitGateDefinition(def_ctx))

    # Visit a parse tree produced by QuietParser#gateDefinition.
    def visitGateDefinition(self, ctx: QuietParser.GateDefinitionContext):
        if ctx is None:
            raise ValueError("The gate definition is None.")
        name = ctx.Id().getText()
        matrix = self.visitNumberArray(ctx.numberArray())
        define_gate = QiDefineInfo(name, matrix)
        return define_gate

    # Visit a parse tree produced by QuietParser#numberArray.
    def visitNumberArray(self, ctx: QuietParser.NumberArrayContext):
        if ctx is None:
            raise ValueError("The number array is None.")
        matrix = self.visitNumberList(ctx.numberList())
        return matrix

    # Visit a parse tree produced by QuietParser#numberList.
    def visitNumberList(self, ctx: QuietParser.NumberListContext):
        if ctx is None:
            raise ValueError("The number list is None.")
        numlist = []
        for num_ctx in ctx.number():
            numlist.append(self.visitNumber(num_ctx))
        return numlist

    # Visit a parse tree produced by QuietParser#bodySecContent.
    def visitBodySecContent(self, ctx: QuietParser.BodySecContentContext):
        if ctx is None:
            return None
        for func in ctx.function():
            self.__prog.add_define_function(self.visitFunction(func))

        # bind the function with the function call.
        ## bind the function after the include file is obtain
        # for func in self.__prog.body_section.functions:
        #     for instr in func.body:
        #         if isinstance(instr, FunctionCall):
        #             instr.bind_function(self.__prog.body_section.get_func(instr.opname))

    def visitFunction(self, ctx: QuietParser.FunctionContext):
        if ctx is None:
            raise ValueError("The function is None.")
        # init a new qi function object.
        self.__current_function = QiFunction()
        self.visitFuncHeader(ctx.funcHeader())
        self.visitFuncBody(ctx.funcBody())
        return self.__current_function

    def visitFuncHeader(self, ctx: QuietParser.FuncHeaderContext):
        if ctx is None:
            raise ValueError("The function header is None.")
        # set the function name.
        func_name = ctx.Id().getText()
        self.__current_function.func_name = func_name

        # init the input_args and output_args.
        self.__current_function.init_input_args(self.visitInputArgs(ctx.inputArgs()))
        self.__current_function.init_output_args(self.visitOutputArgs(ctx.outputArgs()))

    # Visit a parse tree produced by QuietParser#formalArgs.
    def visitInputArgs(self, ctx: QuietParser.InputArgsContext):
        inpurArgs = []
        if ctx is None:
            return None
        else:
            params = ctx.formalParam()
            for formalParam in params:
                param = self.visitFormalParam(formalParam)
                inpurArgs.append(param)
        return inpurArgs

    def visitOutputArgs(self, ctx: QuietParser.OutputArgsContext):
        outputArgs = []
        if ctx is None:
            return None
        else:
            params = ctx.formalParam()
            for formalParam in params:
                param = self.visitFormalParam(formalParam)
                outputArgs.append(param)
        return outputArgs

    # Visit a parse tree produced by QuietParser#formalParam.
    def visitFormalParam(self, ctx: QuietParser.FormalParamContext):
        if ctx is None:
            raise ValueError("The formal param is None.")
        else:
            var_name = str(ctx.Id().getText())
            qi_params = self.visitParamType(ctx.paramType())

            # check the variable type
            if str(qi_params[0]) == "qubit":
                var_type = QubitType()
            elif str(qi_params[0]) == "int":
                var_type = IntType()
            elif str(qi_params[0]) == "double":
                var_type = DoubleType()
            else:
                raise SyntaxError("The type of variable is not defined yet.")

            # check the variable is a QiVariable or QiList
            if qi_params[1] == -1:
                # It indicates that the variable type is no-list type.
                qi_var = QiVariable(var_type, var_name)
            else:
                qi_var = QiList(var_type, var_name, int(qi_params[1]))

            var_decl = VariableDecl(var_type, qi_var)
        return var_decl

    # Visit a parse tree produced by QuietParser#funcBody.
    def visitFuncBody(self, ctx: QuietParser.FuncBodyContext):
        # funcbody = self.visitActions(ctx.actions())
        if ctx is None:
            raise ValueError("The function body is None.")
        for act_ins in ctx.action():
            self.visitAction(act_ins)

    # Visit a parse tree produced by QuietParser#actions.
    def visitAction(self, ctx: QuietParser.ActionContext):
        if ctx is None:
            return None
        label = self.visitLabel(ctx.label())
        ins = self.visitInstruction(ctx.instruction())
        if isinstance(ins, list):
            # variable declaration
            # The label will point to the first instruction in the list.
            ins[0].label = label
            for insn in ins:
                self.__current_function.push_instr(insn)
        elif ins is not None:
            ins.label = label
            self.__current_function.push_instr(ins)

    # Visit a parse tree produced by QuietParser#label.
    def visitLabel(self, ctx: QuietParser.LabelContext):
        if ctx is None:
            return None
        else:
            label = ctx.Id().getText()
            return label

    # Visit a parse tree produced by QuietParser#instruction.
    def visitInstruction(self, ctx: QuietParser.InstructionContext):
        if ctx is None:
            raise ValueError("The instruction is None.")
        if ctx.quantumOpInsn() is not None:
            ins = self.visitQuantumOpInsn(ctx.quantumOpInsn())
        elif ctx.funcCall() is not None:
            ins = self.visitFuncCall(ctx.funcCall())
        elif ctx.variableDecl() is not None:
            ins = self.visitVariableDecl(ctx.variableDecl())
        elif ctx.integerModuleInsn() is not None:
            ins = self.visitIntegerModuleInsn(ctx.integerModuleInsn())
        elif ctx.floatModuleInsn() is not None:
            ins = self.visitFloatModuleInsn(ctx.floatModuleInsn())
        elif ctx.EOL() is not None:
            return None
        else:
            raise ValueError("The instruction type is not supported yet.")
        return ins

    # Visit a parse tree produced by QuietParser#returnStmt.
    def visitReturnStmt(self, ctx: QuietParser.ReturnStmtContext):
        if ctx is None:
            return None
        return self.visitChildren(ctx)

    def visitControlQubit(self, ctx: QuietParser.ControlQubitContext):
        if ctx is None:
            raise ValueError(
                "The control qubit is not defined, but the control words is set."
            )
        ctx_vars = ctx.variable()
        qubits = []
        for var in ctx_vars:
            qubit = self.visitVariable(var)
            if not isinstance(qubit, QiVariable):
                raise ValueError("The control qubit must be a QiVariable.")
            qubits.append(qubit)
        return qubits

    def visitControlModifier(self, ctx: QuietParser.ControlModifierContext):
        c_word = ControlWords()
        if ctx is None:
            return c_word
        c_qubits = self.visitControlQubit(ctx.controlQubit())
        c_word.set_ctrl()
        c_word.set_qubits(c_qubits)
        return c_word

    # Visit a parse tree produced by QuietParser#quantumOpInsn.
    def visitQuantumOpInsn(self, ctx: QuietParser.QuantumOpInsnContext):
        if ctx is None:
            raise ValueError("The quantum operation instruction is None.")
        q_gate = self.visitQuantumGate(ctx.quantumGate())

        # generate the control words
        c_word = self.visitControlModifier(ctx.controlModifier())

        # generate the quantum operands.
        varlist = ctx.variable()
        vars = []
        for ctx_var in varlist:
            assert ctx_var is not None
            var = self.visitVariable(ctx_var)
            vars.append(var)
        assert len(vars) > 0

        # extract the params from instructions.
        params = self.visitActualParamList(ctx.actualParamList())
        if isinstance(q_gate, QiDefineGate):
            q_gate.operands(vars)
            q_gate.set_ctrl(c_word)
            return q_gate
        # There are two kinds of quantum operations: 1Q gate and 2Q gate.
        if len(vars) == 1:
            # 1Q gate with param and no param
            if params is None:
                insn = q_gate(vars[0])
                insn.set_ctrl(c_word)
                return insn
            else:
                insn = q_gate(vars[0], params)
                insn.set_ctrl(c_word)
                return insn
        elif len(vars) == 2:
            # 2Q gate with param and no param.
            if params is None:
                insn = q_gate(vars[0], vars[1])
                insn.set_ctrl(c_word)
                return insn
            else:
                insn = q_gate(vars[0], vars[1], params)
                insn.set_ctrl(c_word)
                return insn
        else:
            raise ValueError("The number of quantum operands is not correct.")

    # Visit a parse tree produced by QuietParser#quantumGate.
    def visitQuantumGate(self, ctx: QuietParser.QuantumGateContext):
        if ctx is None:
            raise ValueError("The quantum gate is None.")
        if ctx.gateNoParam() is not None:
            return self.visitGateNoParam(ctx.gateNoParam())
        elif ctx.gateWithParams() is not None:
            return self.visitGateWithParams(ctx.gateWithParams())
        else:
            raise ValueError("The type of gate is not defined yet")

    # Visit a parse tree produced by QuietParser#gateNoParam.
    def visitGateNoParam(self, ctx: QuietParser.GateNoParamContext):
        if ctx is None:
            raise ValueError("The gate without param is None.")
        if ctx.Id() != None:
            # process the case of QiDefineGate
            name = str(ctx.Id().getText())
            return QiDefineGate(self.__prog.gate_section.info(name))
        elif ctx.Hadamard() != None:
            return H
        elif ctx.PauliX() != None:
            return X
        elif ctx.PauliY() != None:
            return Y
        elif ctx.PauliZ() != None:
            return Z
        elif ctx.SGate() != None:
            return S
        elif ctx.Sdag() != None:
            return Sdag
        elif ctx.TGate() != None:
            return T
        elif ctx.Tdg() != None:
            return Tdag
        elif ctx.Cnot() != None:
            return CNOT
        elif ctx.Cz() != None:
            return CZ
        elif ctx.Swap() != None:
            return SWAP
        else:
            raise ValueError("Gate name is not valid")

    # Visit a parse tree produced by QuietParser#actualParamList.
    def visitActualParamList(self, ctx: QuietParser.ActualParamListContext):
        if ctx is None:
            return None
        qi_params = []
        params = ctx.actualParam()
        for param in params:
            qi_params.append(self.visitActualParam(param))
        return qi_params

    # Visit a parse tree produced by QuietParser#actualParam.
    def visitActualParam(self, ctx: QuietParser.ActualParamContext):
        if ctx is None:
            raise ValueError("The actual param is None.")
        if ctx.variable() is not None:
            return self.visitVariable(ctx.variable())
        elif ctx.number() is not None:
            return self.visitNumber(ctx.number())
        else:
            raise ValueError("The actual param can not be parsed.")

    # Visit a parse tree produced by QuietParser#gateWithParams.
    def visitGateWithParams(self, ctx: QuietParser.GateWithParamsContext):
        if ctx is None:
            raise ValueError("The gate with param is None.")
        if ctx.U4() is not None:
            return U4
        elif ctx.Rx() is not None:
            return Rx
        elif ctx.Ry() is not None:
            return Ry
        elif ctx.Rz() is not None:
            return Rz
        elif ctx.Rxy() is not None:
            return Rxy
        elif ctx.CPhase() is not None:
            return CP
        elif ctx.CRz() is not None:
            return CRz
        else:
            raise ValueError("Gate name is not valid")

    # Visit a parse tree produced by QuietParser#number.
    def visitNumber(self, ctx: QuietParser.NumberContext):
        if ctx is None:
            raise ValueError("The number is None.")
        if ctx.IntLiteral() is not None:
            num = int(ctx.IntLiteral().getText())
        elif ctx.DoubleLiteral() is not None:
            if ctx.DoubleLiteral().getText() == "pi":
                num = numpy.pi
            else:
                num = float(ctx.DoubleLiteral().getText())
        elif ctx.complexLiteral() is not None:
            num = self.visitComplexLiteral(ctx.complexLiteral())
        return num

    def visitComplexLiteral(self, ctx: QuietParser.ComplexLiteralContext):
        if ctx is None:
            raise ValueError("The complex literal is None.")
        real = self.visitRealPart(ctx.realPart())
        im = self.visitImaginaryPart(ctx.imaginaryPart())
        return complex(real, im)

    def visitRealPart(self, ctx: QuietParser.RealPartContext):
        if ctx is None:
            raise ValueError("The real part is None.")
        if ctx.IntLiteral() is not None:
            real = int(ctx.IntLiteral().getText())
        else:
            real = float(ctx.DoubleLiteral().getText())
        return real

    def visitImaginaryPart(self, ctx: QuietParser.ImaginaryPartContext):
        if ctx is None:
            raise ValueError("The imaginary part is None.")
        if ctx.IntLiteral() is not None:
            im = int(ctx.IntLiteral().getText())
        else:
            im = float(ctx.DoubleLiteral().getText())
        return im

    # Visit a parse tree produced by QuietParser#paramType.
    def visitParamType(self, ctx: QuietParser.ParamTypeContext):
        if ctx is None:
            raise ValueError("The param has no type declaration.")
        if ctx.typeAtomic() is not None:
            qi_types = self.visitTypeAtomic(ctx.typeAtomic())
        elif ctx.typeArrayNoLength() is not None:
            qi_types = self.visitTypeArrayNoLength(ctx.typeArrayNoLength())
        elif ctx.typeArrayWithLength() is not None:
            qi_types = self.visitTypeArrayWithLength(ctx.typeArrayWithLength())
        else:
            raise SyntaxError("The type is not defined yet.")

        return qi_types

    # Visit a parse tree produced by QuietParser#typeAtomic.
    def visitTypeAtomic(self, ctx: QuietParser.TypeAtomicContext):
        if ctx is None:
            raise ValueError("The type is None.")
        if ctx.Qubit() is not None:
            typeAtomic = QubitType()
        elif ctx.Int() is not None:
            typeAtomic = IntType()
        else:
            typeAtomic = DoubleType()
        return typeAtomic, -1

    # Visit a parse tree produced by QuietParser#typeArrayNoLength.
    def visitTypeArrayNoLength(self, ctx: QuietParser.TypeArrayNoLengthContext):
        if ctx is None:
            raise ValueError("The type is None.")
        typeNoLen = self.visitTypeAtomic(ctx.typeAtomic())[0]
        num = 0
        return typeNoLen, num

    # Visit a parse tree produced by QuietParser#typeArrayWithLength.
    def visitTypeArrayWithLength(self, ctx: QuietParser.TypeArrayWithLengthContext):
        if ctx is None:
            raise ValueError("The type is None.")
        if ctx.Id():
            assert len(ctx.Id()) != 0
            num = str(ctx.Id()[0].getText())
        elif ctx.IntLiteral():
            assert len(ctx.IntLiteral()) != 0
            num = int(ctx.IntLiteral()[0].getText())
        else:
            raise ValueError(
                "The type with array length must have a number or variable."
            )
        typeWithLen = self.visitTypeAtomic(ctx.typeAtomic())[0]
        return typeWithLen, num

    # Visit a parse tree produced by QuietParser#variableDecl.
    def visitVariableDecl(self, ctx: QuietParser.VariableDeclContext):
        if ctx is None:
            raise ValueError("The variable declaration is None.")
        var_type = self.visitParamType(ctx.paramType())[0]
        param = self.visitParamType(ctx.paramType())[1]
        var_list = ctx.Id()
        assert len(var_list) >= 1

        # generate the VariableDecl list.
        var_decl_list = []
        if param == -1:
            for var_name in var_list:
                qi_var = QiVariable(var_type, str(var_name))
                qi_decl = VariableDecl(var_type, qi_var)
                var_decl_list.append(qi_decl)
        else:
            for var_name in var_list:
                qi_var = QiList(var_type, str(var_name), param)
                qi_decl = VariableDecl(var_type, qi_var)
                var_decl_list.append(qi_decl)
        return var_decl_list

    # Visit a parse tree produced by QuietParser#variable.
    def visitVariable(self, ctx: QuietParser.VariableContext):
        if ctx is None:
            raise ValueError("The variable is None.")
        ids = ctx.Id()
        var_name = ids[0].getText()  # get the variable from the defined variables list.
        qi_var = self.__current_function.var_list().get_variable(str(var_name))

        # we need a more detailed sematic check,
        # the decalred variable and the used variable may be different.
        if isinstance(qi_var, QiList):
            if len(ids) == 2:
                # it is a QiList Variable.
                param = str(ids[1].getText())
            elif len(ids) == 1:
                # If the IntLiteral is None, it indicates that the variable is a whole QiList.
                # ? we should check the instr whether support vector operation or not.
                param = None
                if ctx.IntLiteral():
                    param = int(ctx.IntLiteral().getText())
            else:
                # len(ids) == 0 case means it is not a variable. We don't need care about that.
                raise ValueError(
                    "We do not support the multi-index form of variable yet."
                )

            # if the param is None, it indicates that the variable is a whole QiList.
            if param is not None:
                qi_var = qi_var.var(param)
        else:
            if ctx.BracketLeft() and ctx.BracketRight():
                qi_var = QiVariable(qi_var.type, qi_var.name)
                if len(ids) == 2:
                    # it is a QiList Variable.
                    param = str(ids[1].getText())
                elif len(ids) == 1:
                    # If the IntLiteral is None, it indicates that the variable is a whole QiList.
                    # ? we should check the instr whether support vector operation or not.
                    param = None
                    if ctx.IntLiteral():
                        param = int(ctx.IntLiteral().getText())
                else:
                    # len(ids) == 0 case means it is not a variable. We don't need care about that.
                    raise ValueError(
                        "We do not support the multi-index form of variable yet."
                    )

                # if the param is None, it indicates that the variable is a whole QiList.
                if param is not None:
                    qi_var.set_index(param)
                # raise SyntaxError(
                #     "The variable {var} is not a QiList, but user add the idex.".format(
                #         var=var_name
                #     )
                # )
        return qi_var

    # Visit a parse tree produced by QuietParser#funcCall.
    def visitFuncCall(self, ctx: QuietParser.FuncCallContext):
        if ctx is None:
            raise ValueError("The function call is described not correctly.")
        if ctx.controlModifier() is not None:
            raise SyntaxError("The control modifier is not supported yet.")
        if ctx.Id() is None:
            name = ctx.Measure().getText()
        else:
            name = ctx.Id().getText()

        inputs = self.visitActualParamList(ctx.actualParamList())
        if inputs is None:
            inputs = []
        outputs = []
        for out_var in ctx.variable():
            output = self.visitVariable(out_var)
            outputs.append(output)
        # bind the function object to the func call object.
        return FunctionCall(name, inputs, outputs)

    # integer module instruction visitor
    # Visit a parse tree produced by QuietParser#integerModuleInsn.
    def visitIntegerModuleInsn(self, ctx: QuietParser.IntegerModuleInsnContext):
        if ctx is None:
            raise ValueError(
                "The integer module instruction is None but arrived at the visitor node."
            )
        # There is four types of integer module instructions.
        if ctx.imDataTransferInsn() is not None:
            insn = self.visitImDataTransferInsn(ctx.imDataTransferInsn())
        elif ctx.logicInsn() is not None:
            insn = self.visitLogicInsn(ctx.logicInsn())
        elif ctx.imArithmeticInsn() is not None:
            insn = self.visitImArithmeticInsn(ctx.imArithmeticInsn())
        elif ctx.jumpInsn() is not None:
            insn = self.visitJumpInsn(ctx.jumpInsn())
        else:
            raise SyntaxError(
                f"{ctx.getText()} --> The type of integer module instruction is not supported yet."
            )
        return insn

    # Visit a parse tree produced by QuietParser#imDataTransferInsn.
    def visitImDataTransferInsn(self, ctx: QuietParser.ImDataTransferInsnContext):
        if ctx is None:
            raise ValueError(
                "The integer module data transfer instruction is None but arrived at the visitor node."
            )
        # There is two types of integer module data transfer instructions.
        # * 1. mov instruction
        if self.visitImDTOp(ctx.imDTOp()) == "mov":
            # check the operand number and kind.
            if len(ctx.variable()) != 2:
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of mov instruction must be two variables."
                )
            var_list = []
            for variable in ctx.variable():
                var_list.append(self.visitVariable(variable))

            # generate the mov instruction.
            insn = Mov(var_list[0], var_list[1])
        # * 1. ld instruction
        elif self.visitImDTOp(ctx.imDTOp()) == "ld":
            # check the operand number and kind.
            if len(ctx.variable()) != 1 or ctx.number() is None:
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of ld instruction must be one variable and a int number."
                )
            # check the number is a int number.
            num = self.visitNumber(ctx.number())
            if not isinstance(num, int):
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of ld instruction must be a int number."
                )
            insn = Ld(self.visitVariable(ctx.variable()[0]), num)
        else:
            raise NotImplementedError(
                f"{ctx.getText()} --> The type of integer module data transfer instruction is not supported yet."
            )
        return insn

    def visitImDTOp(self, ctx: QuietParser.ImDTOpContext):
        if ctx is None:
            raise ValueError(
                "The integer module data transfer instruction operand is None but arrived at the visitor node."
            )
        return str(ctx.getText()).lower()

    # Visit a parse tree produced by QuietParser#logicInsn.
    def visitLogicInsn(self, ctx: QuietParser.LogicInsnContext):
        if ctx is None:
            raise ValueError(
                "The integer module logic instruction is None but arrived at the visitor node."
            )
        # There exists four logic instructions.
        var_list = []
        for variable in ctx.variable():
            var_list.append(self.visitVariable(variable))
        op_name = self.visitImLogicOp(ctx.imLogicOp())
        if op_name == "lnot":
            if len(var_list) != 2:
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of lnot instruction must be two variables."
                )
            insn = Lnot(var_list[0], var_list[1])
        else:
            if len(ctx.variable()) != 3:
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of land instruction must be three variables."
                )
            if op_name == "land":
                insn = Land(var_list[0], var_list[1], var_list[2])
            elif op_name == "lor":
                insn = Lor(var_list[0], var_list[1], var_list[2])
            else:
                insn = Lxor(var_list[0], var_list[1], var_list[2])
        return insn

    def visitImLogicOp(self, ctx: QuietParser.ImLogicOpContext):
        if ctx is None:
            raise ValueError(
                "The integer module logic instruction operand is None but arrived at the visitor node."
            )
        return str(ctx.getText()).lower()

    # Visit a parse tree produced by QuietParser#imArithmeticInsn.
    def visitImArithmeticInsn(self, ctx: QuietParser.ImArithmeticInsnContext):
        if ctx is None:
            raise ValueError(
                "The integer module arithmetic instruction is None but arrived at the visitor node."
            )
        # There exists Two kinds of arithmetic instructions.
        # * 1. imArithVarInsn
        if ctx.imArithVarInsn() is not None:
            insn = self.visitImArithVarInsn(ctx.imArithVarInsn())
        else:
            insn = self.visitImArithImmInsn(ctx.imArithImmInsn())
        return insn

    # Visit a parse tree produced by QuietParser#imArithVarInsn.
    def visitImArithVarInsn(self, ctx: QuietParser.ImArithVarInsnContext):
        if ctx is None:
            raise ValueError(
                "The integer module arithmetic instruction with variable is None but arrived at the visitor node."
            )
        # There exists four arithmetic variable instructions.
        # process the variable first.
        var_list = []
        for var in ctx.variable():
            var_list.append(self.visitVariable(var))
        if len(var_list) != 3:
            raise SyntaxError(
                f"{ctx.getText()} --> The operand of arithmetic instruction must be three variables."
            )
        gate_name = self.visitImArithVarOp(ctx.imArithVarOp())
        if gate_name == "add":
            insn = Add(var_list[0], var_list[1], var_list[2])
        elif gate_name == "sub":
            insn = Sub(var_list[0], var_list[1], var_list[2])
        elif gate_name == "mul":
            insn = Mul(var_list[0], var_list[1], var_list[2])
        else:
            insn = Div(var_list[0], var_list[1], var_list[2])
        return insn

    def visitImArithVarOp(self, ctx: QuietParser.ImArithVarOpContext):
        if ctx is None:
            raise ValueError(
                "The integer module arithmetic instruction operand is None but arrived at the visitor node."
            )
        return str(ctx.getText()).lower()

    # Visit a parse tree produced by QuietParser#imArithImmInsn.
    def visitImArithImmInsn(self, ctx: QuietParser.ImArithImmInsnContext):
        if ctx is None:
            raise ValueError(
                "The integer module arithmetic instruction with immediate is None but arrived at the visitor node."
            )
        # There exists four arithmetic immediate instructions.
        # process the variable first.
        var_list = []
        for var in ctx.variable():
            var_list.append(self.visitVariable(var))
        if len(var_list) != 2:
            raise SyntaxError(
                f"{ctx.getText()} --> The operand of arithmetic instruction must be two variables."
            )
        if ctx.number() is None:
            raise SyntaxError(
                f"{ctx.getText()} --> The final operand of arithmetic instruction must be a number."
            )
        num = self.visitNumber(ctx.number())
        if not isinstance(num, int):
            raise SyntaxError(
                f"{ctx.getText()} --> The final operand of arithmetic instruction must be a int number."
            )
        gate_name = self.visitImArithImmOp(ctx.imArithImmOp())
        if gate_name == "addi":
            insn = Addi(var_list[0], var_list[1], num)
        elif gate_name == "subi":
            insn = Subi(var_list[0], var_list[1], num)
        elif gate_name == "muli":
            insn = Muli(var_list[0], var_list[1], num)
        else:
            insn = Divi(var_list[0], var_list[1], num)
        return insn

    def visitImArithImmOp(self, ctx: QuietParser.ImArithImmOpContext):
        if ctx is None:
            raise ValueError(
                "The integer module arithmetic instruction operand is None but arrived at the visitor node."
            )
        return str(ctx.getText()).lower()

    # Visit a parse tree produced by QuietParser#jumpInsn.
    def visitJumpInsn(self, ctx: QuietParser.JumpInsnContext):
        if ctx is None:
            raise ValueError(
                "The jump instruction is None but arrived at the visitor node."
            )
        # There exists two kinds of jump instructions.
        # process the variable first.
        dst_label = str(self.visitLabel(ctx.label()))
        gate_name = self.visitJumpOp(ctx.jumpOp())
        if gate_name == "jump":
            if len(ctx.variable()) != 0:
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of jump instruction must be zero variable."
                )
            insn = Jump(dst_label)
        else:
            if len(ctx.variable()) != 2:
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of jump instruction must be two variable."
                )
            var_list = []
            for var in ctx.variable():
                var_list.append(self.visitVariable(var))
            if gate_name == "bne":
                insn = Bne(var_list[0], var_list[1], dst_label)
            elif gate_name == "beq":
                insn = Beq(var_list[0], var_list[1], dst_label)
            elif gate_name == "blt":
                insn = Blt(var_list[0], var_list[1], dst_label)
            elif gate_name == "ble":
                insn = Ble(var_list[0], var_list[1], dst_label)
            elif gate_name == "bgt":
                insn = Bgt(var_list[0], var_list[1], dst_label)
            else:
                insn = Bge(var_list[0], var_list[1], dst_label)
        return insn

    def visitJumpOp(self, ctx: QuietParser.JumpOpContext):
        if ctx is None:
            raise ValueError(
                "The jump instruction operand is None but arrived at the visitor node."
            )
        return str(ctx.getText()).lower()

    # new visit process of the float module.
    # Visit a parse tree produced by QuietParser#floatModuleInsn.
    def visitFloatModuleInsn(self, ctx: QuietParser.FloatModuleInsnContext):
        if ctx is None:
            raise ValueError(
                "The float module instruction is None but arrived at the visitor node."
            )
        # There is only two kinds of float module instructions.
        if ctx.fmArithmeticInsn() is not None:
            insn = self.visitFmArithmeticInsn(ctx.fmArithmeticInsn())
        elif ctx.fmDataTransferInsn() is not None:
            insn = self.visitFmDataTransferInsn(ctx.fmDataTransferInsn())
        else:
            raise SyntaxError(
                f"{ctx.getText()} --> The float module instruction must be arithmetic or data transfer instruction."
            )
        return insn

    # Visit a parse tree produced by QuietParser#fmDataTransferInsn.
    def visitFmDataTransferInsn(self, ctx: QuietParser.FmDataTransferInsnContext):
        if ctx is None:
            raise ValueError(
                "The float module data transfer instruction is None but arrived at the visitor node."
            )
        # There exists two kinds of float module data transfer instructions.
        var_list = []
        for var in ctx.variable():
            var_list.append(self.visitVariable(var))
        gate_name = self.visitFmDTOp(ctx.fmDTOp())
        if gate_name == "movd":
            if len(ctx.variable()) != 2:
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of movd instruction must be two variables."
                )
            insn = Movd(var_list[0], var_list[1])
        else:
            if len(ctx.variable()) != 1 or ctx.number() is None:
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of ldd instruction must be one variable and a float number."
                )
            num = self.visitNumber(ctx.number())
            if not isinstance(num, (int, float)):
                raise SyntaxError(
                    f"{ctx.getText()} --> The operand of ldd instruction must be a float or int number."
                )
            insn = Ldd(var_list[0], num)
        return insn

    def visitFmDTOp(self, ctx: QuietParser.FmDTOpContext):
        if ctx is None:
            raise ValueError(
                "The float module data transfer instruction operand is None but arrived at the visitor node."
            )
        return str(ctx.getText()).lower()

    # Visit a parse tree produced by QuietParser#fmArithmeticInsn.
    def visitFmArithmeticInsn(self, ctx: QuietParser.FmArithmeticInsnContext):
        if ctx is None:
            raise ValueError(
                "The float module arithmetic instruction is None but arrived at the visitor node."
            )
        # There exists two kinds of float module arithmetic instructions.
        if ctx.fmArithImmInsn() is not None:
            insn = self.visitFmArithImmInsn(ctx.fmArithImmInsn())
        else:
            insn = self.visitFmArithVarInsn(ctx.fmArithVarInsn())
        return insn

    # Visit a parse tree produced by QuietParser#fmArithVarInsn.
    def visitFmArithVarInsn(self, ctx: QuietParser.FmArithVarInsnContext):
        if ctx is None:
            raise ValueError(
                "The float module arithmetic instruction with variable is None but arrived at the visitor node."
            )
        # There exists four arithmetic variable instructions.
        if len(ctx.variable()) != 3:
            raise SyntaxError(
                f"{ctx.getText()} --> The operand of arithmetic instruction must be three variables."
            )
        var_list = []
        for var in ctx.variable():
            var_list.append(self.visitVariable(var))
        gate_name = self.visitFmArithVarOp(ctx.fmArithVarOp())
        if gate_name == "addd":
            insn = Addd(var_list[0], var_list[1], var_list[2])
        elif gate_name == "subd":
            insn = Subd(var_list[0], var_list[1], var_list[2])
        elif gate_name == "muld":
            insn = Muld(var_list[0], var_list[1], var_list[2])
        else:
            insn = Divd(var_list[0], var_list[1], var_list[2])
        return insn

    def visitFmArithVarOp(self, ctx: QuietParser.FmArithVarOpContext):
        if ctx is None:
            raise ValueError(
                "The float module arithmetic instruction operand is None but arrived at the visitor node."
            )
        return str(ctx.getText()).lower()

    # Visit a parse tree produced by QuietParser#fmArithImmInsn.
    def visitFmArithImmInsn(self, ctx: QuietParser.FmArithImmInsnContext):
        if ctx is None:
            raise ValueError(
                "The float module arithmetic instruction with immediate is None but arrived at the visitor node."
            )
        # There exists four arithmetic immediate instructions.
        if len(ctx.variable()) != 2:
            raise SyntaxError(
                f"{ctx.getText()} --> The operand of arithmetic instruction must be two variables."
            )
        var_list = []
        for var in ctx.variable():
            var_list.append(self.visitVariable(var))

        # check the number type.
        if ctx.number() is None:
            raise SyntaxError(
                f"{ctx.getText()} --> The operand of arithmetic instruction must be a float number."
            )
        num = self.visitNumber(ctx.number())
        if not isinstance(num, (int, float)):
            raise SyntaxError(
                f"{ctx.getText()} --> The operand of arithmetic instruction must be a int or float number."
            )
        gate_name = self.visitFmArithImmOp(ctx.fmArithImmOp())
        if gate_name == "adddi":
            insn = Adddi(var_list[0], var_list[1], num)
        elif gate_name == "subdi":
            insn = Subdi(var_list[0], var_list[1], num)
        elif gate_name == "muldi":
            insn = Muldi(var_list[0], var_list[1], num)
        else:
            insn = Divdi(var_list[0], var_list[1], num)
        return insn

    def visitFmArithImmOp(self, ctx: QuietParser.FmArithImmOpContext):
        if ctx is None:
            raise ValueError(
                "The float module arithmetic instruction operand is None but arrived at the visitor node."
            )
        return str(ctx.getText()).lower()
