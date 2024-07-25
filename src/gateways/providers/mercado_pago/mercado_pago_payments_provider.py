# from fastapi.encoders import jsonable_encoder
from enum import Enum

from httpx import AsyncClient
from pydantic import BaseModel

from src.config.mercado_pago.config import MERCADO_PAGO_TOKEN
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


class MercadoPagoPaymentsProvider(PaymentsProvider):
    async def create_payment(
        self, order_id: str, amount: float, products: list[str]
    ) -> ExternalPaymentDataDto:
        rounded_amount = round(amount, 2)
        payment_data = {
            "transaction_amount": rounded_amount,
            "description": f"Pedido ID:{order_id} na lanchonete do Luciano. <br/> Itens {products[0]}<br/>",  # noqa
            "payment_method_id": "pix",
            "notification_url": "https://webhook.site/3380b27f-9d24-4b87-bae0-0cb2a5c2b067",  # noqa
            "payer": {
                "email": "no_customer@email.com",
                "first_name": "Test",
                "last_name": "User",
                "identification": {"type": "CPF", "number": "191191191-00"},
                "address": {
                    "zip_code": "06233-200",
                    "street_name": "Av. das Nações Unidas",
                    "street_number": "3003",
                    "neighborhood": "Bonfim",
                    "city": "Osasco",
                    "federal_unit": "SP",
                },
            },
        }
        async with AsyncClient() as client:
            response = await client.post(
                url="https://api.mercadopago.com/v1/payments",
                headers={
                    "Authorization": f"Bearer {MERCADO_PAGO_TOKEN}",
                    "X-Idempotency-Key": order_id,
                },  # noqa
                json=payment_data,
            )
            res = response.json()
            response_data = MercadoPagoPaymentResponse(**res)
            return ExternalPaymentDataDto(
                externalId=str(response_data.id),
                paymentLink=response_data.point_of_interaction.transaction_data.ticket_url,  # noqa
                amount=rounded_amount,
                status=mercado_pago_status_to_payment_status(response_data.status),
            )

    async def get_payment(self, external_payment_id: str) -> ExternalPaymentDataDto:
        async with AsyncClient() as client:
            response = await client.get(
                url=f"https://api.mercadopago.com/v1/payments/{external_payment_id}",
                headers={
                    "Authorization": f"Bearer {MERCADO_PAGO_TOKEN}",
                },
            )
            res = response.json()
            response_data = MercadoPagoPaymentResponse(**res)
            return ExternalPaymentDataDto(
                externalId=str(response_data.id),
                paymentLink=response_data.point_of_interaction.transaction_data.ticket_url,  # noqa
                amount=response_data.transaction_amount,
                status=mercado_pago_status_to_payment_status(response_data.status),
            )
