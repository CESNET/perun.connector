from models import HasIdInterface


class Member(HasIdInterface):
    def __init__(self, id, vo_id, status):
        self.VALID = 'VALID'
        self.INVALID = 'INVALID'
        self.EXPIRED = 'EXPIRED'
        self.SUSPENDED = 'SUSPENDED'
        self.DISABLED = 'DISABLED'
        self.__id = id
        self.__vo_id = vo_id
        self.__status = status

    def get_id(self) -> int:
        return self.__id

    def get_vo_id(self) -> int:
        return self.__vo_id

    def get_status(self) -> str:
        return self.__status
