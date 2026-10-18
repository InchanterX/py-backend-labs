from typing import Annotated, Any

from fastapi import Depends, Header, Query

from src.core.schemas import Error, IdempotencyKey, PageParams

API_PREFIX = "/api/v1"

IdempotencyKeyHeader = Annotated[IdempotencyKey, Header(alias="Idempotency-Key")]


def page_params(
    offset: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    sort: str | None = None,
) -> PageParams:
    """
    Pagination as a dependency: a query model (Annotated[PageParams, Query()]) is flattened
    by FastAPI only when it is the single query parameter of a route.
    """
    return PageParams(offset=offset, limit=limit, sort=sort)


PageQuery = Annotated[PageParams, Depends(page_params)]


def error_responses(*status_codes: int) -> dict[int | str, dict[str, Any]]:
    """Documents error responses in Swagger with the common Error schema."""
    return {code: {"model": Error} for code in status_codes}
