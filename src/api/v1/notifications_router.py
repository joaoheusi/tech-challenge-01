from fastapi import Body, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.controllers.notifications_controller import NotificationsController
from src.types.dtos.generic_notification_data import GenericNotificationDataDto

notifications_router = APIRouter(prefix="/notifications", tags=["notifications"])


@notifications_router.post("", response_model=dict[str, str])
async def receive_notification(
    notification: GenericNotificationDataDto = Body(...),
) -> JSONResponse:
    await NotificationsController.handle_received_notification(
        notification=notification
    )
    return JSONResponse(
        content={"message": "Notification received"},
        status_code=status.HTTP_200_OK,
    )
