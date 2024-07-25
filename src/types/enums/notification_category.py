from enum import Enum


class NotificationCategoryEnum(str, Enum):
    PAYMENT_UPDATED = "payment.updated"
    PAYMENT_CREATED = "payment.created"
