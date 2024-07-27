from pydantic import BaseModel


class PaymentUpdatedNotificationDataDto(BaseModel):
    id: str
