from pydantic import BaseModel

from src.types.enums.product_category_enum import ProductCategoryEnum


class PatchProductDto(BaseModel):
    label: str | None = None
    description: str | None = None
    price: float | None = None
    availableAmount: int | None = None
    category: ProductCategoryEnum | None = None
    imageUrl: str | None = None
    isActive: bool | None = None
