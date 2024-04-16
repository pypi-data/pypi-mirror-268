# coding: utf-8

"""
    CDO API

    Use the documentation to explore the endpoints CDO has to offer

    The version of the OpenAPI document: 0.1.0
    Contact: cdo.tac@cisco.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Status(str, Enum):
    """
    The status of the SDC.
    """

    """
    allowed enum values
    """
    NEW = 'NEW'
    ONBOARDING = 'ONBOARDING'
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    DISABLED = 'DISABLED'
    UNKNOWN = 'UNKNOWN'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Status from a JSON string"""
        return cls(json.loads(json_str))


