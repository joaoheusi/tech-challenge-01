from datetime import datetime, timedelta, timezone
from uuid import uuid4

from pydantic import BaseModel, Field

from src.types.enums.order_status_enum import OrderStatusEnum
from src.types.order_item import OrderItem


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
