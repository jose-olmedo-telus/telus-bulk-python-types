# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401
from pydantic import AnyUrl, Field

from telus_bulk.models.tmf_645.time_period import TimePeriod


class FeatureRelationship(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FeatureRelationship - a model defined in OpenAPI

        id: The id of this FeatureRelationship [Optional].
        name: The name of this FeatureRelationship.
        relationship_type: The relationship_type of this FeatureRelationship.
        valid_for: The valid_for of this FeatureRelationship [Optional].
        base_type: The base_type of this FeatureRelationship [Optional].
        schema_location: The schema_location of this FeatureRelationship [Optional].
        type: The type of this FeatureRelationship [Optional].
    """

    id: Optional[str] = None
    name: str
    relationship_type: str
    valid_for: Optional[TimePeriod] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias="@type")


FeatureRelationship.update_forward_refs()
