from models import HasIdInterface


class User(HasIdInterface):
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name
