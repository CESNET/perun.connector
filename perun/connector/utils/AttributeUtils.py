from typing import List

from perun.connector.utils.Logger import Logger


class AttributeUtils:
    LDAP = "ldap"
    TYPE = "type"
    PERUN_STRING = "java.lang.String"
    PERUN_LIST = "java.util.ArrayList"
    PERUN_INT = "java.lang.Integer"
    PERUN_DICT = "java.util.LinkedHashMap"
    PERUN_BOOL = "java.lang.Boolean"

    def __init__(self, attrs_map):
        self._logger = Logger.get_logger(self.__class__.__name__)
        self.attributes_map = attrs_map

    def get_specific_attrs_config_dict(self, attr_names: List[str]):
        result = {}
        for attr_name in attr_names:
            attr_cfg = self.attributes_map.get(attr_name)
            if attr_cfg is None:
                self._logger.warning(
                    f'Missing "{attr_name}" attribute in config '
                    f"file, omitting this attribute from the result map."
                )
                continue
            result[attr_name] = attr_cfg
        return result

    def get_ldap_attr_names(self, attr_names: List[str]):
        result = []
        for attr_name in attr_names:
            attr_cfg = self.attributes_map.get(attr_name)
            if attr_cfg is None:
                self._logger.warning(
                    f'Missing "{attr_name}" attribute in config '
                    f"file, omitting this attribute from the result map."
                )
                continue
            if "ldap" in attr_cfg and attr_cfg["ldap"]:
                result.append(attr_cfg["ldap"])
            else:
                self._logger.warning(
                    f'requested attribute: "{attr_name}" attribute is not in ldap.'
                )
                return []
        return result
