# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401
from pydantic import AnyUrl, Field

from telus_bulk.models.tmf_645.service_category_ref import ServiceCategoryRef
from telus_bulk.models.tmf_645.service_ref_or_value import ServiceRefOrValue


class ServiceQualificationItem(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceQualificationItem - a model defined in OpenAPI

        id: The id of this ServiceQualificationItem [Optional].
        expected_activation_date: The expected_activation_date of this ServiceQualificationItem [Optional].
        expected_service_availability_date: The expected_service_availability_date of this ServiceQualificationItem [Optional].
        expiration_date: The expiration_date of this ServiceQualificationItem [Optional].
        category: The category of this ServiceQualificationItem [Optional].
        service: The service of this ServiceQualificationItem [Optional].
        base_type: The base_type of this ServiceQualificationItem [Optional].
        schema_location: The schema_location of this ServiceQualificationItem [Optional].
        type: The type of this ServiceQualificationItem [Optional].
    """

    id: Optional[str] = None
    expected_activation_date: Optional[datetime] = None
    expected_service_availability_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None
    category: Optional[ServiceCategoryRef] = None
    service: Optional[ServiceRefOrValue] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias="@type")


ServiceQualificationItem.update_forward_refs()
