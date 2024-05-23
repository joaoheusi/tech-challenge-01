from abc import ABC, abstractmethod

from src.core.domain.dtos.orders.get_orders_filters_dto import GetOrdersFiltersDto
from src.core.domain.models.order import Order


class OrdersPort(ABC):

    @abstractmethod
    async def create_order(self, order: Order) -> Order:
        raise NotImplementedError

    @abstractmethod
    async def get_order_by_id(self, order_id: str) -> Order | None:
        raise NotImplementedError

    @abstractmethod
    async def get_orders(self, filters: GetOrdersFiltersDto) -> list[Order]:
        raise NotImplementedError
