from injector import inject

from src.entities.order import Order
from src.interfaces.repositories.orders_repository import OrdersRepository


class GetOngoingOrdersUseCase:
    @inject
    def __init__(self, orders_repository: OrdersRepository):
        self.orders_repository = orders_repository

    async def execute(self) -> list[Order]:
        ongoing_orders = await self.orders_repository.get_ongoing_orders()
        return ongoing_orders
