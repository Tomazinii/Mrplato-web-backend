from typing import IO, List


class ListProblem:
    __list: List[str]

    def __init__(self, list: IO):
        self.validate(list)


    def validate(self, list):
        allowed_extensions = {".txt", ".arg"}
        if not (hasattr(list, "name") and list.name.endswith(tuple(
            allowed_extensions
        ))):
            raise ValueError("Requires .txt or .arg file; other type not is supported.")
        lines_limit = 150
        array = list.readlines()
        array = [line.strip() for line in array]

        if len(array) > lines_limit:
                raise ValueError(f"Only {lines_limit} problems per file are allowed")
        
        self.__list = array

    def get_list(self):
        return self.__list

        


