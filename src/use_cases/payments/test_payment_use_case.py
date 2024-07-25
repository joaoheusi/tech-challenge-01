from injector import inject

from src.interfaces.providers.payments_provider import PaymentsProvider
from src.types.dtos.external_payment_data_dto import ExternalPaymentDataDto


class TestPaymentUseCase:
    @inject
    def __init__(self, payment_provider: PaymentsProvider):
        self.payment_provider = payment_provider

    async def execute(self, order_id: str, amount: float) -> ExternalPaymentDataDto:
        payment = await self.payment_provider.create_payment(
            order_id=order_id, amount=amount, products=["jubileu"]
        )
        return payment
