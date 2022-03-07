from models.HasIdAbstract import HasIdAbstract


class UserExtSource(HasIdAbstract):
    def __init__(self, id, name, login, user):
        super().__init__(id)
        self.name = name
        self.login = login
        self.user = user

    def __str__(self):
        return f"id: {self.id} name: {self.name} login: {self.login} " \
               f"user: {self.user}"
