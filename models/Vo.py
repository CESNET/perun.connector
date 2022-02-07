from models import HasIdAbstract


class Vo(HasIdAbstract):
    def __init__(self, id, name, short_name):
        super.__init__(id)
        self.name = name
        self.short_name = short_name

    def __str__(self):
        return "id:", self.id, "name: ", self.name, "short_name: ", self.short_name
