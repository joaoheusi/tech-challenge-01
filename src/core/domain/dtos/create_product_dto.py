from pydantic import BaseModel

from core.domain.enums.product_category_enum import ProductCategoryEnum


class CreateProductDto(BaseModel):
    label: str
    description: str
    price: float
    availableAmount: int
    category: ProductCategoryEnum
    imageUrl: str
