from pydantic import BaseModel

from src.types.enums.payment_status_enum import PaymentStatusEnum


class ExternalPaymentDataDto(BaseModel):
    externalId: str
    paymentLink: str
    amount: float
    status: PaymentStatusEnum
