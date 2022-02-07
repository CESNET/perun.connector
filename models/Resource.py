from models import HasIdAbstract


class Resource(HasIdAbstract):
    def __init__(self, id, vo_id, facility_id, name):
        super.__init__(id)
        self.vo_id = vo_id
        self.facility_id = facility_id
        self.name = name

    def __str__(self):
        return "id:", self.id, "vo_id: ", self.vo_id, "facility_id: ", self.facility_id, "name:", self.name
