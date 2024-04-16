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


from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr
from lusid.models.component_transaction import ComponentTransaction

class TransactionTemplateRequest(BaseModel):
    """
    TransactionTemplateRequest
    """
    description: constr(strict=True, max_length=100, min_length=0) = Field(..., description="The description of the transaction template.")
    component_transactions: conlist(ComponentTransaction) = Field(..., alias="componentTransactions", description="A set of component transactions that relate to the template to be created.")
    __properties = ["description", "componentTransactions"]

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
    def from_json(cls, json_str: str) -> TransactionTemplateRequest:
        """Create an instance of TransactionTemplateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in component_transactions (list)
        _items = []
        if self.component_transactions:
            for _item in self.component_transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['componentTransactions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionTemplateRequest:
        """Create an instance of TransactionTemplateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionTemplateRequest.parse_obj(obj)

        _obj = TransactionTemplateRequest.parse_obj({
            "description": obj.get("description"),
            "component_transactions": [ComponentTransaction.from_dict(_item) for _item in obj.get("componentTransactions")] if obj.get("componentTransactions") is not None else None
        })
        return _obj
