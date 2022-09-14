# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401
from pydantic import AnyUrl, Field


class Extensible(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Extensible - a model defined in OpenAPI

        base_type: The base_type of this Extensible [Optional].
        schema_location: The schema_location of this Extensible [Optional].
        type: The type of this Extensible [Optional].
    """

    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias='@type')


Extensible.update_forward_refs()
