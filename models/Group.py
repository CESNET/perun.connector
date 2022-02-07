from models import HasIdAbstract


class Group(HasIdAbstract):
    def __init__(self, id, vo_id, uuid, name, unique_name, description):
        super.__init__(id)
        self.vo_id = vo_id
        self.uuid = uuid
        self.name = name
        self.unique_name = unique_name
        self.description = description

    def __str__(self):
        return "id:", self.id, "vo_id:", self.vo_id, "uuid:", self.uuid, "name:", self.name,\
               "unique_name: ", self.unique_name, "description: ", self.description
