

from typing import IO


class ListProblem:
    __list: IO

    def __init__(self, list):
        self.__list = list
        self.validate()

    def validate(self):
        pass

    def get_list(self):
        return self.__list

    
