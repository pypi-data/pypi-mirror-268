import logging
from typing import Callable

from kucoin_futures.client import WsToken, User, Trade, Market

from kucoin_futures_lib.kucoinf import KucoinFutures
from kucoin_futures_lib.market import KucoinFuturesMarket
from kucoin_futures_lib.trade import KucoinFuturesTrade
from kucoin_futures_lib.user import KucoinFuturesUser
from kucoin_futures_lib.websocket import KucoinFuturesWebsocket

logger = logging.getLogger(__name__)


def initialize_kucoinf(
    api_key: str, api_secret: str, api_passphrase: str, retriable: Callable = None
) -> KucoinFutures:
    """Initialize the Kucoin Futures client using API credentials."""
    user = initialize_user(api_key, api_secret, api_passphrase, retriable)
    trade = initialize_trade(api_key, api_secret, api_passphrase, retriable)
    market = initialize_market(api_key, api_secret, api_passphrase, retriable)
    websocket = initialize_websocket(api_key, api_secret, api_passphrase, retriable)
    kucoinf = KucoinFutures(user=user, trade=trade, market=market, websocket=websocket)
    logger.info("Kucoin Futures client initialized.")
    return kucoinf


def initialize_user(
    api_key: str, api_secret: str, api_passphrase: str, retriable: Callable = None
) -> "KucoinFuturesUser":
    """Initialize the Kucoin Futures User client using API credentials."""
    user = User(key=api_key, secret=api_secret, passphrase=api_passphrase)
    return KucoinFuturesUser(client=user, retriable=retriable)


def initialize_market(
    api_key: str, api_secret: str, api_passphrase: str, retriable: Callable = None
) -> KucoinFuturesMarket:
    """Initialize the Kucoin Futures Market client using API credentials."""
    market = Market(key=api_key, secret=api_secret, passphrase=api_passphrase)
    return KucoinFuturesMarket(client=market, retriable=retriable)


def initialize_trade(
    api_key: str, api_secret: str, api_passphrase: str, retriable: Callable = None
) -> KucoinFuturesTrade:
    """Initialize the Kucoin Futures Trade client using API credentials."""
    trade = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase)
    return KucoinFuturesTrade(client=trade, retriable=retriable)


def initialize_websocket(
    api_key: str,
    api_secret: str,
    api_passphrase: str,
    url="https://api-futures.kucoin.com",
) -> KucoinFuturesWebsocket:
    """Initialize the Kucoin Futures Websocket client using API credentials."""
    token = WsToken(
        key=api_key,
        secret=api_secret,
        passphrase=api_passphrase,
        url=url,
    )
    return KucoinFuturesWebsocket(token=token)
