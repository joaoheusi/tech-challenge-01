from fastapi.exceptions import HTTPException


class ApplicationExceptions:

    @staticmethod
    def resource_not_found(
        resource_name: str,
        identifier: list[str],
        identifier_value: str,
    ) -> HTTPException:
        return HTTPException(
            status_code=404,
            detail={
                "error_code": "RESOURCE_NOT_FOUND",
                "message": f"Resource {resource_name} not found "
                f"with identifier {identifier}:{identifier_value}",
            },
        )

    @staticmethod
    def resource_already_exists(
        resource_name: str,
        identifier: list[str],
        identifier_value: str,
    ) -> HTTPException:
        return HTTPException(
            status_code=409,
            detail={
                "error_code": "RESOURCE_ALREADY_EXISTS",
                "message": f"Resource {resource_name} already exists "
                f"with identifier {identifier}:{identifier_value}",
            },
        )

    @staticmethod
    def product_inactive(
        product_id: str,
    ) -> HTTPException:
        return HTTPException(
            status_code=409,
            detail={
                "error_code": "PRODUCT_INACTIVE",
                "message": f"Product {product_id} is inactive",
            },
        )

    @staticmethod
    def product_not_available(
        product_id: str,
        requested_quantity: int,
        available_quantity: int,
    ) -> HTTPException:
        return HTTPException(
            status_code=409,
            detail={
                "error_code": "PRODUCT_NOT_AVAILABLE",
                "message": f"Product {product_id} not available in requested quantity."
                f"Requested: {requested_quantity}."
                f"Available: {available_quantity}.",
            },
        )
