from pydantic import BaseModel

from src.types.enums.product_category_enum import ProductCategoryEnum


class CreateProductDto(BaseModel):
    label: str
    description: str
    price: float
    availableAmount: int
    category: ProductCategoryEnum
    imageUrl: str
