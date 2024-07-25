from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from src.controllers.orders_controller import OrdersUseCasesController
from src.entities.order import Order
from src.entities.payment import Payment
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


@orders_router.get("/{order_id}/payment", response_model=Payment)
async def get_order_payment(order_id: str) -> Payment:
    payment = await OrdersUseCasesController.get_order_payment(order_id=order_id)
    return payment

@orders_router.post("/{order_id}/ready", response_model=Order)
async def ready_order(order_id: str) -> Order:
    order = await OrdersUseCasesController.ready_order(order_id=order_id)
    return order

@orders_router.post("/{order_id}/complete", response_model=Order)
async def complete_order(order_id: str) -> Order:
    order = await OrdersUseCasesController.complete_order(order_id=order_id)
    return order


@orders_router.get("/ongoing", response_model=list[Order])
async def get_ongoing_orders() -> list[Order]:
    ongoing_orders = await OrdersUseCasesController.get_ongoing_orders()
    return ongoing_orders


@orders_router.get("/{order_id}", response_model=Order)
async def get_order(order_id: str) -> Order:
    payment = await OrdersUseCasesController.get_order(order_id=order_id)
    return payment
