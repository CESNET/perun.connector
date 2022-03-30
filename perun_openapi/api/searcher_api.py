"""
    Perun RPC API

    Perun Remote Procedure Calls Application Programming Interface  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: perun@cesnet.cz
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from perun_openapi.api_client import ApiClient, Endpoint as _Endpoint
from perun_openapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from perun_openapi.model.facility import Facility
from perun_openapi.model.input_get_facilities import InputGetFacilities
from perun_openapi.model.input_get_members_by_user_attributes import InputGetMembersByUserAttributes
from perun_openapi.model.input_get_resources import InputGetResources
from perun_openapi.model.input_get_resources1 import InputGetResources1
from perun_openapi.model.input_get_users import InputGetUsers
from perun_openapi.model.member import Member
from perun_openapi.model.perun_exception import PerunException
from perun_openapi.model.resource import Resource
from perun_openapi.model.user import User


class SearcherApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_attributes_match_resources_endpoint = _Endpoint(
            settings={
                'response_type': ([Resource],),
                'auth': [
                    'ApiKeyAuth',
                    'BasicAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/json/Searcher/getResources/attributes-match',
                'operation_id': 'get_attributes_match_resources',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_get_resources1',
                ],
                'required': [
                    'input_get_resources1',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'input_get_resources1':
                        (InputGetResources1,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_get_resources1': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_attributes_resources_endpoint = _Endpoint(
            settings={
                'response_type': ([Resource],),
                'auth': [
                    'ApiKeyAuth',
                    'BasicAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/json/Searcher/getResources/attributes',
                'operation_id': 'get_attributes_resources',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_get_resources',
                ],
                'required': [
                    'input_get_resources',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'input_get_resources':
                        (InputGetResources,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_get_resources': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_facilities_endpoint = _Endpoint(
            settings={
                'response_type': ([Facility],),
                'auth': [
                    'ApiKeyAuth',
                    'BasicAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/json/Searcher/getFacilities',
                'operation_id': 'get_facilities',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_get_facilities',
                ],
                'required': [
                    'input_get_facilities',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'input_get_facilities':
                        (InputGetFacilities,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_get_facilities': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_members_by_user_attributes_endpoint = _Endpoint(
            settings={
                'response_type': ([Member],),
                'auth': [
                    'ApiKeyAuth',
                    'BasicAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/json/Searcher/getMembersByUserAttributes',
                'operation_id': 'get_members_by_user_attributes',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_get_members_by_user_attributes',
                ],
                'required': [
                    'input_get_members_by_user_attributes',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'input_get_members_by_user_attributes':
                        (InputGetMembersByUserAttributes,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_get_members_by_user_attributes': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_users_searcher_endpoint = _Endpoint(
            settings={
                'response_type': ([User],),
                'auth': [
                    'ApiKeyAuth',
                    'BasicAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/json/Searcher/getUsers',
                'operation_id': 'get_users_searcher',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_get_users',
                ],
                'required': [
                    'input_get_users',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'input_get_users':
                        (InputGetUsers,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_get_users': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_attributes_match_resources(
        self,
        input_get_resources1,
        **kwargs
    ):
        """Get list of resources that have attributes with partially matched values if allowPartialMatchForString is set to true, else with exactly matched values.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_attributes_match_resources(input_get_resources1, async_req=True)
        >>> result = thread.get()

        Args:
            input_get_resources1 (InputGetResources1):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Resource]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['input_get_resources1'] = \
            input_get_resources1
        return self.get_attributes_match_resources_endpoint.call_with_http_info(**kwargs)

    def get_attributes_resources(
        self,
        input_get_resources,
        **kwargs
    ):
        """Get list of resources who have attributes with specific values.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_attributes_resources(input_get_resources, async_req=True)
        >>> result = thread.get()

        Args:
            input_get_resources (InputGetResources):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Resource]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['input_get_resources'] = \
            input_get_resources
        return self.get_attributes_resources_endpoint.call_with_http_info(**kwargs)

    def get_facilities(
        self,
        input_get_facilities,
        **kwargs
    ):
        """Get list of facilities who have attributes with specific values.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_facilities(input_get_facilities, async_req=True)
        >>> result = thread.get()

        Args:
            input_get_facilities (InputGetFacilities):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Facility]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['input_get_facilities'] = \
            input_get_facilities
        return self.get_facilities_endpoint.call_with_http_info(**kwargs)

    def get_members_by_user_attributes(
        self,
        input_get_members_by_user_attributes,
        **kwargs
    ):
        """Get list of members who have attributes with specific values.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_members_by_user_attributes(input_get_members_by_user_attributes, async_req=True)
        >>> result = thread.get()

        Args:
            input_get_members_by_user_attributes (InputGetMembersByUserAttributes):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Member]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['input_get_members_by_user_attributes'] = \
            input_get_members_by_user_attributes
        return self.get_members_by_user_attributes_endpoint.call_with_http_info(**kwargs)

    def get_users_searcher(
        self,
        input_get_users,
        **kwargs
    ):
        """Get list of users who have attributes with specific values.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_users_searcher(input_get_users, async_req=True)
        >>> result = thread.get()

        Args:
            input_get_users (InputGetUsers):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [User]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['input_get_users'] = \
            input_get_users
        return self.get_users_searcher_endpoint.call_with_http_info(**kwargs)

