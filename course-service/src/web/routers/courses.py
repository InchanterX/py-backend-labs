# pylint: disable=redefined-builtin
# Path parameter is named `id` in openapi.yaml.
from uuid import UUID

from fastapi import APIRouter

from src.core.schemas import Course, CourseCreate, CourseEdit, Courses, CourseStatus
from src.core.services import courses as courses_service
from src.web.routers.common import API_PREFIX, IdempotencyKeyHeader, PageQuery, error_responses

courses_router = APIRouter(prefix=API_PREFIX, tags=["Courses"])


@courses_router.get(
    "/courses",
    response_model=Courses,
    responses=error_responses(401),
    summary="Получить список доступных курсов",
)
def list_courses(page: PageQuery, status: CourseStatus | None = None):
    return courses_service.list_courses(page, status)


@courses_router.post(
    "/courses",
    response_model=Course,
    status_code=201,
    responses=error_responses(401, 403, 404),
    summary="Создать новый курс",
)
def create_course(idempotency_key: IdempotencyKeyHeader, body: CourseCreate):
    return courses_service.create_course(body, idempotency_key)


@courses_router.get(
    "/courses/{id}",
    response_model=Course,
    responses=error_responses(401, 403, 404),
    summary="Получить курс по идентификатору",
)
def get_course(id: UUID):
    return courses_service.get_course(id)


@courses_router.patch(
    "/courses/{id}",
    response_model=Course,
    responses=error_responses(401, 403, 404),
    summary="Изменить курс",
)
def update_course(id: UUID, body: CourseEdit):
    return courses_service.update_course(id, body)


@courses_router.delete(
    "/courses/{id}",
    response_model=None,
    status_code=204,
    responses=error_responses(401, 403, 404),
    summary="Удалить курс",
)
def delete_course(id: UUID):
    courses_service.delete_course(id)
