# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import datetime  # noqa: F401
from typing import List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel
from pydantic import AnyUrl, Field  # noqa: F401

from telus_bulk.models.tmf_645.alternate_service_proposal import (
    AlternateServiceProposal,
)
from telus_bulk.models.tmf_645.service_category_ref import ServiceCategoryRef
from telus_bulk.models.tmf_645.service_eligibility_unavailability_reason import (
    ServiceEligibilityUnavailabilityReason,
)
from telus_bulk.models.tmf_645.service_qualification_item_relationship import (
    ServiceQualificationItemRelationship,
)
from telus_bulk.models.tmf_645.service_qualification_relationship import (
    ServiceQualificationRelationship,
)
from telus_bulk.models.tmf_645.service_ref_or_value import ServiceRefOrValue
from telus_bulk.models.tmf_645.termination_error import TerminationError


class CheckServiceQualificationItem(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CheckServiceQualificationItem - a model defined in OpenAPI

        id: The id of this CheckServiceQualificationItem [Optional].
        expected_activation_date: The expected_activation_date of this CheckServiceQualificationItem [Optional].
        expected_service_availability_date: The expected_service_availability_date of this CheckServiceQualificationItem [Optional].
        expiration_date: The expiration_date of this CheckServiceQualificationItem [Optional].
        qualification_result: The qualification_result of this CheckServiceQualificationItem [Optional].
        state: The state of this CheckServiceQualificationItem [Optional].
        alternate_service_proposal: The alternate_service_proposal of this CheckServiceQualificationItem [Optional].
        category: The category of this CheckServiceQualificationItem [Optional].
        eligibility_unavailability_reason: The eligibility_unavailability_reason of this CheckServiceQualificationItem [Optional].
        qualification_item_relationship: The qualification_item_relationship of this CheckServiceQualificationItem [Optional].
        qualification_relationship: The qualification_relationship of this CheckServiceQualificationItem [Optional].
        service: The service of this CheckServiceQualificationItem [Optional].
        termination_error: The termination_error of this CheckServiceQualificationItem [Optional].
        base_type: The base_type of this CheckServiceQualificationItem [Optional].
        schema_location: The schema_location of this CheckServiceQualificationItem [Optional].
        type: The type of this CheckServiceQualificationItem [Optional].
    """

    id: Optional[str] = None
    expected_activation_date: Optional[datetime] = None
    expected_service_availability_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None
    qualification_result: Optional[str] = None
    state: Optional[str] = None
    alternate_service_proposal: Optional[List[AlternateServiceProposal]] = None
    category: Optional[ServiceCategoryRef] = None
    eligibility_unavailability_reason: Optional[
        List[ServiceEligibilityUnavailabilityReason]
    ] = None
    qualification_item_relationship: Optional[
        List[ServiceQualificationItemRelationship]
    ] = None
    qualification_relationship: Optional[List[ServiceQualificationRelationship]] = None
    service: Optional[ServiceRefOrValue] = None
    termination_error: Optional[List[TerminationError]] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias="@type")


CheckServiceQualificationItem.update_forward_refs()
