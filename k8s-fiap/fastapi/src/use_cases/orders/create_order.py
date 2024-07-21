from datetime import datetime, timedelta, timezone

from injector import inject

from src.entities.order import Order
from src.excecptions.application_exceptions import ApplicationExceptions
from src.interfaces.repositories.orders_repository import OrdersRepository
from src.interfaces.repositories.products_repository import ProductsRepository
from src.types.dtos.create_order_dto import CreateOrderDto
from src.types.dtos.get_orders_filters_dto import GetOrdersFiltersDto
from src.types.dtos.patch_product_dto import PatchProductDto
from src.types.enums.order_status_enum import OrderStatusEnum
from src.types.order_item import OrderItem


class CreateOrderUseCase:
    @inject
    def __init__(
        self,
        orders_repository: OrdersRepository,
        products_repository: ProductsRepository,
    ):
        self.orders_repository = orders_repository
        self.products_repository = products_repository

    async def execute(self, order: CreateOrderDto) -> Order:
        products_ids = [preItem.productId for preItem in order.preItems]
        products = await self.products_repository.find_product_by_list_of_ids(
            products_ids
        )
        order_items: list[OrderItem] = []
        for preItem in order.preItems:
            product = next(
                (product for product in products if product.id == preItem.productId),
                None,
            )
            if not product:
                raise ApplicationExceptions.resource_not_found(
                    resource_name="Product",
                    identifier=["id"],
                    identifier_value=preItem.productId,
                )
            if not product.isActive:
                raise ApplicationExceptions.product_inactive(
                    product_id=product.id,
                )
            if product.availableAmount < preItem.quantity:
                raise ApplicationExceptions.product_not_available(
                    product_id=product.id,
                    requested_quantity=preItem.quantity,
                    available_quantity=product.availableAmount,
                )
            product.availableAmount -= preItem.quantity

            order_items.append(
                OrderItem(
                    productId=product.id,
                    productLabel=product.label,
                    quantity=preItem.quantity,
                    unitaryPrice=product.price,
                )
            )

        for product in products:
            await self.products_repository.update_product(
                product.id, PatchProductDto(**product.model_dump())
            )

        totalPrice = sum([item.quantity * item.unitaryPrice for item in order_items])

        orders_being_prepared = await self.orders_repository.get_orders(
            filters=GetOrdersFiltersDto(status=OrderStatusEnum.PREPARING)
        )

        # If this grows to a more complex logic, we should move it to a service
        estimated_time_minutes_to_ready = 10

        if orders_being_prepared:
            estimated_time_minutes_to_ready += len(orders_being_prepared) * 5

        estimated_time_to_ready = datetime.now(timezone.utc) + timedelta(
            minutes=estimated_time_minutes_to_ready
        )

        order_to_create = Order(
            items=order_items,
            status=OrderStatusEnum.RECEIVED,
            totalPrice=totalPrice,
            customerId=order.customerId,
            estimatedTimeToReady=estimated_time_to_ready,
        )

        created_order = await self.orders_repository.create_order(order=order_to_create)

        return created_order
