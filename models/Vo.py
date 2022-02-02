from models import HasIdInterface


class Vo(HasIdInterface):
    def __init__(self, id, name, short_name):
        self.__id = id
        self.__name = name
        self.__short_name = short_name

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_short_name(self) -> str:
        return self.__short_name
