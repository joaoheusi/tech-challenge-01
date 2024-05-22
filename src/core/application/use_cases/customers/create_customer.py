from injector import inject

from src.core.domain.dtos.customer.create_customer_dto import CreateCustomerDto
from src.core.domain.models.customer import Customer
from src.core.domain.repositories.customers_port import CustomersPort
from src.core.utils.validate_cpf import validate_cpf
from src.core.utils.validate_email import validate_email


class CreateCustomerUseCase:

    @inject
    def __init__(self, customers_repository: CustomersPort):
        self.customers_repository = customers_repository

    async def execute(self, customer: CreateCustomerDto) -> Customer:

        cpf_is_valid = await validate_cpf(customer.cpf)

        if not cpf_is_valid:
            raise ValueError("Invalid CPF.")

        formatted_cpf = customer.cpf.replace(".", "").replace("-", "")

        customer.cpf = formatted_cpf

        email_is_valid = await validate_email(customer.email)

        if not email_is_valid:
            raise ValueError("Invalid Email.")

        existing_customer_with_email = (
            await self.customers_repository.find_customer_by_email(email=customer.email)
        )

        if existing_customer_with_email:
            raise ValueError("Customer already exists with this email.")

        existing_customer_with_cpf = (
            await self.customers_repository.find_customer_by_cpf(cpf=customer.cpf)
        )
        if existing_customer_with_cpf:
            raise ValueError("Customer already exists with this CPF.")

        return await self.customers_repository.create_customer(customer)
