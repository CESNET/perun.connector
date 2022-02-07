from models import HasIdAbstract


class Member(HasIdAbstract):
    def __init__(self, id, vo_id, status):
        self.VALID = 'VALID'
        self.INVALID = 'INVALID'
        self.EXPIRED = 'EXPIRED'
        self.SUSPENDED = 'SUSPENDED'
        self.DISABLED = 'DISABLED'
        super.__init__(id)
        self.vo_id = vo_id
        self.status = status

    def __str__(self):
        return "id:", self.id, "vo_id: ", self.vo_id, "status: ", self.status

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, value: str):
        match value.casefold():
            case [self.VALID.casefold()]:
                self.status = self.VALID
            case [self.INVALID.casefold()]:
                self.status = self.INVALID
            case [self.EXPIRED.casefold()]:
                self.status = self.EXPIRED
            case [self.SUSPENDED.casefold()]:
                self.status = self.SUSPENDED
            case [self.DISABLED.casefold()]:
                self.status = self.DISABLED
            case _:
                raise ValueError("\"" + value + "\" is not a valid state.")
