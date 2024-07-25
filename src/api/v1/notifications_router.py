from typing import Any

from fastapi import Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.controllers.notifications_controller import NotificationsController

notifications_router = APIRouter(prefix="/notifications", tags=["notifications"])


@notifications_router.post("")
async def receive_notification(
    notification_data: dict[str, Any] = Body(...),
) -> JSONResponse:
    response = await NotificationsController.handle_received_notification(
        notification_data
    )
    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=200,
    )
