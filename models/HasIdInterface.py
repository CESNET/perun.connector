import abc


class HasIdInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "get_id")
            and callable(subclass.get_id)
            or NotImplemented
        )

    @abc.abstractmethod
    def get_id(self) -> int:
        """Get ID of entity"""
        raise NotImplementedError
