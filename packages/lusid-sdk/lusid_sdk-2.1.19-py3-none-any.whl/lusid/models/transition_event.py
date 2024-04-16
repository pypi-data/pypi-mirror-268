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
from pydantic.v1 import Field, StrictStr, conlist, validator
from lusid.models.input_transition import InputTransition
from lusid.models.instrument_event import InstrumentEvent
from lusid.models.output_transition import OutputTransition

class TransitionEvent(InstrumentEvent):
    """
    A 'transition' within a corporate action, representing a set of output movements paired to a single input position  # noqa: E501
    """
    announcement_date: Optional[datetime] = Field(None, alias="announcementDate", description="The announcement date of the corporate action")
    ex_date: Optional[datetime] = Field(None, alias="exDate", description="The ex date of the corporate action")
    record_date: Optional[datetime] = Field(None, alias="recordDate", description="The record date of the corporate action")
    payment_date: Optional[datetime] = Field(None, alias="paymentDate", description="The payment date of the corporate action")
    input_transition: Optional[InputTransition] = Field(None, alias="inputTransition")
    output_transitions: Optional[conlist(OutputTransition)] = Field(None, alias="outputTransitions", description="The resulting transitions from this event")
    instrument_event_type: StrictStr = Field(..., alias="instrumentEventType", description="The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent")
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentEventType", "announcementDate", "exDate", "recordDate", "paymentDate", "inputTransition", "outputTransitions"]

    @validator('instrument_event_type')
    def instrument_event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent'):
            raise ValueError("must be one of enum values ('TransitionEvent', 'InformationalEvent', 'OpenEvent', 'CloseEvent', 'StockSplitEvent', 'BondDefaultEvent', 'CashDividendEvent', 'AmortisationEvent', 'CashFlowEvent', 'ExerciseEvent', 'ResetEvent', 'TriggerEvent', 'RawVendorEvent', 'InformationalErrorEvent', 'BondCouponEvent', 'DividendReinvestmentEvent', 'AccumulationEvent', 'BondPrincipalEvent', 'DividendOptionEvent', 'MaturityEvent', 'FxForwardSettlementEvent', 'ExpiryEvent', 'ScripDividendEvent')")
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
    def from_json(cls, json_str: str) -> TransitionEvent:
        """Create an instance of TransitionEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of input_transition
        if self.input_transition:
            _dict['inputTransition'] = self.input_transition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in output_transitions (list)
        _items = []
        if self.output_transitions:
            for _item in self.output_transitions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['outputTransitions'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if output_transitions (nullable) is None
        # and __fields_set__ contains the field
        if self.output_transitions is None and "output_transitions" in self.__fields_set__:
            _dict['outputTransitions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransitionEvent:
        """Create an instance of TransitionEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransitionEvent.parse_obj(obj)

        _obj = TransitionEvent.parse_obj({
            "instrument_event_type": obj.get("instrumentEventType"),
            "announcement_date": obj.get("announcementDate"),
            "ex_date": obj.get("exDate"),
            "record_date": obj.get("recordDate"),
            "payment_date": obj.get("paymentDate"),
            "input_transition": InputTransition.from_dict(obj.get("inputTransition")) if obj.get("inputTransition") is not None else None,
            "output_transitions": [OutputTransition.from_dict(_item) for _item in obj.get("outputTransitions")] if obj.get("outputTransitions") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
