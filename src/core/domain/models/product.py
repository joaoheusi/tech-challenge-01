from pydantic import BaseModel

from src.core.domain.enums.product_category_enum import ProductCategoryEnum


class Product(BaseModel):
    id: str
    createdAt: str
    updatedAt: str
    label: str
    isActive: bool
    description: str
    imageUrl: str
    price: float
    availableAmount: int
    category: ProductCategoryEnum
