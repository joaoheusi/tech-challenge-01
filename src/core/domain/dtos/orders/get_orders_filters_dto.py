from pydantic import BaseModel

from src.core.domain.enums.order_status_enum import OrderStatusEnum


class GetOrdersFiltersDto(BaseModel):
    status: OrderStatusEnum | None = None
    customerId: str | None = None
