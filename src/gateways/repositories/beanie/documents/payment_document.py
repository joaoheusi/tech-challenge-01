from uuid import uuid4

from beanie import Document
from pydantic import Field

from src.entities.payment import Payment


class PaymentDocument(Document, Payment):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")  # type: ignore

    class Settings:
        name = "payments"
        use_state_management = True
