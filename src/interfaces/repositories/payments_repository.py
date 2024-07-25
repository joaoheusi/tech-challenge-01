from abc import ABC, abstractmethod

from src.entities.payment import Payment
from src.types.dtos.create_payment_dto import CreatePaymentDto


class PaymentsRepository(ABC):

    @abstractmethod
    async def create_payment(self, payment: CreatePaymentDto) -> Payment:
        raise NotImplementedError

    @abstractmethod
    async def get_payment_by_id(self, payment_id: str) -> Payment | None:
        raise NotImplementedError

    @abstractmethod
    async def get_payment_by_external_id(
        self, external_payment_id: str
    ) -> Payment | None:
        raise NotImplementedError

    @abstractmethod
    async def update_payment(self, payment: Payment) -> Payment | None:
        raise NotImplementedError
