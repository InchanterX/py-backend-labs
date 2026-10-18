# pylint: disable=unused-argument
# Stubs: arguments are kept to fix the signatures for the future implementation.
from uuid import UUID

from src.core.schemas import PageParams, Student, StudentAdd, Students
from src.core.services.common import not_implemented


def add_student(course_id: UUID, body: StudentAdd, idempotency_key: str) -> Student:
    not_implemented()


def list_students(course_id: UUID, page: PageParams) -> Students:
    not_implemented()


def remove_student(course_id: UUID, student_id: UUID) -> None:
    not_implemented()
