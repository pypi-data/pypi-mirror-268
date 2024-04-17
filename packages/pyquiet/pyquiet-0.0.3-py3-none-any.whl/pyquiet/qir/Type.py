from typing import Union

class TypeBase:
    def __init__(self, type:str = None) -> None:
        self.type_set = ("int", "double", "qubit")
        self.type = None
        if type in self.type_set:
            self.type = type
    
    def __str__(self) -> str:
        if not self.type:
            raise ValueError("The Type is not support or not defined yet.")
        return self.type
            

class IntType(TypeBase):
    def __init__(self, type = "int") -> None:
        super().__init__(type)
        
    def __str__(self) -> str:
        return super().__str__()
        
class DoubleType(TypeBase):
    def __init__(self, type: str = "double") -> None:
        super().__init__(type)

    def __str__(self) -> str:
        return super().__str__()

class QubitType(TypeBase):
    def __init__(self, type: str = "qubit") -> None:
        super().__init__(type)
    
    def __str__(self) -> str:
        return super().__str__()


QuietType = Union[IntType, DoubleType, QubitType]

        