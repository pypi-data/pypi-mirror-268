import logging
import time
from typing import Callable, Any, Tuple, Type, Optional

logger = logging.getLogger(__name__)


def retry(
    func: Callable[[], Any],
    retries: int,
    backoff_base: float = 2.0,
    initial_backoff: float = 0.1,  # Initial backoff time for the first retry
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Optional[Any]:
    """
    Calls a function with retries on exception, with configurable exponential backoff, using logging for output.
    :param func: The function to call.
    :param exceptions: A tuple of Exceptions to catch.
    :param retries: The number of retries to attempt.
    :param initial_backoff: The initial delay before the first retry.
    :param backoff_base: The base of the exponential backoff. Default is 2.
    :return: The result of the function call on success, None if retries exhausted.
    """
    for attempt in range(retries):
        try:
            return func()
        except exceptions as e:
            logger.error(
                "Attempt %d failed with error: %s", attempt + 1, e, exc_info=True
            )
            if attempt < retries - 1:  # Only sleep if there are more attempts left
                sleep_time = initial_backoff * (backoff_base ** attempt)  # Adjusted formula for initial delay
                logger.info("Waiting %s seconds before retrying...", sleep_time)
                time.sleep(sleep_time)
    return None


def retriable(
    retries: int,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    backoff_base: float = 1.5,  # Keep adjustable base for granularity in backoff timing
    initial_backoff: float = 0.1  # Initial backoff time for the first retry
) -> Callable:
    """
    A decorator factory for retrying a function call with configurable exponential backoff on specified exceptions.
    Allows for sub-second retries right from the first failure with more control over the backoff timing.
    :param retries: The number of retries to attempt.
    :param exceptions: A tuple of Exceptions to catch.
    :param backoff_base: The base of the exponential backoff, can be adjusted for finer control.
    :param initial_backoff: The initial delay before the first retry.
    :return: Decorator for the function.
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Optional[Any]:
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.error(
                        "Attempt %d failed with error: %s", attempt + 1, e, exc_info=True
                    )
                    if attempt < retries - 1:  # Only sleep if there are more attempts left
                        sleep_time = initial_backoff * (backoff_base ** attempt)  # Adjusted formula for initial delay
                        logger.info("Waiting %s seconds before retrying...", sleep_time)
                        time.sleep(sleep_time)
            return None

        return wrapper

    return decorator