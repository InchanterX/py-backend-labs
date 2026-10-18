from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, StringConstraints

from src.core.schemas.common import BaseInputModel, BaseSchemaModel, Pagination

CourseTitle = Annotated[str, StringConstraints(min_length=15, max_length=255)]
CourseDescription = Annotated[str, StringConstraints(min_length=32, max_length=4096)]


class CourseStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    DRAFT = "DRAFT"


class Course(BaseSchemaModel):
    id: UUID
    title: CourseTitle
    description: CourseDescription | None = None
    teacher_id: UUID
    status: CourseStatus
    created_at: AwareDatetime
    updated_at: AwareDatetime


class CourseCreate(BaseInputModel):
    title: CourseTitle
    description: CourseDescription | None = None
    teacher_id: UUID
    status: CourseStatus = CourseStatus.DRAFT


class CourseEdit(BaseInputModel):
    title: CourseTitle | None = None
    description: CourseDescription | None = None
    teacher_id: UUID | None = None
    status: CourseStatus | None = None


class Courses(BaseSchemaModel):
    data: list[Course]
    pagination: Pagination
