from injector import inject

from src.entities.order import Order
from src.interfaces.repositories.orders_repository import OrdersRepository
from src.types.dtos.get_orders_filters_dto import GetOrdersFiltersDto


class GetOrdersUseCase:
    @inject
    def __init__(self, orders_repository: OrdersRepository):
        self.orders_repository = orders_repository

    async def execute(self, filters: GetOrdersFiltersDto) -> list[Order]:
        return await self.orders_repository.get_orders(filters)
