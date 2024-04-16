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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cdo_sdk_python.models.cdo_transaction_status import CdoTransactionStatus
from cdo_sdk_python.models.cdo_transaction_type import CdoTransactionType
from typing import Optional, Set
from typing_extensions import Self

class CdoTransaction(BaseModel):
    """
    CdoTransaction
    """ # noqa: E501
    transaction_uid: Optional[StrictStr] = Field(default=None, description="The unique identifier of the asynchronous transaction triggered.", alias="transactionUid")
    tenant_uid: Optional[StrictStr] = Field(default=None, description="The unique identifier of the tenant that asynchronous transaction triggered on.", alias="tenantUid")
    entity_uid: Optional[StrictStr] = Field(default=None, description="The unique identifier of the entity that the asynchronous transaction is triggered on.", alias="entityUid")
    entity_url: Optional[StrictStr] = Field(default=None, description="A URL to access the entity that the asynchronous transaction is triggered on.", alias="entityUrl")
    transaction_polling_url: Optional[StrictStr] = Field(default=None, description="The URL to poll to track the progress of the transaction.", alias="transactionPollingUrl")
    submission_time: Optional[datetime] = Field(default=None, description="The time (UTC; represented using the RFC-3339 standard) at which the transaction was triggered", alias="submissionTime")
    last_updated_time: Optional[datetime] = Field(default=None, description="The time (UTC; represented using the RFC-3339 standard) at which the transaction status was last updated", alias="lastUpdatedTime")
    transaction_type: Optional[CdoTransactionType] = Field(default=None, alias="transactionType")
    cdo_transaction_status: Optional[CdoTransactionStatus] = Field(default=None, alias="cdoTransactionStatus")
    error_message: Optional[StrictStr] = Field(default=None, description="Transaction error message, if any", alias="errorMessage")
    error_details: Optional[Dict[str, StrictStr]] = Field(default=None, description="Transaction error details, if any", alias="errorDetails")
    __properties: ClassVar[List[str]] = ["transactionUid", "tenantUid", "entityUid", "entityUrl", "transactionPollingUrl", "submissionTime", "lastUpdatedTime", "transactionType", "cdoTransactionStatus", "errorMessage", "errorDetails"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CdoTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CdoTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactionUid": obj.get("transactionUid"),
            "tenantUid": obj.get("tenantUid"),
            "entityUid": obj.get("entityUid"),
            "entityUrl": obj.get("entityUrl"),
            "transactionPollingUrl": obj.get("transactionPollingUrl"),
            "submissionTime": obj.get("submissionTime"),
            "lastUpdatedTime": obj.get("lastUpdatedTime"),
            "transactionType": obj.get("transactionType"),
            "cdoTransactionStatus": obj.get("cdoTransactionStatus"),
            "errorMessage": obj.get("errorMessage"),
            "errorDetails": obj.get("errorDetails")
        })
        return _obj


