from models import HasIdAbstract


class Member(HasIdAbstract):
    def __init__(self, id, vo_id, status):
        self.VALID = "VALID"
        self.INVALID = "INVALID"
        self.EXPIRED = "EXPIRED"
        self.SUSPENDED = "SUSPENDED"
        self.DISABLED = "DISABLED"
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
        formatted_value = value.casefold()
        if formatted_value == self.VALID.casefold():
            self.status = self.VALID
        elif formatted_value == self.INVALID.casefold():
            self.status = self.INVALID
        elif formatted_value == self.EXPIRED.casefold():
            self.status = self.EXPIRED
        elif formatted_value == self.SUSPENDED.casefold():
            self.status = self.SUSPENDED
        elif formatted_value == self.DISABLED.casefold():
            self.status = self.DISABLED
        else:
            raise ValueError('"' + value + '" is not a valid state.')
