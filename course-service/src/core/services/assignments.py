# pylint: disable=unused-argument
# Stubs: arguments are kept to fix the signatures for the future implementation.
from uuid import UUID

from src.core.schemas import (
    Assignment,
    AssignmentCreate,
    AssignmentEdit,
    Assignments,
    PageParams,
)
from src.core.services.common import not_implemented


def create_assignment(body: AssignmentCreate, idempotency_key: str) -> Assignment:
    not_implemented()


def list_assignments(page: PageParams, course_id: UUID | None) -> Assignments:
    not_implemented()


def get_assignment(assignment_id: UUID) -> Assignment:
    not_implemented()


def update_assignment(assignment_id: UUID, body: AssignmentEdit) -> Assignment:
    not_implemented()


def delete_assignment(assignment_id: UUID) -> None:
    not_implemented()
