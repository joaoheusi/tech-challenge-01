from pydantic import BaseModel

from src.types.enums.order_status_enum import OrderStatusEnum


class GetOrdersFiltersDto(BaseModel):
    status: OrderStatusEnum | None = None
    customerId: str | None = None
