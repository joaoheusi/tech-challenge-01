from injector import inject

from src.core.domain.dtos.orders.get_orders_filters_dto import GetOrdersFiltersDto
from src.core.domain.models.order import Order
from src.core.domain.repositories.orders_port import OrdersPort


class GetOrdersUseCase:
    @inject
    def __init__(self, orders_repository: OrdersPort):
        self.orders_repository = orders_repository

    async def execute(self, filters: GetOrdersFiltersDto) -> list[Order]:
        return await self.orders_repository.get_orders(filters)
