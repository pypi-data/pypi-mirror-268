# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic.v1 import Field, StrictStr, constr, validator

from typing import Optional

from lusid.models.complete_relation import CompleteRelation
from lusid.models.create_relation_request import CreateRelationRequest
from lusid.models.delete_relation_request import DeleteRelationRequest
from lusid.models.deleted_entity_response import DeletedEntityResponse

from lusid.api_client import ApiClient
from lusid.api_response import ApiResponse
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RelationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def create_relation(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope of the relation definition")], code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The code of the relation definition")], create_relation_request : Annotated[CreateRelationRequest, Field(..., description="The details of the relation to create.")], effective_at : Annotated[Optional[StrictStr], Field(description="The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified.")] = None, **kwargs) -> CompleteRelation:  # noqa: E501
        ...

    @overload
    def create_relation(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope of the relation definition")], code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The code of the relation definition")], create_relation_request : Annotated[CreateRelationRequest, Field(..., description="The details of the relation to create.")], effective_at : Annotated[Optional[StrictStr], Field(description="The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified.")] = None, async_req: Optional[bool]=True, **kwargs) -> CompleteRelation:  # noqa: E501
        ...

    @validate_arguments
    def create_relation(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope of the relation definition")], code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The code of the relation definition")], create_relation_request : Annotated[CreateRelationRequest, Field(..., description="The details of the relation to create.")], effective_at : Annotated[Optional[StrictStr], Field(description="The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified.")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[CompleteRelation, Awaitable[CompleteRelation]]:  # noqa: E501
        """[EXPERIMENTAL] CreateRelation: Create Relation  # noqa: E501

        Create a relation between two entity objects by their identifiers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_relation(scope, code, create_relation_request, effective_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope of the relation definition (required)
        :type scope: str
        :param code: The code of the relation definition (required)
        :type code: str
        :param create_relation_request: The details of the relation to create. (required)
        :type create_relation_request: CreateRelationRequest
        :param effective_at: The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified.
        :type effective_at: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CompleteRelation
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_relation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.create_relation_with_http_info(scope, code, create_relation_request, effective_at, **kwargs)  # noqa: E501

    @validate_arguments
    def create_relation_with_http_info(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope of the relation definition")], code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The code of the relation definition")], create_relation_request : Annotated[CreateRelationRequest, Field(..., description="The details of the relation to create.")], effective_at : Annotated[Optional[StrictStr], Field(description="The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EXPERIMENTAL] CreateRelation: Create Relation  # noqa: E501

        Create a relation between two entity objects by their identifiers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_relation_with_http_info(scope, code, create_relation_request, effective_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope of the relation definition (required)
        :type scope: str
        :param code: The code of the relation definition (required)
        :type code: str
        :param create_relation_request: The details of the relation to create. (required)
        :type create_relation_request: CreateRelationRequest
        :param effective_at: The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified.
        :type effective_at: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CompleteRelation, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'scope',
            'code',
            'create_relation_request',
            'effective_at'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_relation" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['scope']:
            _path_params['scope'] = _params['scope']

        if _params['code']:
            _path_params['code'] = _params['code']


        # process the query parameters
        _query_params = []
        if _params.get('effective_at') is not None:  # noqa: E501
            _query_params.append(('effectiveAt', _params['effective_at']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_relation_request'] is not None:
            _body_params = _params['create_relation_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "CompleteRelation",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/relations/{scope}/{code}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def delete_relation(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope of the relation definition")], code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The code of the relation definition")], delete_relation_request : Annotated[DeleteRelationRequest, Field(..., description="The details of the relation to delete.")], effective_at : Annotated[Optional[StrictStr], Field(description="The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified.")] = None, **kwargs) -> DeletedEntityResponse:  # noqa: E501
        ...

    @overload
    def delete_relation(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope of the relation definition")], code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The code of the relation definition")], delete_relation_request : Annotated[DeleteRelationRequest, Field(..., description="The details of the relation to delete.")], effective_at : Annotated[Optional[StrictStr], Field(description="The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified.")] = None, async_req: Optional[bool]=True, **kwargs) -> DeletedEntityResponse:  # noqa: E501
        ...

    @validate_arguments
    def delete_relation(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope of the relation definition")], code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The code of the relation definition")], delete_relation_request : Annotated[DeleteRelationRequest, Field(..., description="The details of the relation to delete.")], effective_at : Annotated[Optional[StrictStr], Field(description="The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified.")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[DeletedEntityResponse, Awaitable[DeletedEntityResponse]]:  # noqa: E501
        """[EXPERIMENTAL] DeleteRelation: Delete a relation  # noqa: E501

        Delete a relation between two entity objects represented by their identifiers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_relation(scope, code, delete_relation_request, effective_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope of the relation definition (required)
        :type scope: str
        :param code: The code of the relation definition (required)
        :type code: str
        :param delete_relation_request: The details of the relation to delete. (required)
        :type delete_relation_request: DeleteRelationRequest
        :param effective_at: The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified.
        :type effective_at: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeletedEntityResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_relation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.delete_relation_with_http_info(scope, code, delete_relation_request, effective_at, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_relation_with_http_info(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope of the relation definition")], code : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The code of the relation definition")], delete_relation_request : Annotated[DeleteRelationRequest, Field(..., description="The details of the relation to delete.")], effective_at : Annotated[Optional[StrictStr], Field(description="The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EXPERIMENTAL] DeleteRelation: Delete a relation  # noqa: E501

        Delete a relation between two entity objects represented by their identifiers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_relation_with_http_info(scope, code, delete_relation_request, effective_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope of the relation definition (required)
        :type scope: str
        :param code: The code of the relation definition (required)
        :type code: str
        :param delete_relation_request: The details of the relation to delete. (required)
        :type delete_relation_request: DeleteRelationRequest
        :param effective_at: The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified.
        :type effective_at: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DeletedEntityResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'scope',
            'code',
            'delete_relation_request',
            'effective_at'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_relation" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['scope']:
            _path_params['scope'] = _params['scope']

        if _params['code']:
            _path_params['code'] = _params['code']


        # process the query parameters
        _query_params = []
        if _params.get('effective_at') is not None:  # noqa: E501
            _query_params.append(('effectiveAt', _params['effective_at']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['delete_relation_request'] is not None:
            _body_params = _params['delete_relation_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "DeletedEntityResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/relations/{scope}/{code}/$delete', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
