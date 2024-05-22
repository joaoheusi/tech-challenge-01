from fastapi.routing import APIRouter

from src.core.application.use_cases.customers.controller import (
    CustomersUseCasesController,
)
from src.core.domain.dtos.customer.create_customer_dto import CreateCustomerDto
from src.core.domain.models.customer import Customer

customers_router = APIRouter(prefix="/customers", tags=["customers"])


@customers_router.get(
    "/{identifier}",
    response_model=Customer,
    description="Identifier can be either the customer's id, email or cpf.",
)
async def get_customer(identifier: str) -> Customer | None:
    customer = await CustomersUseCasesController.get_customer_by_identifier(
        identifier=identifier
    )
    return customer


@customers_router.post("/", response_model=Customer)
async def create_customer(customer: CreateCustomerDto) -> Customer:
    created_customer = await CustomersUseCasesController.create_customer(
        customer=customer
    )
    return created_customer
