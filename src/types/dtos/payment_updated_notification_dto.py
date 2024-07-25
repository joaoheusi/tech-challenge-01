from datetime import datetime

from pydantic import BaseModel


class PaymentUpdatedNotificationDataDto(BaseModel):
    id: str


class PaymentUpdatedNotificationDto(BaseModel):
    action: str
    api_version: str
    data: PaymentUpdatedNotificationDataDto
    date_created: datetime
    id: int
    live_mode: bool
    type: str
    user_id: str
