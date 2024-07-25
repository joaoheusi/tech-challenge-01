from src.config.injector.container import container
from src.types.dtos.external_payment_data_dto import ExternalPaymentDataDto
from src.use_cases.payments.test_payment_use_case import TestPaymentUseCase


class PaymentsController:

    @staticmethod
    async def create_payment(
        payment_id: str, payment_amount: float
    ) -> ExternalPaymentDataDto:
        create_payment_use_case = container.get(TestPaymentUseCase)
        result = await create_payment_use_case.execute(
            order_id=payment_id, amount=payment_amount
        )
        return result
