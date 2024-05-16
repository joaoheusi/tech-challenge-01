from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field

from src.core.domain.enums.product_category_enum import ProductCategoryEnum


class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    label: str
    isActive: bool = True
    description: str
    imageUrl: str
    price: float
    availableAmount: int
    category: ProductCategoryEnum
