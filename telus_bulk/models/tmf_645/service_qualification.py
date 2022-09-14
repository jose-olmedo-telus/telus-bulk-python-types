# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401
from pydantic import AnyUrl, Field

from telus_bulk.models.tmf_645.related_party import RelatedParty
from telus_bulk.models.tmf_645.task_state_type import TaskStateType


class ServiceQualification(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceQualification - a model defined in OpenAPI

        id: The id of this ServiceQualification [Optional].
        href: The href of this ServiceQualification [Optional].
        description: The description of this ServiceQualification [Optional].
        effective_qualification_date: The effective_qualification_date of this ServiceQualification [Optional].
        estimated_response_date: The estimated_response_date of this ServiceQualification [Optional].
        expected_qualification_date: The expected_qualification_date of this ServiceQualification [Optional].
        expiration_date: The expiration_date of this ServiceQualification [Optional].
        external_id: The external_id of this ServiceQualification [Optional].
        instant_sync_qualification: The instant_sync_qualification of this ServiceQualification [Optional].
        related_party: The related_party of this ServiceQualification [Optional].
        state: The state of this ServiceQualification [Optional].
        base_type: The base_type of this ServiceQualification [Optional].
        schema_location: The schema_location of this ServiceQualification [Optional].
        type: The type of this ServiceQualification [Optional].
    """

    id: Optional[str] = None
    href: Optional[str] = None
    description: Optional[str] = None
    effective_qualification_date: Optional[datetime] = None
    estimated_response_date: Optional[datetime] = None
    expected_qualification_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None
    external_id: Optional[str] = None
    instant_sync_qualification: Optional[bool] = None
    related_party: Optional[List[RelatedParty]] = None
    state: Optional[TaskStateType] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias="@type")


ServiceQualification.update_forward_refs()
