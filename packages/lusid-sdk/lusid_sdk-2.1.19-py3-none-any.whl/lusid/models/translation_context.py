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
from pydantic.v1 import BaseModel, Field, StrictBool
from lusid.models.script_map_reference import ScriptMapReference

class TranslationContext(BaseModel):
    """
    Options for overriding default scripted translation configuration.  # noqa: E501
    """
    disable_scripted_translation: Optional[StrictBool] = Field(None, alias="disableScriptedTranslation")
    script_map: Optional[ScriptMapReference] = Field(None, alias="scriptMap")
    __properties = ["disableScriptedTranslation", "scriptMap"]

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
    def from_json(cls, json_str: str) -> TranslationContext:
        """Create an instance of TranslationContext from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of script_map
        if self.script_map:
            _dict['scriptMap'] = self.script_map.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TranslationContext:
        """Create an instance of TranslationContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TranslationContext.parse_obj(obj)

        _obj = TranslationContext.parse_obj({
            "disable_scripted_translation": obj.get("disableScriptedTranslation"),
            "script_map": ScriptMapReference.from_dict(obj.get("scriptMap")) if obj.get("scriptMap") is not None else None
        })
        return _obj
