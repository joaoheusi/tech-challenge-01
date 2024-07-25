from typing import Any

from fastapi import HTTPException
from pydantic import ValidationError

from src.config.injector.container import container
from src.types.dtos.generic_notification_data import GenericNotificationDataDto
from src.types.dtos.payment_updated_notification_dto import (
    PaymentUpdatedNotificationDto,
)
from src.types.enums.notification_category import NotificationCategoryEnum
from src.use_cases.payments.update_payment_use_case import UpdatePaymentUseCase


class NotificationsController:

    @staticmethod
    async def handle_received_notification(notification_data: dict[str, Any]) -> Any:
        try:
            notification = GenericNotificationDataDto(**notification_data)
            if notification.action == NotificationCategoryEnum.PAYMENT_CREATED:
                raise NotImplementedError(
                    "Payment created action is not implemented yet"
                )
            elif notification.action == NotificationCategoryEnum.PAYMENT_UPDATED:
                update_payment_use_case = container.get(UpdatePaymentUseCase)
                await update_payment_use_case.execute(
                    notification=PaymentUpdatedNotificationDto(**notification_data)
                )
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.errors())
        return notification
