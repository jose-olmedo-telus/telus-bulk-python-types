# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401

from telus_bulk.models.tmf_645.query_service_qualification_create_event_payload import (
    QueryServiceQualificationCreateEventPayload,
)


class QueryServiceQualificationCreateEvent(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    QueryServiceQualificationCreateEvent - a model defined in OpenAPI

        event: The event of this QueryServiceQualificationCreateEvent [Optional].
        event_id: The event_id of this QueryServiceQualificationCreateEvent [Optional].
        event_time: The event_time of this QueryServiceQualificationCreateEvent [Optional].
        event_type: The event_type of this QueryServiceQualificationCreateEvent [Optional].
        correlation_id: The correlation_id of this QueryServiceQualificationCreateEvent [Optional].
        domain: The domain of this QueryServiceQualificationCreateEvent [Optional].
        title: The title of this QueryServiceQualificationCreateEvent [Optional].
        description: The description of this QueryServiceQualificationCreateEvent [Optional].
        priority: The priority of this QueryServiceQualificationCreateEvent [Optional].
        time_ocurred: The time_ocurred of this QueryServiceQualificationCreateEvent [Optional].
    """

    event: Optional[QueryServiceQualificationCreateEventPayload] = None
    event_id: Optional[str] = None
    event_time: Optional[datetime] = None
    event_type: Optional[str] = None
    correlation_id: Optional[str] = None
    domain: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    time_ocurred: Optional[datetime] = None


QueryServiceQualificationCreateEvent.update_forward_refs()
