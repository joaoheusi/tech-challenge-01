from datetime import datetime, timedelta, timezone
from uuid import uuid4

from pydantic import BaseModel, Field

from src.core.domain.dtos.order_item import OrderItem
from src.core.domain.enums.order_status_enum import OrderStatusEnum


class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    status: OrderStatusEnum
    items: list[OrderItem]
    totalPrice: float
    customerId: str | None = None
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    estimatedTimeToReady: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc) + timedelta(minutes=10)
    )
