# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401
from pydantic import AnyUrl, Field


class Error(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Error - a model defined in OpenAPI

        code: The code of this Error.
        reason: The reason of this Error.
        message: The message of this Error [Optional].
        status: The status of this Error [Optional].
        reference_error: The reference_error of this Error [Optional].
        base_type: The base_type of this Error [Optional].
        schema_location: The schema_location of this Error [Optional].
        type: The type of this Error [Optional].
    """

    code: str
    reason: str
    message: Optional[str] = None
    status: Optional[str] = None
    reference_error: Optional[AnyUrl] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias='@type')


Error.update_forward_refs()
