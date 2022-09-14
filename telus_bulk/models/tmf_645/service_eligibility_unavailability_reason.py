# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel
from pydantic import AnyUrl, Field


class ServiceEligibilityUnavailabilityReason(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceEligibilityUnavailabilityReason - a model defined in OpenAPI

        code: The code of this ServiceEligibilityUnavailabilityReason [Optional].
        label: The label of this ServiceEligibilityUnavailabilityReason [Optional].
        base_type: The base_type of this ServiceEligibilityUnavailabilityReason [Optional].
        schema_location: The schema_location of this ServiceEligibilityUnavailabilityReason [Optional].
        type: The type of this ServiceEligibilityUnavailabilityReason [Optional].
    """

    code: Optional[str] = None
    label: Optional[str] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias='@type')


ServiceEligibilityUnavailabilityReason.update_forward_refs()
