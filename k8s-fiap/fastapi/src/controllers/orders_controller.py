from src.config.injector.container import container
from src.entities.order import Order
from src.types.dtos.create_order_dto import CreateOrderDto
from src.types.dtos.get_orders_filters_dto import GetOrdersFiltersDto
from src.use_cases.orders.create_order import CreateOrderUseCase
from src.use_cases.orders.get_orders import GetOrdersUseCase


class OrdersUseCasesController:

    @staticmethod
    async def create_order(order: CreateOrderDto) -> Order:
        create_order_use_case = container.get(CreateOrderUseCase)
        result = await create_order_use_case.execute(order)
        return result

    @staticmethod
    async def get_orders(filters: GetOrdersFiltersDto) -> list[Order]:
        get_orders_use_case = container.get(GetOrdersUseCase)
        result = await get_orders_use_case.execute(filters)
        return result
