from models.HasIdAbstract import HasIdAbstract


class User(HasIdAbstract):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def __str__(self):
        return f"id: {self.id} name: {self.name}"
