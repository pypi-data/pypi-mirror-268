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
from datetime import datetime

from pydantic.v1 import Field, constr, validator

from typing import Optional

from lusid.models.resource_list_of_change import ResourceListOfChange

from lusid.api_client import ApiClient
from lusid.api_response import ApiResponse
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EntitiesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def get_portfolio_changes(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope")], effective_at : Annotated[constr(strict=True, max_length=256, min_length=0), Field(..., description="The effective date of the origin.")], as_at : Annotated[Optional[datetime], Field(description="The as-at date of the origin.")] = None, **kwargs) -> ResourceListOfChange:  # noqa: E501
        ...

    @overload
    def get_portfolio_changes(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope")], effective_at : Annotated[constr(strict=True, max_length=256, min_length=0), Field(..., description="The effective date of the origin.")], as_at : Annotated[Optional[datetime], Field(description="The as-at date of the origin.")] = None, async_req: Optional[bool]=True, **kwargs) -> ResourceListOfChange:  # noqa: E501
        ...

    @validate_arguments
    def get_portfolio_changes(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope")], effective_at : Annotated[constr(strict=True, max_length=256, min_length=0), Field(..., description="The effective date of the origin.")], as_at : Annotated[Optional[datetime], Field(description="The as-at date of the origin.")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[ResourceListOfChange, Awaitable[ResourceListOfChange]]:  # noqa: E501
        """[EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.  # noqa: E501

        Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subscriptions (e.g corporate actions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_portfolio_changes(scope, effective_at, as_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope (required)
        :type scope: str
        :param effective_at: The effective date of the origin. (required)
        :type effective_at: str
        :param as_at: The as-at date of the origin.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfChange
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_portfolio_changes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_portfolio_changes_with_http_info(scope, effective_at, as_at, **kwargs)  # noqa: E501

    @validate_arguments
    def get_portfolio_changes_with_http_info(self, scope : Annotated[constr(strict=True, max_length=64, min_length=1), Field(..., description="The scope")], effective_at : Annotated[constr(strict=True, max_length=256, min_length=0), Field(..., description="The effective date of the origin.")], as_at : Annotated[Optional[datetime], Field(description="The as-at date of the origin.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.  # noqa: E501

        Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subscriptions (e.g corporate actions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_portfolio_changes_with_http_info(scope, effective_at, as_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope (required)
        :type scope: str
        :param effective_at: The effective date of the origin. (required)
        :type effective_at: str
        :param as_at: The as-at date of the origin.
        :type as_at: datetime
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
        :rtype: tuple(ResourceListOfChange, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'scope',
            'effective_at',
            'as_at'
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
                    " to method get_portfolio_changes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('scope') is not None:  # noqa: E501
            _query_params.append(('scope', _params['scope']))

        if _params.get('effective_at') is not None:  # noqa: E501
            _query_params.append(('effectiveAt', _params['effective_at']))

        if _params.get('as_at') is not None:  # noqa: E501
            if isinstance(_params['as_at'], datetime):
                _query_params.append(('asAt', _params['as_at'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('asAt', _params['as_at']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '400': "LusidValidationProblemDetails",
            '200': "ResourceListOfChange",
        }

        return self.api_client.call_api(
            '/api/entities/changes/portfolios', 'GET',
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
