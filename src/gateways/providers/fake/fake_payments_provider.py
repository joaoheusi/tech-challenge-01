from enum import Enum
from uuid import uuid4

from pydantic import BaseModel

from src.interfaces.providers.payments_provider import PaymentsProvider
from src.types.dtos.external_payment_data_dto import ExternalPaymentDataDto
from src.types.enums.payment_status_enum import PaymentStatusEnum


class MercadoPagoTransactionData(BaseModel):
    ticket_url: str


class MercadoPagoPointOfInteraction(BaseModel):
    transaction_data: MercadoPagoTransactionData


class MercadoPagoPaymentStatusEnum(str, Enum):
    pending = "pending"
    approved = "approved"


class MercadoPagoPaymentResponse(BaseModel):
    id: int
    point_of_interaction: MercadoPagoPointOfInteraction
    status: str
    transaction_amount: float


def mercado_pago_status_to_payment_status(status: str) -> PaymentStatusEnum:
    if status == MercadoPagoPaymentStatusEnum.approved:
        return PaymentStatusEnum.SUCCESSFUL
    if status == MercadoPagoPaymentStatusEnum.pending:
        return PaymentStatusEnum.PENDING
    else:
        return PaymentStatusEnum.FAILED


class FakePaymentProvider(PaymentsProvider):
    async def create_payment(
        self, order_id: str, amount: float, products: list[str]
    ) -> ExternalPaymentDataDto:

        return ExternalPaymentDataDto(
            externalId=str(uuid4()),
            paymentLink="https://fakePaymentProvider.com/payments/123456",  # noqa
            amount=round(amount, 2),
            status=mercado_pago_status_to_payment_status("pending"),
        )

    async def get_payment(self, external_payment_id: str) -> ExternalPaymentDataDto:
        return ExternalPaymentDataDto(
            externalId=str(uuid4()),
            paymentLink="https://fakePaymentProvider.com/payments/123456",  # noqa
            amount=0.0,
            status=mercado_pago_status_to_payment_status("approved"),
        )
