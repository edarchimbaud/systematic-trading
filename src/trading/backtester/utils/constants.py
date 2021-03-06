"""
Definition of the constants of the module
"""
from methodtools import lru_cache

from ..v2.data.client import Client

REMOVE_EMPTY = "remove-empty"

FUTURE_TYPE = "Future"


@lru_cache()
def get_futures():
    """
    Get the futures.
    """
    futures, _ = Client().get_tickers()
    return futures


LETTERS = ["F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z"]

LIBOR_BEFORE_2001 = 6.65125
