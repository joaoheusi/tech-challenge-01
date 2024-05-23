from pydantic import BaseModel


class OrderPreItem(BaseModel):
    productId: str
    quantity: int
