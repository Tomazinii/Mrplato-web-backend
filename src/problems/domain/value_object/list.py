from typing import IO, List
from src._shared.errors.bad_request import BadRequestError

from src.problems.domain.value_object.file import File


class ListProblem:
    __list: List[str]

    def __init__(self, list: File):
        self.validate(list)


    def validate(self, list: File):

        allowed_extensions = {".txt", ".arg"}
        if not (list.get_name().endswith(tuple(
            allowed_extensions
        ))):
            raise BadRequestError("Requires .txt or .arg file; other type not is supported.")
        lines_limit = 150
        array = [line.strip() for line in list.get_file().readlines()]

        print("QWEQWEQWEWQEWQEWQEWQEWEQ", array)
        print("QWEQWEQWEWQEWQEWQEWQEWEQ", array)
        print("QWEQWEQWEWQEWQEWQEWQEWEQ", array)


        if len(array) > lines_limit:
                raise BadRequestError(f"Only {lines_limit} problems per file are allowed")
        
        self.__list = array

    def get_list(self):
        return self.__list

        


