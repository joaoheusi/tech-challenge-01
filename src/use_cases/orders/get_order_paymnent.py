from injector import inject

from src.entities.payment import Payment
from src.excecptions.application_exceptions import ApplicationExceptions
from src.interfaces.repositories.orders_repository import OrdersRepository
from src.interfaces.repositories.payments_repository import PaymentsRepository


class GetOrderPaymentUseCase:
    @inject
    def __init__(
        self,
        orders_repository: OrdersRepository,
        payments_repository: PaymentsRepository,
    ):
        self.orders_repository = orders_repository
        self.payments_repository = payments_repository

    async def execute(self, order_id: str) -> Payment:
        order = await self.orders_repository.get_order_by_id(order_id)
        if not order:
            raise ApplicationExceptions.resource_not_found(
                resource_name="Order",
                identifier=["id"],
                identifier_value=order_id,
            )

        if not order.paymentId:
            raise ApplicationExceptions.resource_not_found(
                resource_name="Payment",
                identifier=["id"],
                identifier_value="none",
            )

        payment = await self.payments_repository.get_payment_by_id(order.paymentId)
        if not payment:
            raise ApplicationExceptions.resource_not_found(
                resource_name="Payment",
                identifier=["id"],
                identifier_value=order.paymentId or "none",
            )
        return payment
