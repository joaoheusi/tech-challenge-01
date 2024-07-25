from abc import ABC, abstractmethod

from src.entities.order import Order
from src.types.dtos.get_orders_filters_dto import GetOrdersFiltersDto


class OrdersRepository(ABC):

    @abstractmethod
    async def create_order(self, order: Order) -> Order:
        raise NotImplementedError

    @abstractmethod
    async def get_order_by_id(self, order_id: str) -> Order | None:
        raise NotImplementedError

    @abstractmethod
    async def get_orders(self, filters: GetOrdersFiltersDto) -> list[Order]:
        raise NotImplementedError

    @abstractmethod
    async def get_order_by_payment_id(self, payment_id: str) -> Order | None:
        raise NotImplementedError

    @abstractmethod
    async def update_order(self, order: Order) -> Order | None:
        raise NotImplementedError

    @abstractmethod
    async def get_ongoing_orders(self) -> list[Order]:
        raise NotImplementedError
