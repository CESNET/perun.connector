"""
    Perun RPC API

    Perun Remote Procedure Calls Application Programming Interface  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: perun@cesnet.cz
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from perun.connector.perun_openapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from perun.connector.perun_openapi.exceptions import ApiAttributeError


def lazy_import():
    from perun.connector.perun_openapi.model.attribute import Attribute
    from perun.connector.perun_openapi.model.attribute_definition import AttributeDefinition
    from perun.connector.perun_openapi.model.auditable import Auditable
    from perun.connector.perun_openapi.model.author import Author
    from perun.connector.perun_openapi.model.authorship import Authorship
    from perun.connector.perun_openapi.model.ban import Ban
    from perun.connector.perun_openapi.model.ban_on_facility import BanOnFacility
    from perun.connector.perun_openapi.model.ban_on_resource import BanOnResource
    from perun.connector.perun_openapi.model.ban_on_vo import BanOnVo
    from perun.connector.perun_openapi.model.candidate import Candidate
    from perun.connector.perun_openapi.model.category import Category
    from perun.connector.perun_openapi.model.consent import Consent
    from perun.connector.perun_openapi.model.consent_hub import ConsentHub
    from perun.connector.perun_openapi.model.destination import Destination
    from perun.connector.perun_openapi.model.ext_source import ExtSource
    from perun.connector.perun_openapi.model.facility import Facility
    from perun.connector.perun_openapi.model.group import Group
    from perun.connector.perun_openapi.model.host import Host
    from perun.connector.perun_openapi.model.member import Member
    from perun.connector.perun_openapi.model.owner import Owner
    from perun.connector.perun_openapi.model.publication import Publication
    from perun.connector.perun_openapi.model.publication_for_gui import PublicationForGUI
    from perun.connector.perun_openapi.model.publication_system import PublicationSystem
    from perun.connector.perun_openapi.model.resource import Resource
    from perun.connector.perun_openapi.model.resource_tag import ResourceTag
    from perun.connector.perun_openapi.model.rich_destination import RichDestination
    from perun.connector.perun_openapi.model.rich_facility import RichFacility
    from perun.connector.perun_openapi.model.rich_group import RichGroup
    from perun.connector.perun_openapi.model.rich_member import RichMember
    from perun.connector.perun_openapi.model.rich_resource import RichResource
    from perun.connector.perun_openapi.model.rich_user import RichUser
    from perun.connector.perun_openapi.model.security_team import SecurityTeam
    from perun.connector.perun_openapi.model.service import Service
    from perun.connector.perun_openapi.model.service_for_gui import ServiceForGUI
    from perun.connector.perun_openapi.model.services_package import ServicesPackage
    from perun.connector.perun_openapi.model.task_result import TaskResult
    from perun.connector.perun_openapi.model.thanks import Thanks
    from perun.connector.perun_openapi.model.thanks_for_gui import ThanksForGUI
    from perun.connector.perun_openapi.model.user import User
    from perun.connector.perun_openapi.model.user_ext_source import UserExtSource
    from perun.connector.perun_openapi.model.vo import Vo
    globals()['Attribute'] = Attribute
    globals()['AttributeDefinition'] = AttributeDefinition
    globals()['Auditable'] = Auditable
    globals()['Author'] = Author
    globals()['Authorship'] = Authorship
    globals()['Ban'] = Ban
    globals()['BanOnFacility'] = BanOnFacility
    globals()['BanOnResource'] = BanOnResource
    globals()['BanOnVo'] = BanOnVo
    globals()['Candidate'] = Candidate
    globals()['Category'] = Category
    globals()['Consent'] = Consent
    globals()['ConsentHub'] = ConsentHub
    globals()['Destination'] = Destination
    globals()['ExtSource'] = ExtSource
    globals()['Facility'] = Facility
    globals()['Group'] = Group
    globals()['Host'] = Host
    globals()['Member'] = Member
    globals()['Owner'] = Owner
    globals()['Publication'] = Publication
    globals()['PublicationForGUI'] = PublicationForGUI
    globals()['PublicationSystem'] = PublicationSystem
    globals()['Resource'] = Resource
    globals()['ResourceTag'] = ResourceTag
    globals()['RichDestination'] = RichDestination
    globals()['RichFacility'] = RichFacility
    globals()['RichGroup'] = RichGroup
    globals()['RichMember'] = RichMember
    globals()['RichResource'] = RichResource
    globals()['RichUser'] = RichUser
    globals()['SecurityTeam'] = SecurityTeam
    globals()['Service'] = Service
    globals()['ServiceForGUI'] = ServiceForGUI
    globals()['ServicesPackage'] = ServicesPackage
    globals()['TaskResult'] = TaskResult
    globals()['Thanks'] = Thanks
    globals()['ThanksForGUI'] = ThanksForGUI
    globals()['User'] = User
    globals()['UserExtSource'] = UserExtSource
    globals()['Vo'] = Vo


class PerunBean(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (int,),  # noqa: E501
            'bean_name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'Attribute': Attribute,
            'AttributeDefinition': AttributeDefinition,
            'Auditable': Auditable,
            'Author': Author,
            'Authorship': Authorship,
            'Ban': Ban,
            'BanOnFacility': BanOnFacility,
            'BanOnResource': BanOnResource,
            'BanOnVo': BanOnVo,
            'Candidate': Candidate,
            'Category': Category,
            'Consent': Consent,
            'ConsentHub': ConsentHub,
            'Destination': Destination,
            'ExtSource': ExtSource,
            'Facility': Facility,
            'Group': Group,
            'Host': Host,
            'Member': Member,
            'Owner': Owner,
            'Publication': Publication,
            'PublicationForGUI': PublicationForGUI,
            'PublicationSystem': PublicationSystem,
            'Resource': Resource,
            'ResourceTag': ResourceTag,
            'RichDestination': RichDestination,
            'RichFacility': RichFacility,
            'RichGroup': RichGroup,
            'RichMember': RichMember,
            'RichResource': RichResource,
            'RichUser': RichUser,
            'SecurityTeam': SecurityTeam,
            'Service': Service,
            'ServiceForGUI': ServiceForGUI,
            'ServicesPackage': ServicesPackage,
            'TaskResult': TaskResult,
            'Thanks': Thanks,
            'ThanksForGUI': ThanksForGUI,
            'User': User,
            'UserExtSource': UserExtSource,
            'Vo': Vo,
        }
        if not val:
            return None
        return {'bean_name': val}

    attribute_map = {
        'id': 'id',  # noqa: E501
        'bean_name': 'beanName',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, bean_name, *args, **kwargs):  # noqa: E501
        """PerunBean - a model defined in OpenAPI

        Args:
            id (int):
            bean_name (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.bean_name = bean_name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, bean_name, *args, **kwargs):  # noqa: E501
        """PerunBean - a model defined in OpenAPI

        Args:
            id (int):
            bean_name (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.bean_name = bean_name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
