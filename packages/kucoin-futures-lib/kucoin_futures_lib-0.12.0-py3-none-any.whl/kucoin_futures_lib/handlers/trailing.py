"""Trailing stop loss handler."""

import asyncio
import logging
from typing import Dict, Callable, Any, Awaitable, Literal

from kucoin_futures_lib.handlers.base import HandlerABC

logger = logging.getLogger(__name__)


class TrailingHandler(HandlerABC):
    """Handler that moves the stop loss price based on the trailing stop loss strategy."""

    def __init__(
        self,
        instrument: str,
        direction: Literal["buy", "sell"],
        sl_order_id: str,
        sl_order_price: float,
        trailing_distance: float,
        trailing_step: float,
        handler: HandlerABC,
        update_order: Callable[[Any], Awaitable[None]],
    ):
        """Initialize the handler.
        :param instrument: instrument symbol
        :param direction: buy or sell
        :param sl_order_id: Stop loss order ID
        :param sl_order_price: Stop loss order stop price
        :param trailing_distance: Distance from the mark price to the stop loss order price.
        When distance is exceeded the stop loss order price is updated
        :param update_order: Function to update the stop loss order price
        :param trailing_step: The step to adjust the stop loss order price by.
        When None, the delta between distance and trailing distance is used.
        """
        self.instrument = instrument
        self.direction = direction
        self.sl_order_id = sl_order_id
        self.sl_order_price = sl_order_price
        self.trailing_distance = trailing_distance
        self.trailing_step = trailing_step
        self.update_order = update_order
        self.external_handler = handler
        self._done = asyncio.Event()
        self._topic = "/contract/instrument"

    def __repr__(self):
        return f"TrailingHandler({self.instrument}, sl_order_id={self.sl_order_id}, trailing_distance={self.trailing_distance}, trailing_step={self.trailing_step})"

    @property
    def topic(self) -> str:
        """Return the topic supported by the handler."""
        return f"{self._topic}:{self.instrument}"

    @property
    def private(self) -> bool:
        return False

    @property
    def done(self) -> asyncio.Event:
        return self._done

    def _calculate_distance(self, mark_price: float) -> float:
        """Calculate the distance between the mark price and the stop loss order price."""
        return abs(mark_price - self.sl_order_price)

    def calculate_new_price(self, mark_price: float):
        """Calculate the new order price based on direction and either dynamic or fixed step."""
        distance = self._calculate_distance(mark_price)
        if distance > self.trailing_distance:
            excess = distance - self.trailing_distance
            adjustment = excess + self.trailing_step
            return (
                self.sl_order_price + adjustment
                if self.direction == "buy"
                else self.sl_order_price - adjustment
            )

    async def handle(self, msg: Dict):
        if self._done.is_set():
            return

        if self.external_handler.done.is_set():
            self._done.set()
            return

        if msg["subject"] == "mark.index.price":
            mark_price = msg["data"]["markPrice"]
            new_price = self.calculate_new_price(mark_price)
            if new_price:
                self.sl_order_price = new_price
                await self.update_order(self.sl_order_price)
                logger.info(
                    "Trailing stop loss for %s updated to %s",
                    self.instrument,
                    self.sl_order_price,
                )
