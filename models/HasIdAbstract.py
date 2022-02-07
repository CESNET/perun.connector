import abc


class HasIdAbstract(metaclass=abc.ABCMeta):

    def __init__(self, id):
        self.id = id
