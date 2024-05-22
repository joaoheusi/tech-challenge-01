from uuid import uuid4

from beanie import Document
from pydantic import Field

from src.core.domain.models.customer import Customer


class CustomerDocument(Document, Customer):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")  # type: ignore

    class Settings:
        name = "customers"
        use_state_management = True
