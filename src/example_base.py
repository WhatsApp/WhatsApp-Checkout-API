# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from checkout_base import CheckoutBase
from stubs import get_access_token, get_app_secret, get_payment_configuration, get_waba


class ExampleBase(CheckoutBase):
    """
    The base class for the example checkout implementation
    """

    def get_access_token(self) -> str:
        """
        Get the access token for the WABA, which can be retrieved from the
        Env variable or your dedicated secrete storage, implement your own logic
        """
        return get_access_token()

    def get_app_secret(self) -> str:
        """
        Get the app secret for the APP, which can be retrieved from the
        Env variable or your dedicated secrete storage, implement your own logic
        """
        return get_app_secret()

    def get_waba(self) -> str:
        """
        Get WhatsApp Business Account ID, implement your own logic to get it
        """
        return get_waba()

    def get_payment_configuration(self) -> str:
        """
        Get the payment configuration id for the WABA
        Implement your own logic to get the payment configuration id
        """
        return get_payment_configuration()
