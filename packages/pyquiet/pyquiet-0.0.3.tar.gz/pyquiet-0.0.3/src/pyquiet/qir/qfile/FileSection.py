from typing import Dict, List
from pyquiet.qir.qfile.file import QiFile


class QiFileSection:
    def __init__(self) -> None:
        self.__table: Dict[str, QiFile] = {}

    def try_emplace(self, qi_include: QiFile):
        file_name = qi_include.file_name
        if self.__table.get(file_name) != None:
            raise ValueError("The QiFile has been already defined.")
        self.__table[file_name] = qi_include

    def get_file(self, file_name: str):
        file = self.__table.get(file_name)
        if file == None:
            raise ValueError("The file is not included yet.")
        return file

    def delete_file(self, file_name: str):
        if self.__table.get(file_name) == None:
            raise ValueError("The file is not included yet.")
        del self.__table[file_name]

    def included_files(self) -> List[QiFile]:
        files = [file for file in self.__table.values()]
        return files

    def file_name_list(self) -> List[str]:
        files = [file for file in self.__table.keys()]
        return files

    def __len__(self):
        return len(self.__table)
