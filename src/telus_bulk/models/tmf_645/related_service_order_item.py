# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel
from pydantic import AnyUrl, Field

from telus_bulk.models.tmf_645.order_item_action_type import OrderItemActionType


class RelatedServiceOrderItem(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RelatedServiceOrderItem - a model defined in OpenAPI

        item_id: The item_id of this RelatedServiceOrderItem.
        role: The role of this RelatedServiceOrderItem [Optional].
        service_order_href: The service_order_href of this RelatedServiceOrderItem [Optional].
        service_order_id: The service_order_id of this RelatedServiceOrderItem.
        item_action: The item_action of this RelatedServiceOrderItem [Optional].
        base_type: The base_type of this RelatedServiceOrderItem [Optional].
        schema_location: The schema_location of this RelatedServiceOrderItem [Optional].
        type: The type of this RelatedServiceOrderItem [Optional].
        referred_type: The referred_type of this RelatedServiceOrderItem [Optional].
    """

    item_id: str
    role: Optional[str] = None
    service_order_href: Optional[str] = None
    service_order_id: str
    item_action: Optional[OrderItemActionType] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias="@type")
    referred_type: Optional[str] = Field(default=None, alias="@referredType")


RelatedServiceOrderItem.update_forward_refs()
