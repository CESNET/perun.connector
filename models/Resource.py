from models import HasIdInterface


class Resource(HasIdInterface):
    def __init__(self, id, vo_id, facility_id, name):
        self.__id = id
        self.__vo_id = vo_id
        self.__facility_id = facility_id
        self.__name = name

    def get_id(self) -> int:
        return self.__id

    def get_vo_id(self) -> int:
        return self.__vo_id

    def get_facility_id(self) -> int:
        return self.__facility_id

    def get_name(self) -> str:
        return self.__name
