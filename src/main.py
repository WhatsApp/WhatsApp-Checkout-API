# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import argparse

from example_base import ExampleBase
from example_util import (
    generate_reference_id,
    get_example_discount_amount,
    get_example_items,
    get_example_shipping_amount,
    get_example_tax_amount,
    get_header,
)
from stubs import get_test_recipient_phone_number, get_test_sender_phone_number


# def send_order_details_msg() -> None:
def main() -> None:
    """Send the details of an order to a customer"""
    parser = argparse.ArgumentParser(
        prog="checkout-api-example",
        description="Demonstrate the Checkout API usage",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("--goods_type", nargs=1)
    parser.add_argument("--msg_body", nargs=1)
    parser.add_argument("--item_number", nargs=1, type=int)
    parser.add_argument("--tax_desc")
    parser.add_argument("--include_sale_amount", action="store_true")
    parser.add_argument("--include_shipping_value", action="store_true")
    parser.add_argument("--shipping_desc")
    parser.add_argument("--include_discount_value", action="store_true")
    parser.add_argument("--discount_desc")
    parser.add_argument("--discount_program_name")
    parser.add_argument("--catalog_id")
    parser.add_argument("--header_text")
    parser.add_argument("--header_image_link")
    parser.add_argument("--footer_text")
    parser.add_argument("--expiration_in_sec")
    parser.add_argument("--expiration_desc")
    args = parser.parse_args()

    reference_id = generate_reference_id()

    example_base = ExampleBase()
    example_base.send_order_details_msg(
        goods_type=args.goods_type[0],
        sender_phone_number=get_test_sender_phone_number(),
        recipient_phone_number=get_test_recipient_phone_number(),
        reference_id=reference_id,
        msg_body=args.msg_body[0],
        items=get_example_items(args.item_number[0], args.include_sale_amount),
        tax_amount=get_example_tax_amount(),
        tax_desc=args.tax_desc,
        shipping_amount=(
            get_example_shipping_amount() if args.include_shipping_value else None
        ),
        shipping_desc=args.shipping_desc,
        discount_amount=(
            get_example_discount_amount() if args.include_discount_value else None
        ),
        discount_desc=args.discount_desc,
        discount_program_name=args.discount_program_name,
        catalog_id=args.catalog_id,
        msg_header=get_header(args.header_text, args.header_image_link),
        msg_footer=args.footer_text,
        expiration_in_sec=args.expiration_in_sec,
        expiration_desc=args.expiration_desc,
    )
    example_base.send_order_status_msg(
        sender_phone_number=get_test_sender_phone_number(),
        recipient_phone_number=get_test_recipient_phone_number(),
        reference_id=reference_id,
        msg_body="Order Status Update",
        status="processing",
    )
    example_base.get_payment_status(get_test_sender_phone_number(), reference_id)


if __name__ == "__main__":
    main()
