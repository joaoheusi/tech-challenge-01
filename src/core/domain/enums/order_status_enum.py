from enum import Enum


class OrderStatusEnum(str, Enum):
    CREATED = "CREATED"
    CONFIRMED = "CONFIRMED"
    FINISHED = "FINISHED"
    DELIVERED = "DELIVERED"
