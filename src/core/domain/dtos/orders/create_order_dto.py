from pydantic import BaseModel

from src.core.domain.dtos.order_pre_item import OrderPreItem


class CreateOrderDto(BaseModel):
    preItems: list[OrderPreItem]
    customerId: str | None = None
