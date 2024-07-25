from injector import inject

from src.interfaces.providers.payments_provider import PaymentsProvider
from src.interfaces.repositories.orders_repository import OrdersRepository
from src.interfaces.repositories.payments_repository import PaymentsRepository
from src.types.dtos.payment_updated_notification_dto import (
    PaymentUpdatedNotificationDto,
)
from src.types.enums.order_status_enum import OrderStatusEnum
from src.types.enums.payment_status_enum import PaymentStatusEnum


class UpdatePaymentUseCase:
    @inject
    def __init__(
        self,
        payments_provider: PaymentsProvider,
        payments_repository: PaymentsRepository,
        orders_repository: OrdersRepository,
    ):
        self.payments_provider = payments_provider
        self.payments_repository = payments_repository
        self.orders_repository = orders_repository

    async def execute(self, notification: PaymentUpdatedNotificationDto) -> None:
        payment = await self.payments_repository.get_payment_by_external_id(
            external_payment_id=notification.data.id
        )
        if not payment:
            # Tentativa de atualizar um pagamento que não existe
            return None

        if payment.status != PaymentStatusEnum.PENDING:
            # Pagamento já foi processado
            return None

        order = await self.orders_repository.get_order_by_payment_id(
            payment_id=payment.id
        )
        if not order:
            # Pagamento sem order associada
            return None

        externalPaymentData = await self.payments_provider.get_payment(
            external_payment_id=notification.data.id
        )

        if externalPaymentData.status == PaymentStatusEnum.SUCCESSFUL:
            # atualizar status do payment
            # atualizar status da order

            payment.status = PaymentStatusEnum.SUCCESSFUL

            order.status = OrderStatusEnum.PREPARING

            await self.orders_repository.update_order(order)
            await self.payments_repository.update_payment(payment)

        elif externalPaymentData.status == PaymentStatusEnum.FAILED:
            # atualizar status do payment
            # atualizar status da order

            payment.status = PaymentStatusEnum.FAILED

            order.status = OrderStatusEnum.CANCELED

            await self.orders_repository.update_order(order)
            await self.payments_repository.update_payment(payment)

        else:
            print("STATUS DO PAGAMENTO ESTA COMO PENDING")
