# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import secrets
import string
from typing import List, Optional

from elements import Amount, Header, Item


def get_example_sale_amount(original_amount_value: int) -> Amount:
    return Amount(value=original_amount_value - 200)


def get_example_tax_amount() -> Amount:
    return Amount(value=100)


def get_example_shipping_amount() -> Amount:
    return Amount(value=100)


def get_example_discount_amount() -> Amount:
    return Amount(value=200)


def get_example_items(number: int, includes_sale_amount: bool) -> List[Item]:
    return [
        Item(
            name=f"Product {i+1}",
            amount=Amount(value=1000 * (i + 1)),
            quantity=i + 1,
            sale_amount=(
                get_example_sale_amount(1000 * (i + 1))
                if includes_sale_amount
                else None
            ),
        )
        for i in range(number)
    ]


def get_header(
    header_text: Optional[str] = None, header_image_link: Optional[str] = None
) -> Optional[Header]:
    if not header_text and not header_image_link:
        return None
    return (
        Header(type="text", text=header_text)
        if header_text
        else Header(type="image", image_link=header_image_link)
    )


def generate_reference_id() -> str:
    """
    Generate a reference ID for the order_details message
    Use whatever algorithm your'd like, but it should be unique
    """
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(32))
