# pylint: disable=redefined-builtin
# Path parameter is named `id` in openapi.yaml.
from uuid import UUID

from fastapi import APIRouter

from src.core.schemas import Artifacts, Submission, SubmissionCreate, SubmissionEdit
from src.core.services import submissions as submissions_service
from src.web.routers.common import API_PREFIX, IdempotencyKeyHeader, error_responses

submissions_router = APIRouter(prefix=API_PREFIX, tags=["Submissions"])


@submissions_router.post(
    "/submissions",
    response_model=Submission,
    status_code=201,
    responses=error_responses(401, 403, 404),
    summary="Отправить решение на проверку",
)
def create_submission(idempotency_key: IdempotencyKeyHeader, body: SubmissionCreate):
    return submissions_service.create_submission(body, idempotency_key)


@submissions_router.get(
    "/submissions/{id}",
    response_model=Submission,
    responses=error_responses(401, 403, 404),
    summary="Получить отправку по идентификатору",
)
def get_submission(id: UUID):
    return submissions_service.get_submission(id)


@submissions_router.patch(
    "/submissions/{id}",
    response_model=Submission,
    responses=error_responses(401, 403, 404),
    summary="Изменить отправку",
)
def update_submission(id: UUID, body: SubmissionEdit):
    return submissions_service.update_submission(id, body)


@submissions_router.delete(
    "/submissions/{id}",
    response_model=None,
    status_code=204,
    responses=error_responses(401, 403, 404),
    summary="Удалить отправку",
)
def delete_submission(id: UUID):
    submissions_service.delete_submission(id)


@submissions_router.get(
    "/submissions/{id}/artifacts",
    response_model=Artifacts,
    responses=error_responses(401, 403, 404),
    summary="Получить артефакты отправки",
)
def get_submission_artifacts(id: UUID):
    return submissions_service.get_submission_artifacts(id)
