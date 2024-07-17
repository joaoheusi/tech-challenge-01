from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from src.controllers.orders_controller import OrdersUseCasesController
from src.entities.order import Order
from src.types.dtos.create_order_dto import CreateOrderDto
from src.types.dtos.get_orders_filters_dto import GetOrdersFiltersDto

orders_router = APIRouter(prefix="/orders", tags=["orders"])


@orders_router.get("", response_model=list[Order])
async def get_orders(
    filters: Annotated[GetOrdersFiltersDto, Depends()],
) -> list[Order]:
    orders = await OrdersUseCasesController.get_orders(filters=filters)
    return orders


@orders_router.post("", response_model=Order)
async def create_order(order: CreateOrderDto) -> Order:
    created_order = await OrdersUseCasesController.create_order(order=order)
    return created_order
