# pylint: disable=redefined-builtin
# Path parameter is named `id` in openapi.yaml.
from uuid import UUID

from fastapi import APIRouter

from src.core.schemas import Student, StudentAdd, Students
from src.core.services import students as students_service
from src.web.routers.common import API_PREFIX, IdempotencyKeyHeader, PageQuery, error_responses

students_router = APIRouter(prefix=API_PREFIX, tags=["Students"])


@students_router.post(
    "/courses/{id}/students",
    response_model=Student,
    status_code=201,
    responses=error_responses(401, 403, 404),
    summary="Записать студента на курс",
)
def add_student(id: UUID, idempotency_key: IdempotencyKeyHeader, body: StudentAdd):
    return students_service.add_student(id, body, idempotency_key)


@students_router.get(
    "/courses/{id}/students",
    response_model=Students,
    responses=error_responses(401, 403, 404),
    summary="Получить список студентов курса",
)
def list_students(id: UUID, page: PageQuery):
    return students_service.list_students(id, page)


@students_router.delete(
    "/courses/{id}/students/{student_id}",
    response_model=None,
    status_code=204,
    responses=error_responses(401, 403, 404),
    summary="Отчислить студента с курса",
)
def remove_student(id: UUID, student_id: UUID):
    students_service.remove_student(id, student_id)
