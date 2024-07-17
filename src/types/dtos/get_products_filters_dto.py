from pydantic import BaseModel

from src.types.enums.product_category_enum import ProductCategoryEnum


class GetProductsFiltersDto(BaseModel):
    category: ProductCategoryEnum | None = None
    isActive: bool | None = None
    onlyInStock: bool | None = None
