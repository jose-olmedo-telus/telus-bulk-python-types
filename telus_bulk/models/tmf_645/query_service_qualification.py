# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401
from pydantic import AnyUrl, Field

from telus_bulk.models.tmf_645.related_party import RelatedParty
from telus_bulk.models.tmf_645.service_qualification_item import (
    ServiceQualificationItem,
)
from telus_bulk.models.tmf_645.task_state_type import TaskStateType


class QueryServiceQualification(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    QueryServiceQualification - a model defined in OpenAPI

        id: The id of this QueryServiceQualification [Optional].
        href: The href of this QueryServiceQualification [Optional].
        description: The description of this QueryServiceQualification [Optional].
        effective_qualification_date: The effective_qualification_date of this QueryServiceQualification [Optional].
        estimated_response_date: The estimated_response_date of this QueryServiceQualification [Optional].
        expected_qualification_date: The expected_qualification_date of this QueryServiceQualification [Optional].
        expiration_date: The expiration_date of this QueryServiceQualification [Optional].
        external_id: The external_id of this QueryServiceQualification [Optional].
        instant_sync_qualification: The instant_sync_qualification of this QueryServiceQualification [Optional].
        query_service_qualification_date: The query_service_qualification_date of this QueryServiceQualification [Optional].
        related_party: The related_party of this QueryServiceQualification [Optional].
        search_criteria: The search_criteria of this QueryServiceQualification [Optional].
        service_qualification_item: The service_qualification_item of this QueryServiceQualification [Optional].
        state: The state of this QueryServiceQualification [Optional].
        base_type: The base_type of this QueryServiceQualification [Optional].
        schema_location: The schema_location of this QueryServiceQualification [Optional].
        type: The type of this QueryServiceQualification [Optional].
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
    query_service_qualification_date: Optional[datetime] = None
    related_party: Optional[List[RelatedParty]] = None
    search_criteria: Optional[ServiceQualificationItem] = None
    service_qualification_item: Optional[List[ServiceQualificationItem]] = None
    state: Optional[TaskStateType] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias="@type")


QueryServiceQualification.update_forward_refs()
