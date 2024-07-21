from enum import Enum


class OrderStatusEnum(str, Enum):
    RECEIVED = "RECEIVED"
    PREPARING = "PREPARING"
    READY = "READY"
    COMPLETED = "COMPLETED"
