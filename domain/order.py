from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import List

from .product import Product, Money


class Order():
    _order_no: OrderNo
    _order_lines: List[OrderLine]
    _shipping_info: ShippingInfo
    _state: OrderState

    def __init__(
            self, order_lines: List[OrderLine], shipping_info: ShippingInfo,
            state: OrderState = None,
            ) -> None:
        if not state:
            state = OrderState.PAYMENT_WAITING

        self.validate_order_lines(order_lines)
        self.validate_shipping_info(shipping_info)

        self._order_no = OrderNo()
        self._order_lines = order_lines
        self._shipping_info = shipping_info
        self._state = state

    @property
    def state(self) -> OrderState:
        return self._state

    @property
    def shipping_info(self) -> ShippingInfo:
        return self._shipping_info

    def validate_order_lines(self, order_lines: List[OrderLine]) -> None:
        if len(order_lines) == 0:
            raise ValueError('Order must have more than one OrderLine')

    def validate_shipping_info(self, shipping_info: ShippingInfo) -> None:
        if shipping_info is None:
            raise ValueError('Order must have not None ShippingInfo')

    @property
    def total_amount(self) -> Money:
        _total_amount = Money(0)
        for line in self._order_lines:
            _total_amount += line.amount

        return _total_amount

    def change_shipping_info(self, shipping_info: ShippingInfo) -> None:
        if not self._state.is_before_shipped():
            raise ValueError(
                    f'cannot change shipping info because the state\
                    {self.state} is not before shipped')

        self.validate_shipping_info(shipping_info)
        self._shipping_info = shipping_info

    def change_shipped(self) -> None:
        self._state = OrderState.SHIPPED

    def payment(self) -> None:
        pass

    def cancel(self) -> None:
        if not self._state.is_before_shipped():
            raise ValueError(
                    f'cannot cancel order because the state {self.state}\
                    is not before shipped')

        self._state = OrderState.CANCELED


@dataclass
class OrderNo():
    _no: str

    def __init__(self) -> None:
        pass


class OrderState(Enum):
    PAYMENT_WAITING = auto()
    PREPARING = auto()
    SHIPPED = auto()
    DELIVERING = auto()
    DELIVERY_COMPLETE = auto()
    CANCELED = auto()

    def is_before_shipped(self) -> bool:
        if self in (self.PAYMENT_WAITING, self.PREPARING):
            return True

        return False


class OrderLine():
    _product: Product
    _quantity: int

    def __init__(self, product: Product, quantity: int) -> None:
        self._product = product
        self._quantity = quantity

    @property
    def amount(self) -> Money:
        price: Money = self._product.price

        return price * self._quantity


@dataclass
class ShippingInfo():
    _receiver: Receiver
    _address: Address


@dataclass
class Receiver():
    _name: str
    _phone_number: str


@dataclass
class Address():
    _address1: str
    _address2: str
    _zipcode: str
