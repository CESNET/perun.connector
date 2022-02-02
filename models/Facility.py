from models import HasIdInterface


class Facility(HasIdInterface):
    def __init__(self, id, name, description, entity_id):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__entity_id = entity_id

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_entity_id(self) -> str:
        return self.__entity_id

