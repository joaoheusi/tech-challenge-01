from enum import Enum


class PaymentStatusEnum(str, Enum):
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"
