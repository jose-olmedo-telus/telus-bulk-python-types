# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401
from pydantic import AnyUrl, Field


class TerminationError(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TerminationError - a model defined in OpenAPI

        id: The id of this TerminationError [Optional].
        value: The value of this TerminationError [Optional].
        base_type: The base_type of this TerminationError [Optional].
        schema_location: The schema_location of this TerminationError [Optional].
        type: The type of this TerminationError [Optional].
    """

    id: Optional[str] = None
    value: Optional[str] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias='@type')


TerminationError.update_forward_refs()
