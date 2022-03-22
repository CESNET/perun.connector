from models.HasIdAbstract import HasIdAbstract


class Resource(HasIdAbstract):
    def __init__(self, id, vo, facility, name):
        super().__init__(id)
        self.vo = vo
        self.facility = facility
        self.name = name

    def __str__(self):
        return f"id: {self.id} vo: {self.vo} facility: {self.facility} "\
               f"name: {self.name}"
