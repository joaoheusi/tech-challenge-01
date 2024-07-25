from beanie.operators import In

from src.entities.order import Order
from src.gateways.repositories.beanie.documents.order_document import OrderDocument
from src.interfaces.repositories.orders_repository import OrdersRepository
from src.types.dtos.get_orders_filters_dto import GetOrdersFiltersDto
from src.types.enums.order_status_enum import OrderStatusEnum
from src.utils.update_beanie_document_from_pydantic import (
    update_beanie_document_from_pydantic,
)


class BeanieOrdersRepository(OrdersRepository):

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

    async def update_order(self, order: Order) -> Order | None:
        order_document = await OrderDocument.find_one(OrderDocument.id == order.id)
        if not order_document:
            return None
        await update_beanie_document_from_pydantic(order_document, order)
        await order_document.save_changes()

        updated_order = await OrderDocument.find_one(
            OrderDocument.id == order.id
        ).project(Order)
        return updated_order

    async def get_order_by_payment_id(self, payment_id: str) -> Order | None:
        order = await OrderDocument.find_one(
            OrderDocument.paymentId == payment_id
        ).project(Order)
        if not order:
            return None
        return order

    async def get_ongoing_orders(self) -> list[Order]:
        orders = (
            await OrderDocument.find(
                In(  # type: ignore
                    OrderDocument.status,
                    [
                        OrderStatusEnum.RECEIVED,
                        OrderStatusEnum.PREPARING,
                        OrderStatusEnum.READY,
                    ],
                )
            )
            .aggregate(
                aggregation_pipeline=[
                    {
                        "$addFields": {
                            "statusValue": {
                                "$switch": {
                                    "branches": [
                                        {
                                            "case": {
                                                "$eq": [
                                                    "$status",
                                                    OrderStatusEnum.RECEIVED,
                                                ]
                                            },
                                            "then": 1,
                                        },
                                        {
                                            "case": {
                                                "$eq": [
                                                    "$status",
                                                    OrderStatusEnum.PREPARING,
                                                ]
                                            },
                                            "then": 2,
                                        },
                                        {
                                            "case": {
                                                "$eq": [
                                                    "$status",
                                                    OrderStatusEnum.READY,
                                                ]
                                            },
                                            "then": 3,
                                        },
                                    ]
                                }
                            }
                        }
                    },
                    {"$sort": {"statusValue": -1, "createdAt": 1}},
                ],
                projection_model=Order,
            )
            .to_list()
        )

        return orders
