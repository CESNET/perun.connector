from HasIdAbstract import HasIdAbstract


class UserExtSource(HasIdAbstract):
    def __init__(self, id, name, login, user_id):
        super().__init__(id)
        self.name = name
        self.login = login
        self.user_id = user_id

    def __str__(self):
        return f"id: {self.id} name: {self.name} login: {self.login} " \
               f"user_id: {self.user_id}"
