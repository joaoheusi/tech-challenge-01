from datetime import datetime

from pydantic import BaseModel

from src.types.dtos.payment_updated_notification_data_dto import (
    PaymentUpdatedNotificationDataDto,
)


class PaymentUpdatedNotificationDto(BaseModel):
    action: str
    api_version: str | None = None
    data: PaymentUpdatedNotificationDataDto
    date_created: datetime | None = None
    id: int | None = None
    live_mode: bool | None = None
    type: str | None = None
    user_id: str | None = None
