"""Kucoin Futures user module."""

import logging
from typing import Optional, Callable

from kucoin_futures.client import User

logger = logging.getLogger(__name__)


class KucoinFuturesUser:
    """Kucoin Futures user wrapper class."""

    def __init__(self, client: User = None, currency: str = "USDT", retriable: Optional[Callable] = None):
        self.client = client
        self.currency = currency
        if retriable:
            self.get_account_overview = retriable(self.get_account_overview)

    def get_account_overview(self, currency: Optional[str] = None) -> dict:
        """Get the account overview.
        :param currency: The currency to get the account overview for.
        :return: The account overview"""
        logger.debug("Getting account overview")
        currency = currency or self.currency
        return self.client.get_account_overview(currency=currency)

    def get_balance(self, currency: Optional[str] = None) -> float:
        """Get the account balance.
        :return: The account balance"""
        logger.debug("Getting account balance")
        account_overview = self.get_account_overview(currency=currency)
        return float(account_overview["availableBalance"])
