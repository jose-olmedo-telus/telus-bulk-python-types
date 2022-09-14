# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel
from pydantic import AnyUrl, Field  # noqa: F401


class RelatedParty(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RelatedParty - a model defined in OpenAPI

        id: The id of this RelatedParty.
        href: The href of this RelatedParty [Optional].
        name: The name of this RelatedParty [Optional].
        role: The role of this RelatedParty [Optional].
        base_type: The base_type of this RelatedParty [Optional].
        schema_location: The schema_location of this RelatedParty [Optional].
        type: The type of this RelatedParty [Optional].
        referred_type: The referred_type of this RelatedParty.
    """

    id: str
    href: Optional[AnyUrl] = None
    name: Optional[str] = None
    role: Optional[str] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias='@type')
    referred_type: str = Field(..., alias='@referredType')


RelatedParty.update_forward_refs()
