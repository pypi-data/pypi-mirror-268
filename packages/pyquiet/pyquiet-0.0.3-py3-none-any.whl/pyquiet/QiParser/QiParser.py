from typing import List
from pathlib import Path
from antlr4 import InputStream, CommonTokenStream
from pyquiet.antlr import QuietLexer, QuietParser
from pyquiet.QiVisitor.QuietVisitor import QuietVisitor
from pyquiet.qir import QiProgram, FunctionCall
from pyquiet.qir.qfile import QiFile, QiFileSection


def ensure_path(fn) -> Path:
    assert isinstance(fn, (str, Path))
    if isinstance(fn, str):
        fn = Path(fn).resolve()
    return fn


class QiParser:
    def __init__(self) -> None:
        # There are several QiPrograms per parsing.
        self.__programs: List[QiProgram] = []
        self.__final_prog: QiProgram = None
        self.__input_files: List[InputStream] = []
        self.__qi_path: Path = None

    def handle_parser(self, filepath: str):
        self.__qi_path = ensure_path(filepath)
        self.__final_prog = self.parse(self.__qi_path)

    def parse(self, filename: Path):
        """Here is the parse func using the quiet-parser lib. You can parse qifile
        into QiProgram.

        Args:
            filename (Path): The Path of input *.qi file.

        Returns:
            QiProgram: The QiProgram will store all data of *.qi file.
        """
        with filename.open("r") as f:
            input = f.read()
        input2 = InputStream(input)
        self.__input_files.append(input2)
        lexer = QuietLexer(input2)
        tokens = CommonTokenStream(lexer)

        # get the CST.
        parser = QuietParser(tokens)
        quiet_cst = parser.prog()

        # convert the CST into QiProg
        visitor = QuietVisitor(qi_path=filename.parent)
        prog: QiProgram = visitor.visit(quiet_cst)

        # add the define_gate and include_file in .file and .gate section.
        qifile: QiFileSection = prog.file_section
        for i in qifile.file_name_list():
            file: QiFile = qifile.get_file(i)
            program_inc: QiProgram = self.parse(file.handle)
            for gate in program_inc.gate_section.infos:
                prog.add_define_gate(gate)
            for func in program_inc.body_section.functions:
                if not prog.body_section.has_func(func.func_name):
                    prog.add_define_function(func)

        # bind the function for FunctionCall instructions.
        for func in prog.body_section.functions:
            for instr in func.body:
                if isinstance(instr, FunctionCall):
                    instr.bind_function(prog.body_section.get_func(instr.opname))
        self.__programs.append(prog)
        return prog

    @property
    def prog(self):
        return self.__final_prog
