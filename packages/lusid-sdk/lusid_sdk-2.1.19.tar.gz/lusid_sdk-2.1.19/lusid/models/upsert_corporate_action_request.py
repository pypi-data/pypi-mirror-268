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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator
from lusid.models.corporate_action_transition_request import CorporateActionTransitionRequest

class UpsertCorporateActionRequest(BaseModel):
    """
    UpsertCorporateActionRequest
    """
    corporate_action_code: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="corporateActionCode", description="The unique identifier of this corporate action")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="The description of the corporate action.")
    announcement_date: datetime = Field(..., alias="announcementDate", description="The announcement date of the corporate action")
    ex_date: datetime = Field(..., alias="exDate", description="The ex date of the corporate action")
    record_date: datetime = Field(..., alias="recordDate", description="The record date of the corporate action")
    payment_date: datetime = Field(..., alias="paymentDate", description="The payment date of the corporate action")
    transitions: conlist(CorporateActionTransitionRequest) = Field(..., description="The transitions that result from this corporate action")
    __properties = ["corporateActionCode", "description", "announcementDate", "exDate", "recordDate", "paymentDate", "transitions"]

    @validator('corporate_action_code')
    def corporate_action_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
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
    def from_json(cls, json_str: str) -> UpsertCorporateActionRequest:
        """Create an instance of UpsertCorporateActionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in transitions (list)
        _items = []
        if self.transitions:
            for _item in self.transitions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transitions'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpsertCorporateActionRequest:
        """Create an instance of UpsertCorporateActionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpsertCorporateActionRequest.parse_obj(obj)

        _obj = UpsertCorporateActionRequest.parse_obj({
            "corporate_action_code": obj.get("corporateActionCode"),
            "description": obj.get("description"),
            "announcement_date": obj.get("announcementDate"),
            "ex_date": obj.get("exDate"),
            "record_date": obj.get("recordDate"),
            "payment_date": obj.get("paymentDate"),
            "transitions": [CorporateActionTransitionRequest.from_dict(_item) for _item in obj.get("transitions")] if obj.get("transitions") is not None else None
        })
        return _obj
