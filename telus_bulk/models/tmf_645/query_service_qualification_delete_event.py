# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401

from telus_bulk.models.tmf_645.query_service_qualification_delete_event_payload import (
    QueryServiceQualificationDeleteEventPayload,
)


class QueryServiceQualificationDeleteEvent(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    QueryServiceQualificationDeleteEvent - a model defined in OpenAPI

        event: The event of this QueryServiceQualificationDeleteEvent [Optional].
        event_id: The event_id of this QueryServiceQualificationDeleteEvent [Optional].
        event_time: The event_time of this QueryServiceQualificationDeleteEvent [Optional].
        event_type: The event_type of this QueryServiceQualificationDeleteEvent [Optional].
        correlation_id: The correlation_id of this QueryServiceQualificationDeleteEvent [Optional].
        domain: The domain of this QueryServiceQualificationDeleteEvent [Optional].
        title: The title of this QueryServiceQualificationDeleteEvent [Optional].
        description: The description of this QueryServiceQualificationDeleteEvent [Optional].
        priority: The priority of this QueryServiceQualificationDeleteEvent [Optional].
        time_ocurred: The time_ocurred of this QueryServiceQualificationDeleteEvent [Optional].
    """

    event: Optional[QueryServiceQualificationDeleteEventPayload] = None
    event_id: Optional[str] = None
    event_time: Optional[datetime] = None
    event_type: Optional[str] = None
    correlation_id: Optional[str] = None
    domain: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    time_ocurred: Optional[datetime] = None


QueryServiceQualificationDeleteEvent.update_forward_refs()
