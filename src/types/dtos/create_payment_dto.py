from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field

from src.types.enums.payment_status_enum import PaymentStatusEnum


class CreatePaymentDto(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    externalId: str
    paymentLink: str
    status: PaymentStatusEnum
