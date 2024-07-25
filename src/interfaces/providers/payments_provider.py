from abc import ABC, abstractmethod

from src.types.dtos.external_payment_data_dto import ExternalPaymentDataDto


class PaymentsProvider(ABC):
    @abstractmethod
    async def create_payment(
        self, order_id: str, amount: float, products: list[str]
    ) -> ExternalPaymentDataDto:
        raise NotImplementedError

    async def get_payment(self, external_payment_id: str) -> ExternalPaymentDataDto:
        raise NotImplementedError
