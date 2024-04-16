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


from typing import Any, Dict
from pydantic.v1 import BaseModel, Field
from lusid.models.transaction import Transaction

class HoldingContributor(BaseModel):
    """
    A list of transactions contributed to a holding.  # noqa: E501
    """
    transaction: Transaction = Field(...)
    __properties = ["transaction"]

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
    def from_json(cls, json_str: str) -> HoldingContributor:
        """Create an instance of HoldingContributor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HoldingContributor:
        """Create an instance of HoldingContributor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HoldingContributor.parse_obj(obj)

        _obj = HoldingContributor.parse_obj({
            "transaction": Transaction.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None
        })
        return _obj
