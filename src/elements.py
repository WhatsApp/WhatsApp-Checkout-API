# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import json
from dataclasses import dataclass
from typing import Optional

VALUE_OFFSET = 100


@dataclass
class Header:
    type: str
    text: Optional[str] = None
    image_link: Optional[str] = None


class Amount:
    """
    Amount object used to represent the amount in Payments, conventionally we
    don't use floating point numbers, so we use integer and an offset to represent
    the amount. Eg, For example, ₹12.34 has value 1234 and offset 100.
    """

    def __init__(self, value: int, offset: int = VALUE_OFFSET) -> None:
        if offset != VALUE_OFFSET:
            raise ValueError(f"Offset must be {VALUE_OFFSET}")
        if value % VALUE_OFFSET != 0:
            raise ValueError(f"Value must be a multiple of {VALUE_OFFSET}")
        self.value = value
        self.offset = offset

    def toJSON(self) -> str:
        return json.dumps({"value": self.value, "offset": self.offset})


@dataclass
class Address:
    """
    Address used in Payments
    """

    address_line1: str
    city: str
    zone_code: str
    postal_code: str
    country_code: str
    address_line2: Optional[str] = None


@dataclass
class Item:
    """
    Item object used to represent the items in an order.
    """

    name: str
    amount: Amount
    quantity: int
    sale_amount: Optional[Amount] = None
    retailer_id: Optional[str] = None
    image_link: Optional[str] = None
    country_of_origin: Optional[str] = None
    importer_name: Optional[str] = None
    importer_address: Optional[Address] = None
