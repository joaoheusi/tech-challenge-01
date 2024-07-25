
from injector import inject

from src.entities.order import Order
from src.excecptions.application_exceptions import ApplicationExceptions
from src.interfaces.repositories.orders_repository import OrdersRepository
from src.types.enums.order_status_enum import OrderStatusEnum


class CompleteOrderUseCase:
    @inject
    def __init__(self, orders_repository: OrdersRepository):
        self.orders_repository = orders_repository

    async def execute(self, order_id: str) -> Order:
        order = await self.orders_repository.get_order_by_id(order_id)
        if not order:
            raise ApplicationExceptions.resource_not_found(
                resource_name='Order', identifier=['id'], identifier_value=order_id
            )
        if not order.status == OrderStatusEnum.READY:
            raise ApplicationExceptions.invalid_order_operation()
        order.status = OrderStatusEnum.COMPLETED
        await self.orders_repository.update_order(order)
        return order