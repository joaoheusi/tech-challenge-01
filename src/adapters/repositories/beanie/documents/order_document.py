from uuid import uuid4

from beanie import Document
from pydantic import Field

from src.core.domain.models.order import Order


class OrderDocument(Document, Order):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")  # type: ignore

    class Settings:
        name = "orders"
        use_state_management = True
