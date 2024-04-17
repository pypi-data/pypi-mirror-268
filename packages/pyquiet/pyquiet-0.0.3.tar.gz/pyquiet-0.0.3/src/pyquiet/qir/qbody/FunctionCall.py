from pyquiet.qir.qModule.InstructionBase import InstructionBase
from pyquiet.qir.qbody.Function import QiFunction


class FunctionCall(InstructionBase):
    def __init__(
        self, func_name: str, inputs: list, outputs: list, label: str = None
    ) -> None:
        super().__init__(func_name, label)
        self.inputs = inputs
        self.outputs = outputs
        self.__func: QiFunction = None

    def __str__(self):
        inputs = ", ".join([str(arg) for arg in self.inputs])
        o_args = ", ".join([str(arg) for arg in self.outputs])
        outputs = f"-> {o_args}"
        if len(self.outputs) == 0:
            outputs = ""

        return f"{self.opname}({inputs}) {outputs}:"

    @property
    def name(self):
        return self.opname

    def bind_function(self, func: QiFunction):
        if self.__func is not None:
            return
            # raise ValueError("The Function has been already binded.")
        self.__func = func

    def to_body(self):
        if self.__func is None:
            raise ValueError("The Function has not been binded yet.")
        return self.__func.body

    def decl_info(self):
        return self.__func.declaration

    def func(self):
        return self.__func
