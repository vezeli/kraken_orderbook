from statistics import mean
from typing import Callable

from pandas import concat, DataFrame, Series

OrderBook = Series
OrderBookFactory = Callable[[str], OrderBook]


def reverse(s: Series) -> Series:
    """Returns reversed series."""
    return s.iloc[::-1]


def _orderbook_factory(data: dict, ccypair: str) -> OrderBookFactory:
    """Factory for creating orderbook sides."""
    _response_root = "result"
    _response_fields = ("price", "volume", "unixtime")
    return lambda orderbook_side: (
        DataFrame(
            data=data[_response_root][ccypair][orderbook_side], columns=_response_fields
        )
        .drop(columns="unixtime")
        .set_index("price")
        .squeeze()
        .astype(float)
        .cumsum()
    )


def _build(f: OrderBookFactory) -> OrderBook:
    """Builds an orderbook from `OrderBookFactory`."""
    ser = concat(
        [
            f("asks").pipe(reverse),
            f("bids"),
        ], axis = 0

    )
    ser.index = ser.index.astype(float)
    return ser


def mid_price(f: OrderBookFactory) -> float:
    """Calculates mid price from `OrderBookFactory`."""
    best_ask, best_bid = f("asks").index.astype(float).min(), f("bids").index.astype(float).max()
    return mean([best_ask, best_bid])


def build_orderbook(data: dict, ccypair: str) -> OrderBook:
    return _build(_orderbook_factory(data=data, ccypair=ccypair))


def _scale(orderbook: OrderBook, mid_price: float) -> OrderBook:
    """Scales the price axis in `OrderBook`."""
    orderbook.index = orderbook.index/mid_price
    return orderbook


def build_scaled_orderbook(data: dict, ccypair: str) -> OrderBook:
    of = _orderbook_factory(data=data, ccypair=ccypair)
    return _scale(orderbook=_build(of), mid_price=mid_price(of))
