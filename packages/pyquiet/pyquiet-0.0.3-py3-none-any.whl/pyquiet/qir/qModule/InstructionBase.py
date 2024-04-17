class InstructionBase:
    def __init__(self, operation:str, label:str = None) -> None:
        self.__operation = operation
        self.label = label
    
    @property
    def opname(self):
        return self.__operation
        
        
