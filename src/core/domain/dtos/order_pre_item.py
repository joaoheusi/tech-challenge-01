from pydantic import BaseModel, field_validator


class OrderPreItem(BaseModel):
    productId: str
    quantity: int

    @field_validator("quantity")
    def validate_quantity(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Quantity must be greater than 0")
        return v
