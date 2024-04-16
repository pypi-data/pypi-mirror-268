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
from pydantic.v1 import Field, StrictStr, conlist, constr, validator
from lusid.models.compliance_step import ComplianceStep
from lusid.models.compliance_template_parameter import ComplianceTemplateParameter

class FilterStep(ComplianceStep):
    """
    FilterStep
    """
    label: constr(strict=True, min_length=1) = Field(..., description="The label of the compliance step")
    parameters: conlist(ComplianceTemplateParameter) = Field(..., description="Parameters required for the step")
    compliance_step_type: StrictStr = Field(..., alias="complianceStepType", description=". The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep")
    additional_properties: Dict[str, Any] = {}
    __properties = ["complianceStepType", "label", "parameters"]

    @validator('compliance_step_type')
    def compliance_step_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('FilterStep', 'GroupByStep', 'GroupFilterStep', 'BranchStep', 'RecombineStep', 'CheckStep'):
            raise ValueError("must be one of enum values ('FilterStep', 'GroupByStep', 'GroupFilterStep', 'BranchStep', 'RecombineStep', 'CheckStep')")
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
    def from_json(cls, json_str: str) -> FilterStep:
        """Create an instance of FilterStep from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FilterStep:
        """Create an instance of FilterStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FilterStep.parse_obj(obj)

        _obj = FilterStep.parse_obj({
            "compliance_step_type": obj.get("complianceStepType"),
            "label": obj.get("label"),
            "parameters": [ComplianceTemplateParameter.from_dict(_item) for _item in obj.get("parameters")] if obj.get("parameters") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
