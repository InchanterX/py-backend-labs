# pylint: disable=redefined-builtin
# Path parameter is named `id` in openapi.yaml.
from uuid import UUID

from fastapi import APIRouter

from src.core.schemas import Review, ReviewCreate, ReviewEdit, Reviews
from src.core.services import reviews as reviews_service
from src.web.routers.common import API_PREFIX, IdempotencyKeyHeader, PageQuery, error_responses

reviews_router = APIRouter(prefix=API_PREFIX, tags=["Reviews"])


@reviews_router.post(
    "/submissions/{id}/review",
    response_model=Review,
    status_code=201,
    responses=error_responses(401, 403, 404),
    summary="Создать проверку отправки",
)
def create_review(id: UUID, idempotency_key: IdempotencyKeyHeader, body: ReviewCreate):
    return reviews_service.create_review(id, body, idempotency_key)


@reviews_router.get(
    "/submissions/{id}/review",
    response_model=Reviews,
    responses=error_responses(401, 403, 404),
    summary="Получить список проверок отправки",
)
def list_reviews(id: UUID, page: PageQuery):
    return reviews_service.list_reviews(id, page)


@reviews_router.get(
    "/submissions/{id}/review/{review_id}",
    response_model=Review,
    responses=error_responses(401, 403, 404),
    summary="Получить проверку по идентификатору",
)
def get_review(id: UUID, review_id: UUID):
    return reviews_service.get_review(id, review_id)


@reviews_router.patch(
    "/submissions/{id}/review/{review_id}",
    response_model=Review,
    responses=error_responses(401, 403, 404),
    summary="Изменить проверку",
)
def update_review(id: UUID, review_id: UUID, body: ReviewEdit):
    return reviews_service.update_review(id, review_id, body)
