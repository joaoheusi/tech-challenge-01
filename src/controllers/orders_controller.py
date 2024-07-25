from src.config.injector.container import container
from src.entities.order import Order
from src.entities.payment import Payment
from src.types.dtos.create_order_dto import CreateOrderDto
from src.types.dtos.get_orders_filters_dto import GetOrdersFiltersDto
from src.use_cases.orders.create_order import CreateOrderUseCase
from src.use_cases.orders.get_ongoing_orders_use_case import GetOngoingOrdersUseCase
from src.use_cases.orders.get_order import GetOrderUseCase
from src.use_cases.orders.get_order_paymnent import GetOrderPaymentUseCase
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

    @staticmethod
    async def get_order_payment(order_id: str) -> Payment:
        get_order_payment_use_case = container.get(GetOrderPaymentUseCase)
        result = await get_order_payment_use_case.execute(order_id)
        return result

    @staticmethod
    async def get_order(order_id: str) -> Order:
        get_order_use_case = container.get(GetOrderUseCase)
        result = await get_order_use_case.execute(order_id)
        return result

    @staticmethod
    async def get_ongoing_orders() -> list[Order]:
        get_ongoing_orders_use_case = container.get(GetOngoingOrdersUseCase)
        result = await get_ongoing_orders_use_case.execute()
        return result
