"""Handler that listens for the status of an order."""
import asyncio
import logging
from typing import Dict, List, Literal, Optional

from kucoin_futures_lib.handlers.base import HandlerABC

logger = logging.getLogger(__name__)


class MessageHandler(HandlerABC):
    def __init__(
        self,
        order_id: str,
        order_status: Optional[Literal["match", "open", "done"]] = None,
        message_type: Optional[
            List[Literal["open", "match", "filled", "canceled", "update"]]
        ] = None,
    ):
        """The handler will stop listening when any of the message_type is received and order_status is received.
        If both order_status and message_type are None, the handler will react to the first message received for the order.
        :param order_id: The order ID to listen for.
        :param message_type: The message type to listen for. Default is None."""

        self.order_id = order_id
        self.message_type = message_type
        self.order_status = order_status
        self.received_message = None
        self._reached = asyncio.Event()
        self._topic = "/contractMarket/tradeOrders"

    def __repr__(self):
        return f"MessageHandler(order_id='{self.order_id}', order_status={self.order_status}, message_type={self.message_type})"

    @property
    def topic(self) -> str:
        """Return the topic supported by the handler."""
        return f"{self._topic}"

    @property
    def private(self) -> bool:
        """Return the privacy status for the topic."""
        return True

    @property
    def done(self) -> asyncio.Event:
        """Return the done status for the handler."""
        return self._reached

    async def handle(self, msg: Dict):
        """Handle the trade order message from
        :param msg: The trade order message.
        https://www.kucoin.com/docs/websocket/futures-trading/private-channels/trade-orders
        """
        if self._reached.is_set():
            return

        trade_order = msg.get("data", {})
        trade_order_id = trade_order.get("orderId", "")
        message_type = trade_order.get("type", "")
        status = trade_order.get("status", "")

        if trade_order_id == self.order_id:
            status_match = self.order_status is None or status in self.order_status
            message_match = (
                self.message_type is None or message_type in self.message_type
            )
            if status_match and message_match:
                logger.info(
                    "Handler done for order %s. Message type: %s, order status: %s",
                    trade_order_id,
                    message_type,
                    status
                )
                self.received_message = msg
                self._reached.set()
