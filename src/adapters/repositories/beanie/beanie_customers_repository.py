from src.adapters.repositories.beanie.documents.customer_document import (
    CustomerDocument,
)
from src.core.domain.dtos.customer.create_customer_dto import CreateCustomerDto
from src.core.domain.models.customer import Customer
from src.core.domain.repositories.customers_port import CustomersPort


class BeanieCustomersRepository(CustomersPort):

    async def find_customer_by_id(self, customer_id: str) -> Customer | None:
        customer = await CustomerDocument.find_one(
            CustomerDocument.id == customer_id
        ).project(CustomerDocument)

        if not customer:
            return None

        return customer

    async def find_customer_by_cpf(self, cpf: str) -> Customer | None:
        customer = await CustomerDocument.find_one(CustomerDocument.cpf == cpf).project(
            CustomerDocument
        )

        if not customer:
            return None

        return customer

    async def find_customer_by_email(self, email: str) -> Customer | None:
        customer = await CustomerDocument.find_one(
            CustomerDocument.email == email
        ).project(CustomerDocument)

        if not customer:
            return None

        return customer

    async def create_customer(self, customer: CreateCustomerDto) -> Customer:
        customer_to_create = CustomerDocument(**customer.model_dump())
        await customer_to_create.insert()
        return customer_to_create
