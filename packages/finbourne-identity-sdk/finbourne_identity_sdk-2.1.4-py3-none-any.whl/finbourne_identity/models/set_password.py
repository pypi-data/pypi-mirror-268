# coding: utf-8

"""
    FINBOURNE Identity Service API

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
from pydantic.v1 import BaseModel, Field, constr

class SetPassword(BaseModel):
    """
    Set password request  # noqa: E501
    """
    value: constr(strict=True, max_length=50, min_length=12) = Field(..., description="The value of the new password")
    __properties = ["value"]

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
    def from_json(cls, json_str: str) -> SetPassword:
        """Create an instance of SetPassword from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetPassword:
        """Create an instance of SetPassword from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetPassword.parse_obj(obj)

        _obj = SetPassword.parse_obj({
            "value": obj.get("value")
        })
        return _obj
