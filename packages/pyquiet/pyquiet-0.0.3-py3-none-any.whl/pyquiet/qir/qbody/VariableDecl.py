from pyquiet.qir.Type import QuietType
from pyquiet.qir.Variable import QiList, QuietVariable


class VariableDecl:
    def __init__(self, type: QuietType, var: QuietVariable, label: str = None) -> None:
        self.type = type
        self.var = var
        self.label = label

    def __str__(self) -> str:
        var_type = str(self.type)
        if isinstance(self.var, QiList):
            size = self.var.size
            if size == 0:
                size = ""
            var_type = f"{var_type}[{self.var.size}]"
        var_name = self.var.name
        return f"{var_type} {var_name}"
