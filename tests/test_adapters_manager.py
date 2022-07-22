import copy
import logging
from unittest.mock import patch, MagicMock

import pytest

import perun
from perun.connector.adapters.AdaptersManager import (
    AdaptersManager,
)
from perun.connector.adapters.LdapAdapter import LdapAdapter, AdapterSkipException
from perun.connector.adapters.PerunRpcAdapter import PerunRpcAdapter
from perun.connector.models.User import User
from perun.connector.perun_openapi.exceptions import ApiException
from perun.connector.utils.ConfigStore import ConfigStore


class HttpResponse:
    def __init__(self, input_data: str):
        self.status = None
        self.data = input_data
        self.reason = None

    def getheaders(self):
        return "headers"


BASE_MANAGER_CONFIG = {"adapters": []}

# 1st priority adapter is LDAP, 2nd priority is RPC - changes in priority
# might affect test results

LDAP_PRIORITY = 1
LDAP_CONFIG_DATA = {
    "type": "ldap",
    "priority": LDAP_PRIORITY,
    "username": "cn=admin,dc=muni,dc=cz",
    "base_dn": "dc=muni,dc=cz",
    "password": "mypassword",
    "start_tls": True,
    "servers": [
        {"hostname": "ldap://openldap", "port": 389},
        {"hostname": "ldap://openldap2", "port": 389},
    ],
}
LDAP_ADAPTER = LdapAdapter(LDAP_CONFIG_DATA, ConfigStore.get_attribute_map())

RPC_PRIORITY = 2
RPC_CONFIG_DATA = {
    "type": "openApi",
    "priority": RPC_PRIORITY,
    "host": "https://perun.cesnet.cz/krb/rpc",
    "auth_type": "BasicAuth",
    "username": "username",
    "password": "mypasswd",
    "api_key": "your_api_key",
    "access_token": "your_bearer_token",
}

UNSUPPORTED_CONFIG_DATA = {"type": "curl", "priority": 3}
SUPPORTED_CONFIG_DATA = [LDAP_CONFIG_DATA, RPC_CONFIG_DATA]


def is_present_rpc_adapter(manager: AdaptersManager) -> bool:
    has_correct_name = manager.adapters.get(RPC_PRIORITY).get("name") == "rpc_adapter"
    has_correct_instance = isinstance(
        manager.adapters.get(RPC_PRIORITY).get("adapter"), PerunRpcAdapter
    )
    return has_correct_instance and has_correct_name


def is_present_ldap_adapter(manager: AdaptersManager) -> bool:
    has_correct_name = manager.adapters.get(LDAP_PRIORITY).get("name") == "ldap_adapter"
    has_correct_instance = isinstance(
        manager.adapters.get(LDAP_PRIORITY).get("adapter"), LdapAdapter
    )
    return has_correct_instance and has_correct_name


SUPPORTED_ADAPTERS_VALIDATORS = [is_present_rpc_adapter, is_present_ldap_adapter]


def test_create_manager_with_ldap_adapter():
    config = copy.deepcopy(BASE_MANAGER_CONFIG)
    config["adapters"].append(LDAP_CONFIG_DATA)

    manager = AdaptersManager(config, ConfigStore.get_attribute_map())

    assert len(manager.adapters) == 1
    assert is_present_ldap_adapter(manager)


def test_create_manager_with_rpc_adapter():
    config = copy.deepcopy(BASE_MANAGER_CONFIG)
    config["adapters"].append(RPC_CONFIG_DATA)

    manager = AdaptersManager(config, ConfigStore.get_attribute_map())

    assert len(manager.adapters) == 1
    assert is_present_rpc_adapter(manager)


def test_create_manager_with_all_supported_adapters():
    config = copy.deepcopy(BASE_MANAGER_CONFIG)
    config["adapters"] = SUPPORTED_CONFIG_DATA

    manager = AdaptersManager(config, ConfigStore.get_attribute_map())

    assert len(manager.adapters) == len(SUPPORTED_CONFIG_DATA)
    for validator in SUPPORTED_ADAPTERS_VALIDATORS:
        assert validator(manager)


def test_create_manager_with_unsupported_adapter(caplog):
    config = copy.deepcopy(BASE_MANAGER_CONFIG)
    config["adapters"] = copy.deepcopy(SUPPORTED_CONFIG_DATA)
    config["adapters"].append(UNSUPPORTED_CONFIG_DATA)

    unsupported_adapter_type = UNSUPPORTED_CONFIG_DATA.get("type")
    unsupported_adapter_warning = (
        f"Config file includes unsupported adapter "
        f'type "{unsupported_adapter_type}"'
    )

    with caplog.at_level(logging.WARNING):
        manager = AdaptersManager(config, ConfigStore.get_attribute_map())

        assert unsupported_adapter_warning in caplog.text
        assert len(manager.adapters) == len(SUPPORTED_CONFIG_DATA)
        for validator in SUPPORTED_ADAPTERS_VALIDATORS:
            assert validator(manager)


@patch("perun.connector.adapters.LdapAdapter.LdapAdapter.get_perun_user")
def test_find_method_on_first_adapter_successfully_execute(mock_request_1):
    config = copy.deepcopy(BASE_MANAGER_CONFIG)
    config["adapters"] = SUPPORTED_CONFIG_DATA

    manager = AdaptersManager(config, ConfigStore.get_attribute_map())

    test_user = User(1, "John Doe")
    perun.connector.adapters.LdapAdapter.LdapAdapter.get_perun_user = MagicMock(
        return_value=test_user
    )

    result = manager.get_perun_user("1", ["John Doe"])

    assert result == test_user


@patch("perun.connector.adapters.LdapAdapter.LdapAdapter.get_perun_user")
@patch("perun.connector.adapters.PerunRpcAdapter.PerunRpcAdapter.get_perun_user")
def test_find_method_on_second_adapter_successfully_execute(
    mock_request_1, mock_request_2, caplog
):
    config = copy.deepcopy(BASE_MANAGER_CONFIG)
    config["adapters"] = SUPPORTED_CONFIG_DATA

    manager = AdaptersManager(config, ConfigStore.get_attribute_map())

    unsupported_method_call_warning = (
        'Adapter not able to execute given action. Method: "get_perun_user" '
        "Adapter: ldap_adapter Going to try another adapter if available."
    )
    perun.connector.adapters.LdapAdapter.LdapAdapter.get_perun_user = MagicMock(
        side_effect=AdapterSkipException
    )

    test_user = User(1, "John Doe")
    perun.connector.adapters.PerunRpcAdapter.PerunRpcAdapter.get_perun_user = MagicMock(
        return_value=test_user
    )

    with caplog.at_level(logging.WARNING):
        result = manager.get_perun_user("1", ["John Doe"])
        assert unsupported_method_call_warning in caplog.text
        assert result == test_user


@patch("perun.connector.adapters.LdapAdapter.LdapAdapter.get_perun_user")
def test_found_method_fail_on_not_found_exception(mock_request_1, caplog):
    config = copy.deepcopy(BASE_MANAGER_CONFIG)
    config["adapters"] = SUPPORTED_CONFIG_DATA

    manager = AdaptersManager(config, ConfigStore.get_attribute_map())

    perun.connector.adapters.LdapAdapter.LdapAdapter.get_perun_user = MagicMock(
        side_effect=ApiException(
            http_resp=HttpResponse('"name":"UserNotExistsException"')
        )
    )

    # test logging of the exception
    expected_error_message = '"name":"UserNotExistsException"'

    with pytest.raises(Exception) as error:
        manager.get_perun_user("1", ["John Doe"])
        assert str(error.value.args[0]) == expected_error_message


@patch("perun.connector.adapters.LdapAdapter.LdapAdapter.get_perun_user")
@patch("perun.connector.adapters.PerunRpcAdapter.PerunRpcAdapter.get_perun_user")
def test_method_not_found_on_any_adapter(mock_request_1, mock_request_2):
    config = copy.deepcopy(BASE_MANAGER_CONFIG)
    config["adapters"] = SUPPORTED_CONFIG_DATA

    manager = AdaptersManager(config, ConfigStore.get_attribute_map())

    unsupported_method_call_message = (
        "'LdapAdapter' object has no attribute" " 'unsupported_method'"
    )
    unsupported_method_error = AttributeError(unsupported_method_call_message)

    perun.connector.adapters.LdapAdapter.LdapAdapter.get_perun_user = MagicMock(
        side_effect=unsupported_method_error
    )

    perun.connector.adapters.PerunRpcAdapter.PerunRpcAdapter.get_perun_user = MagicMock(
        side_effect=unsupported_method_error
    )

    method_not_found_on_any_adapter_message = (
        "None of the provided adapters "
        "was able to resolve method "
        '"unsupported_method"'
    )
    with pytest.raises(Exception) as error:
        _ = manager.get_perun_user("1", ["John Doe"])
        assert str(error.value.args[0]) == method_not_found_on_any_adapter_message
