from src.adapters.repositories.beanie.documents.order_document import OrderDocument
from src.core.domain.dtos.orders.get_orders_filters_dto import GetOrdersFiltersDto
from src.core.domain.models.order import Order
from src.core.domain.repositories.orders_port import OrdersPort


class BeanieOrdersRepository(OrdersPort):

    async def create_order(self, order: Order) -> Order:
        order_to_create = OrderDocument(**order.model_dump())
        await order_to_create.insert()
        return order_to_create

    async def get_order_by_id(self, order_id: str) -> Order | None:
        order = await OrderDocument.find_one(OrderDocument.id == order_id).project(
            Order
        )
        if not order:
            return None
        return order

    async def get_orders(self, filters: GetOrdersFiltersDto) -> list[Order]:
        search_filters = []
        if filters is not None:
            if filters.status is not None:
                search_filters.append(OrderDocument.status == filters.status)
            if filters.customerId is not None:
                search_filters.append(OrderDocument.customerId == filters.customerId)
        orders = await OrderDocument.find(*search_filters).project(Order).to_list()
        return orders
