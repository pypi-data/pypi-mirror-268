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
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from lusid.models.legal_entity import LegalEntity
from lusid.models.model_property import ModelProperty
from lusid.models.resource_id import ResourceId

class CustodianAccount(BaseModel):
    """
    CustodianAccount
    """
    custodian_account_id: ResourceId = Field(..., alias="custodianAccountId")
    status: constr(strict=True, min_length=1) = Field(..., description="The Account status. Can be Active, Inactive or Deleted. Defaults to Active.")
    account_number: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="accountNumber", description="The Custodian Account Number")
    account_name: constr(strict=True, min_length=1) = Field(..., alias="accountName", description="The identifiable name given to the Custodian Account")
    accounting_method: constr(strict=True, min_length=1) = Field(..., alias="accountingMethod", description="The Accounting method to be used")
    currency: StrictStr = Field(..., description="The Currency for the Account")
    properties: Optional[Dict[str, ModelProperty]] = Field(None, description="Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the 'CustodianAccount' domain.")
    custodian: LegalEntity = Field(...)
    account_type: constr(strict=True, min_length=1) = Field(..., alias="accountType", description="The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin.")
    __properties = ["custodianAccountId", "status", "accountNumber", "accountName", "accountingMethod", "currency", "properties", "custodian", "accountType"]

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
    def from_json(cls, json_str: str) -> CustodianAccount:
        """Create an instance of CustodianAccount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of custodian_account_id
        if self.custodian_account_id:
            _dict['custodianAccountId'] = self.custodian_account_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of custodian
        if self.custodian:
            _dict['custodian'] = self.custodian.to_dict()
        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustodianAccount:
        """Create an instance of CustodianAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustodianAccount.parse_obj(obj)

        _obj = CustodianAccount.parse_obj({
            "custodian_account_id": ResourceId.from_dict(obj.get("custodianAccountId")) if obj.get("custodianAccountId") is not None else None,
            "status": obj.get("status"),
            "account_number": obj.get("accountNumber"),
            "account_name": obj.get("accountName"),
            "accounting_method": obj.get("accountingMethod"),
            "currency": obj.get("currency"),
            "properties": dict(
                (_k, ModelProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "custodian": LegalEntity.from_dict(obj.get("custodian")) if obj.get("custodian") is not None else None,
            "account_type": obj.get("accountType")
        })
        return _obj
