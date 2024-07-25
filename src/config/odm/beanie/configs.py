import os
from typing import Any

from dotenv import load_dotenv

from src.gateways.repositories.beanie.documents.customer_document import (
    CustomerDocument,
)
from src.gateways.repositories.beanie.documents.order_document import OrderDocument
from src.gateways.repositories.beanie.documents.payment_document import PaymentDocument
from src.gateways.repositories.beanie.documents.product_document import ProductDocument

load_dotenv()


MONGODB_URL = os.getenv("MONGODB_URL")

DOCUMENT_MODELS: list[Any] = [
    ProductDocument,
    CustomerDocument,
    OrderDocument,
    PaymentDocument,
]
