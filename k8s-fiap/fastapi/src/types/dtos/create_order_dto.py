from pydantic import BaseModel

from src.types.order_pre_item import OrderPreItem


class CreateOrderDto(BaseModel):
    preItems: list[OrderPreItem]
    customerId: str | None = None
