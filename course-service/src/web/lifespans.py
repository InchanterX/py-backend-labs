import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

logger = logging.getLogger(__name__)

"""
contextmanager and asynccontextmanager transform function to a contextmanager (as with for example)
so the begining and the end will be guaranted to be executed.
Async manager used for async functions with async body.
"""


@asynccontextmanager
async def lifespan_service_router(app: FastAPI):
    logger.debug("Lifespan course service router startup")
    try:
        yield
    finally:
        logger.debug("Lifespan course service router shutdown")


@asynccontextmanager
async def lifespan_app(app: FastAPI):
    logger.debug("Lifespan course app startup")
    try:
        yield
    finally:
        logger.debug("Lifespan course app shutdown")
