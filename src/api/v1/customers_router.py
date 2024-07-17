from fastapi.routing import APIRouter

from src.controllers.customers_controller import CustomersUseCasesController
from src.entities.customer import Customer
from src.types.dtos.create_customer_dto import CreateCustomerDto

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
