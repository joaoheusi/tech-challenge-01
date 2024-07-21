from uuid import uuid4

from beanie import Document
from pydantic import Field

from src.entities.product import Product


class ProductDocument(Document, Product):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")  # type: ignore

    class Settings:
        name = "products"
        use_state_management = True
