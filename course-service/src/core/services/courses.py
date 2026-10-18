# pylint: disable=unused-argument
# Stubs: arguments are kept to fix the signatures for the future implementation.
from uuid import UUID

from src.core.schemas import Course, CourseCreate, CourseEdit, Courses, CourseStatus, PageParams
from src.core.services.common import not_implemented


def list_courses(page: PageParams, course_status: CourseStatus | None) -> Courses:
    not_implemented()


def create_course(body: CourseCreate, idempotency_key: str) -> Course:
    not_implemented()


def get_course(course_id: UUID) -> Course:
    not_implemented()


def update_course(course_id: UUID, body: CourseEdit) -> Course:
    not_implemented()


def delete_course(course_id: UUID) -> None:
    not_implemented()
