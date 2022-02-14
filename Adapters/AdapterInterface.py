import abc
from typing import List, Union, Optional
from models import User, Group, VO, Facility, HasIdAbstract, UserExtSource


class AdapterInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                hasattr(subclass, "get_perun_user")
                and callable(subclass.get_perun_user)
                and hasattr(subclass, "get_group_by_name")
                and callable(subclass.get_group_by_name)
                and hasattr(subclass, "get_vo")
                and callable(subclass.get_vo)
                and hasattr(subclass, "get_member_groups")
                and callable(subclass.get_member_groups)
                and hasattr(subclass, "get_sp_groups")
                and callable(subclass.get_sp_groups)
                and hasattr(subclass, "get_user_attributes")
                and callable(subclass.get_user_attributes)
                and hasattr(subclass, "get_entityless_attribute")
                and callable(subclass.get_entityless_attribute)
                and hasattr(subclass, "get_vo_attributes")
                and callable(subclass.get_vo_attributes)
                and hasattr(subclass, "get_facility_attribute")
                and callable(subclass.get_facility_attribute)
                and hasattr(subclass, "get_facility_by_rp_identifier")
                and callable(subclass.get_facility_by_rp_identifier)
                and hasattr(subclass, "get_users_groups_on_facility")
                and callable(subclass.get_users_groups_on_facility)
                and hasattr(subclass, "get_facilities_by_attribute_value")
                and callable(subclass.get_facilities_by_attribute_value)
                and hasattr(subclass, "get_facility_attributes")
                and callable(subclass.get_facility_attributes)
                and hasattr(subclass, "get_user_ext_source")
                and callable(subclass.get_user_ext_source)
                and hasattr(subclass, "update_user_ext_source_last_access")
                and callable(subclass.update_user_ext_source_last_access)
                and hasattr(subclass, "get_user_ext_source_attributes")
                and callable(subclass.get_user_ext_source_attributes)
                and hasattr(subclass, "set_user_ext_source_attributes")
                and callable(subclass.set_user_ext_source_attributes)
                and hasattr(subclass, "get_member_status_by_user_and_vo")
                and callable(subclass.get_member_status_by_user_and_vo)
                and hasattr(subclass, "is_user_in_vo")
                and callable(subclass.is_user_in_vo)
                and hasattr(subclass, "get_resource_capabilities")
                and callable(subclass.get_resource_capabilities)
                and hasattr(subclass, "get_facility_capabilities")
                and callable(subclass.get_facility_capabilities)
                and hasattr(subclass, "unique_entities")
                and callable(subclass.unique_entities)
                or NotImplemented
        )

    @abc.abstractmethod
    def get_perun_user(self, idp_id: str, uids: List[str]) -> User:
        """Get Perun user with at least one of the uids"""
        raise NotImplementedError

    def get_group_by_name(self, vo: VO, name: str) -> Group:
        """Get Group based on its name"""
        raise NotImplementedError

    def get_vo(self, short_name=None, id=None) -> VO:
        """Get VO by either its id or short name"""
        raise NotImplementedError

    def get_member_groups(self, user: User, vo: VO) -> List[Group]:
        """Get member groups of given user"""
        raise NotImplementedError

    def get_sp_groups(self, rp_identifier: str) -> List[Group]:
        """Get groups associated withs given SP entity"""
        raise NotImplementedError

    def get_user_attributes(
            self, user: User, attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        """Get specified attributes of given user"""
        raise NotImplementedError

    def get_entityless_attribute(
            self, attr_name: str
    ) -> Union[str, Optional[int], bool, List[str], dict[str, str]]:
        """Get value of given entityless attribute"""
        raise NotImplementedError

    def get_vo_attributes(
            self, vo: VO, attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        """Get specified attributes of given VO"""
        raise NotImplementedError

    def get_facility_attribute(
            self, facility: Facility, attr_name: str
    ) -> Union[str, Optional[int], bool, List[str], dict[str, str]]:
        """Get specified attribute of given facility"""
        raise NotImplementedError

    def get_facility_by_rp_identifier(
            self, rp_identifier: str, rp_identifier_attr: str
    ) -> Facility:
        """Get specified facility based on given rp_identifier"""
        raise NotImplementedError

    def get_users_groups_on_facility(
            self, rp_identifier: str, user_id: str
    ) -> List[Group]:
        """Get groups of specified user on given facility"""
        raise NotImplementedError

    def get_facilities_by_attribute_value(
            self, attribute: dict[str, str]
    ) -> List[Facility]:
        """Search facilities based on given attribute value"""
        raise NotImplementedError

    def get_facility_attributes(
            self, facility: Facility, attr_names: List[str]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        """Get specified attributes of given facility"""
        raise NotImplementedError

    def get_user_ext_source(
            self, ext_source_name: str, ext_source_login: str
    ) -> str:
        """Get user's external source based on external source name and
        login"""
        raise NotImplementedError

    def update_user_ext_source_last_access(self, user_ext_source: str) -> None:
        """Update user's last access of external source"""
        raise NotImplementedError

    def get_user_ext_source_attributes(
            self, user_ext_source: UserExtSource,
            attributes: List[dict[str, str]]
    ) -> dict[str, Union[str, Optional[int], bool, List[str], dict[str, str]]]:
        """Get attributes of user's external source"""
        raise NotImplementedError

    def set_user_ext_source_attributes(
            self, user_ext_source: UserExtSource,
            attributes: List[dict[str, str]]
    ) -> None:
        """Set attributes of user's external source"""
        raise NotImplementedError

    def get_member_status_by_user_and_vo(self, user: User, vo: VO) -> str:
        """Get member's status based on given User and VO"""
        raise NotImplementedError

    def is_user_in_vo(self, user: User, vo_short_name: str) -> bool:
        """Verifies whether given User is in given VO"""
        raise NotImplementedError

    def get_resource_capabilities(
            self, rp_identifier: str, user_groups: List[Group]
    ) -> List[str]:
        """Obtains resource capabilities of groups linked to the facility
        with given entity ID"""
        raise NotImplementedError

    def get_facility_capabilities(self, rp_identifier: str) -> List[str]:
        """Obtains facility capabilities of facility with given entity ID"""
        raise NotImplementedError

    def unique_entities(
            self, entities: List[HasIdAbstract]
    ) -> List[HasIdAbstract]:
        """Returns objects with IDs of unique entities in input list"""
        raise NotImplementedError
