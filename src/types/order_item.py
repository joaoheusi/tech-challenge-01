from pydantic import BaseModel


class OrderItem(BaseModel):
    productId: str
    productLabel: str
    quantity: int
    unitaryPrice: float
