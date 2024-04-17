from pathlib import Path

class QiFile:
    def __init__(self, file:Path) -> None:
        # check the file whther exists first.
        if not file.exists():
            raise FileNotFoundError("The file does not exist.")
        # check the file format whether is .qi
        if not file.suffix == ".qi":
            raise ValueError("File name must end with .qi")
        self.handle = file.absolute()
        self.file_name = self.handle.name
    
    def __str__(self):
        op_name = "include"
        return f"{op_name} {self.file_name}"