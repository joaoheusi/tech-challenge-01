from uuid import uuid4

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.controllers.payments_controller import PaymentsController
from src.entities.order import Order

payments_router = APIRouter(prefix="/payments", tags=["orders"])


@payments_router.post("", response_model=list[Order])
async def create_payment() -> JSONResponse:
    payment_id = str(uuid4())
    payment_amount = 100
    payment = await PaymentsController.create_payment(payment_id, payment_amount)
    return JSONResponse(
        content=jsonable_encoder(payment),
        status_code=status.HTTP_200_OK,
    )
