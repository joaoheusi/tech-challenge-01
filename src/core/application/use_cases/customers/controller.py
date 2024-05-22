from src.config.injector.container import container
from src.core.application.use_cases.customers.create_customer import (
    CreateCustomerUseCase,
)
from src.core.application.use_cases.customers.get_customer import GetCustomerUseCase
from src.core.domain.dtos.customer.create_customer_dto import CreateCustomerDto
from src.core.domain.models.customer import Customer


class CustomersUseCasesController:

    @staticmethod
    async def get_customer_by_identifier(identifier: str) -> Customer | None:
        """
        identifier can be either the customer's id, cpf or email
        """
        get_customer_use_case = container.get(GetCustomerUseCase)
        customer = await get_customer_use_case.execute(identifier=identifier)
        return customer

    @staticmethod
    async def create_customer(customer: CreateCustomerDto) -> Customer:
        create_customer_use_case = container.get(CreateCustomerUseCase)
        created_customer = await create_customer_use_case.execute(customer=customer)
        return created_customer
