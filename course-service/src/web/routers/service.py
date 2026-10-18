import logging

from fastapi import APIRouter

from src.core.schemas import ServiceInfo
from src.core.services import get_service_info
from src.web.lifespans import lifespan_service_router
from src.web.routers.common import API_PREFIX

logger = logging.getLogger(__name__)

service_router = APIRouter(
    prefix=API_PREFIX,  # /api/v1/
    lifespan=lifespan_service_router,  # custom context manager
    tags=["Service"],  # groups for swagger
)

"""
Decorator registrate the function in a list of routes.
That one uses method GET (.get). It is also can be .post, .put, .patch, .delete and etc.
"""


@service_router.get(
    "/health",
    # description in Swagger
    description="Course service info route",
    # returned value will be validated through the given schema
    response_model=ServiceInfo,
    status_code=200,
)
def info():
    """
    Synchronous handlers are executed by FastAPI in a separated thread not to block async handlers.
    """
    return get_service_info()
