from HasIdAbstract import HasIdAbstract


class UserExtSource(HasIdAbstract):
    def __init__(self, id, name, bean_name, type, attributes):
        super().__init__(id)
        self.name = name
        self.bean_name = bean_name
        self.type = type
        self.attributes = attributes

    def __str__(self):
        return f"id: {self.id} name: {self.name} bean_name: {self.bean_name} "\
               f"type: {self.type} attributes: {self.attributes}"
