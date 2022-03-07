from models.HasIdAbstract import HasIdAbstract


class Facility(HasIdAbstract):
    def __init__(self, id, name, description, rp_id):
        super().__init__(id)
        self.name = name
        self.description = description
        self.rp_id = rp_id

    def __str__(self):
        return f"id: {self.id} name: {self.name} description: " \
               f"{self.description} rp_id: {self.rp_id}"
