# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401

from telus_bulk.models.tmf_645.check_service_qualification import (
    CheckServiceQualification,
)


class CheckServiceQualificationCreateEventPayload(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CheckServiceQualificationCreateEventPayload - a model defined in OpenAPI

        check_service_qualification: The check_service_qualification of this CheckServiceQualificationCreateEventPayload [Optional].
    """

    check_service_qualification: Optional[CheckServiceQualification] = None


CheckServiceQualificationCreateEventPayload.update_forward_refs()
