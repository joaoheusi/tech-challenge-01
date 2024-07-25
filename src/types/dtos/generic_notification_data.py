from pydantic import BaseModel

from src.types.enums.notification_category import NotificationCategoryEnum


class GenericNotificationDataDto(BaseModel):
    action: NotificationCategoryEnum
