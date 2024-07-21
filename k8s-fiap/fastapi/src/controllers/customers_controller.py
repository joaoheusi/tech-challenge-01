from src.config.injector.container import container
from src.entities.customer import Customer
from src.types.dtos.create_customer_dto import CreateCustomerDto
from src.use_cases.customers.create_customer import CreateCustomerUseCase
from src.use_cases.customers.get_customer import GetCustomerUseCase


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
