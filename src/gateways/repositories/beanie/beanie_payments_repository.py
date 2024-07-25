from src.entities.payment import Payment
from src.gateways.repositories.beanie.documents.payment_document import PaymentDocument
from src.interfaces.repositories.payments_repository import PaymentsRepository
from src.types.dtos.create_payment_dto import CreatePaymentDto
from src.utils.update_beanie_document_from_pydantic import (
    update_beanie_document_from_pydantic,
)


class BeaniePaymentsRepository(PaymentsRepository):

    async def create_payment(self, payment: CreatePaymentDto) -> Payment:
        payment_to_create = PaymentDocument(**payment.model_dump())
        await payment_to_create.insert()
        return payment_to_create

    async def get_payment_by_id(self, payment_id: str) -> Payment | None:
        payment = await PaymentDocument.find_one(
            PaymentDocument.id == payment_id
        ).project(Payment)
        if not payment:
            return None
        return payment

    async def get_payment_by_external_id(
        self, external_payment_id: str
    ) -> Payment | None:
        payment = await PaymentDocument.find_one(
            PaymentDocument.externalId == external_payment_id
        ).project(Payment)
        if not payment:
            return None
        return payment

    async def update_payment(self, payment: Payment) -> Payment | None:
        payment_document = await PaymentDocument.find_one(
            PaymentDocument.id == payment.id
        )
        if not payment_document:
            return None
        await update_beanie_document_from_pydantic(payment_document, payment)
        await payment_document.save_changes()

        updated_payment = await PaymentDocument.find_one(
            PaymentDocument.id == payment.id
        ).project(Payment)
        return updated_payment
