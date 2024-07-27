from pydantic import BaseModel

from src.types.dtos.payment_updated_notification_data_dto import (
    PaymentUpdatedNotificationDataDto,
)
from src.types.enums.notification_category import NotificationCategoryEnum


class GenericNotificationDataDto(BaseModel):
    action: NotificationCategoryEnum
    data: PaymentUpdatedNotificationDataDto
