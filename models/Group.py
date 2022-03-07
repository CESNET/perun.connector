from models.HasIdAbstract import HasIdAbstract


class Group(HasIdAbstract):
    def __init__(self, id, vo, uuid, name, unique_name, description):
        super().__init__(id)
        self.vo = vo
        self.uuid = uuid
        self.name = name
        self.unique_name = unique_name
        self.description = description

    def __str__(self):
        return f"id: {self.id} vo: {self.vo} uuid: {self.uuid} name: " \
               f"{self.name} unique_name: {self.unique_name}, descri" \
               f"ption: {self.description}"
