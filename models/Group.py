from models import HasIdInterface


class Group(HasIdInterface):
    def __init__(self, id, vo_id, uuid, name, unique_name, description):
        self.__id = id
        self.__vo_id = vo_id
        self.__uuid = uuid
        self.__name = name
        self.__unique_name = unique_name
        self.__description = description

    def get_id(self) -> int:
        return self.__id

    def get_vo_id(self) -> int:
        return self.__vo_id

    def get_uuid(self) -> str:
        return self.__uuid

    def get_name(self) -> str:
        return self.__name

    def get_unique_name(self) -> str:
        return self.__unique_name

    def get_description(self) -> str:
        return self.__description
