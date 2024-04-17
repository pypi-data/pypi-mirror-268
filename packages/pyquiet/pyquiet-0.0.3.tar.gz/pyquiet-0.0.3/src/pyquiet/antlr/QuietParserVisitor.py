# Generated from QuietParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .QuietParser import QuietParser
else:
    from QuietParser import QuietParser

# This class defines a complete generic visitor for a parse tree produced by QuietParser.

class QuietParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QuietParser#prog.
    def visitProg(self, ctx:QuietParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#usingModules.
    def visitUsingModules(self, ctx:QuietParser.UsingModulesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fileSection.
    def visitFileSection(self, ctx:QuietParser.FileSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fileSecDecl.
    def visitFileSecDecl(self, ctx:QuietParser.FileSecDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fileSecContent.
    def visitFileSecContent(self, ctx:QuietParser.FileSecContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#includeStatement.
    def visitIncludeStatement(self, ctx:QuietParser.IncludeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#filename.
    def visitFilename(self, ctx:QuietParser.FilenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#gateSection.
    def visitGateSection(self, ctx:QuietParser.GateSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#gateSecDecl.
    def visitGateSecDecl(self, ctx:QuietParser.GateSecDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#gateSecContent.
    def visitGateSecContent(self, ctx:QuietParser.GateSecContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#gateDefinition.
    def visitGateDefinition(self, ctx:QuietParser.GateDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#numberArray.
    def visitNumberArray(self, ctx:QuietParser.NumberArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#numberList.
    def visitNumberList(self, ctx:QuietParser.NumberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#bodySection.
    def visitBodySection(self, ctx:QuietParser.BodySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#bodySecDecl.
    def visitBodySecDecl(self, ctx:QuietParser.BodySecDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#bodySecContent.
    def visitBodySecContent(self, ctx:QuietParser.BodySecContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#function.
    def visitFunction(self, ctx:QuietParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#funcHeader.
    def visitFuncHeader(self, ctx:QuietParser.FuncHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#inputArgs.
    def visitInputArgs(self, ctx:QuietParser.InputArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#outputArgs.
    def visitOutputArgs(self, ctx:QuietParser.OutputArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#formalParam.
    def visitFormalParam(self, ctx:QuietParser.FormalParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#funcBody.
    def visitFuncBody(self, ctx:QuietParser.FuncBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#action.
    def visitAction(self, ctx:QuietParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#label.
    def visitLabel(self, ctx:QuietParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#instruction.
    def visitInstruction(self, ctx:QuietParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#returnStmt.
    def visitReturnStmt(self, ctx:QuietParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#controlQubit.
    def visitControlQubit(self, ctx:QuietParser.ControlQubitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#controlModifier.
    def visitControlModifier(self, ctx:QuietParser.ControlModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#quantumOpInsn.
    def visitQuantumOpInsn(self, ctx:QuietParser.QuantumOpInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#quantumGate.
    def visitQuantumGate(self, ctx:QuietParser.QuantumGateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#gateNoParam.
    def visitGateNoParam(self, ctx:QuietParser.GateNoParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#actualParamList.
    def visitActualParamList(self, ctx:QuietParser.ActualParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#actualParam.
    def visitActualParam(self, ctx:QuietParser.ActualParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#gateWithParams.
    def visitGateWithParams(self, ctx:QuietParser.GateWithParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#complexLiteral.
    def visitComplexLiteral(self, ctx:QuietParser.ComplexLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#realPart.
    def visitRealPart(self, ctx:QuietParser.RealPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imaginaryPart.
    def visitImaginaryPart(self, ctx:QuietParser.ImaginaryPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#number.
    def visitNumber(self, ctx:QuietParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#paramType.
    def visitParamType(self, ctx:QuietParser.ParamTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#typeAtomic.
    def visitTypeAtomic(self, ctx:QuietParser.TypeAtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#typeArrayNoLength.
    def visitTypeArrayNoLength(self, ctx:QuietParser.TypeArrayNoLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#typeArrayWithLength.
    def visitTypeArrayWithLength(self, ctx:QuietParser.TypeArrayWithLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#variableDecl.
    def visitVariableDecl(self, ctx:QuietParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#variable.
    def visitVariable(self, ctx:QuietParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#funcCall.
    def visitFuncCall(self, ctx:QuietParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#integerModuleInsn.
    def visitIntegerModuleInsn(self, ctx:QuietParser.IntegerModuleInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imDataTransferInsn.
    def visitImDataTransferInsn(self, ctx:QuietParser.ImDataTransferInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imDTOp.
    def visitImDTOp(self, ctx:QuietParser.ImDTOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#logicInsn.
    def visitLogicInsn(self, ctx:QuietParser.LogicInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imLogicOp.
    def visitImLogicOp(self, ctx:QuietParser.ImLogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imArithmeticInsn.
    def visitImArithmeticInsn(self, ctx:QuietParser.ImArithmeticInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imArithVarInsn.
    def visitImArithVarInsn(self, ctx:QuietParser.ImArithVarInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imArithVarOp.
    def visitImArithVarOp(self, ctx:QuietParser.ImArithVarOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imArithImmInsn.
    def visitImArithImmInsn(self, ctx:QuietParser.ImArithImmInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#imArithImmOp.
    def visitImArithImmOp(self, ctx:QuietParser.ImArithImmOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#jumpInsn.
    def visitJumpInsn(self, ctx:QuietParser.JumpInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#jumpOp.
    def visitJumpOp(self, ctx:QuietParser.JumpOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#floatModuleInsn.
    def visitFloatModuleInsn(self, ctx:QuietParser.FloatModuleInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fmDataTransferInsn.
    def visitFmDataTransferInsn(self, ctx:QuietParser.FmDataTransferInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fmDTOp.
    def visitFmDTOp(self, ctx:QuietParser.FmDTOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fmArithmeticInsn.
    def visitFmArithmeticInsn(self, ctx:QuietParser.FmArithmeticInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fmArithVarInsn.
    def visitFmArithVarInsn(self, ctx:QuietParser.FmArithVarInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fmArithVarOp.
    def visitFmArithVarOp(self, ctx:QuietParser.FmArithVarOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fmArithImmInsn.
    def visitFmArithImmInsn(self, ctx:QuietParser.FmArithImmInsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuietParser#fmArithImmOp.
    def visitFmArithImmOp(self, ctx:QuietParser.FmArithImmOpContext):
        return self.visitChildren(ctx)



del QuietParser