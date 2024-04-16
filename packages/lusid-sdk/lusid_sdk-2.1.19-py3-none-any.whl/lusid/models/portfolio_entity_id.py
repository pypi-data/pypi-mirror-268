# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

class PortfolioEntityId(BaseModel):
    """
    Specification of a portfolio or portfolio group id, its scope and which it is.  # noqa: E501
    """
    scope: Optional[constr(strict=True, max_length=256, min_length=1)] = Field(None, description="The scope within which the portfolio or portfolio group lives.")
    code: Optional[constr(strict=True, max_length=256, min_length=1)] = Field(None, description="Portfolio name or code.")
    portfolio_entity_type: Optional[constr(strict=True, max_length=128, min_length=0)] = Field(None, alias="portfolioEntityType", description="String identifier for portfolio e.g. \"SinglePortfolio\" and \"GroupPortfolio\". If not specified, it is assumed to be a single portfolio.")
    __properties = ["scope", "code", "portfolioEntityType"]

    @validator('scope')
    def scope_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('code')
    def code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PortfolioEntityId:
        """Create an instance of PortfolioEntityId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        # set to None if portfolio_entity_type (nullable) is None
        # and __fields_set__ contains the field
        if self.portfolio_entity_type is None and "portfolio_entity_type" in self.__fields_set__:
            _dict['portfolioEntityType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PortfolioEntityId:
        """Create an instance of PortfolioEntityId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PortfolioEntityId.parse_obj(obj)

        _obj = PortfolioEntityId.parse_obj({
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "portfolio_entity_type": obj.get("portfolioEntityType")
        })
        return _obj
