# pylint: disable=redefined-builtin
# Path parameter is named `id` in openapi.yaml.
from uuid import UUID

from fastapi import APIRouter

from src.core.schemas import (
    Assignment,
    AssignmentCreate,
    AssignmentEdit,
    Assignments,
)
from src.core.services import assignments as assignments_service
from src.web.routers.common import API_PREFIX, IdempotencyKeyHeader, PageQuery, error_responses

assignments_router = APIRouter(prefix=API_PREFIX, tags=["Assignments"])


@assignments_router.post(
    "/assignments",
    response_model=Assignment,
    status_code=201,
    responses=error_responses(401, 403, 404),
    summary="Создать задание",
)
def create_assignment(idempotency_key: IdempotencyKeyHeader, body: AssignmentCreate):
    return assignments_service.create_assignment(body, idempotency_key)


@assignments_router.get(
    "/assignments",
    response_model=Assignments,
    responses=error_responses(401, 403),
    summary="Получить список заданий",
)
def list_assignments(page: PageQuery, course_id: UUID | None = None):
    return assignments_service.list_assignments(page, course_id)


@assignments_router.get(
    "/assignments/{id}",
    response_model=Assignment,
    responses=error_responses(401, 403, 404),
    summary="Получить задание по идентификатору",
)
def get_assignment(id: UUID):
    return assignments_service.get_assignment(id)


@assignments_router.patch(
    "/assignments/{id}",
    response_model=Assignment,
    responses=error_responses(401, 403, 404),
    summary="Изменить задание",
)
def update_assignment(id: UUID, body: AssignmentEdit):
    return assignments_service.update_assignment(id, body)


@assignments_router.delete(
    "/assignments/{id}",
    response_model=None,
    status_code=204,
    responses=error_responses(401, 403, 404),
    summary="Удалить задание",
)
def delete_assignment(id: UUID):
    assignments_service.delete_assignment(id)
