from typing import NoReturn

from fastapi import HTTPException, status

from src.core.schemas import ServiceInfo


def get_service_info():
    return ServiceInfo()


def not_implemented() -> NoReturn:
    """Placeholder for routes described in openapi.yaml but not implemented yet."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Not implemented")
