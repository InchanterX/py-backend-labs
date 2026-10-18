from datetime import date
from typing import Annotated
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, Field, StringConstraints

from src.core.schemas.common import BaseInputModel, BaseSchemaModel, Pagination

AssignmentTitle = Annotated[str, StringConstraints(min_length=1)]
SubmitLimit = Annotated[int, Field(ge=3, le=10)]


class Assignment(BaseSchemaModel):
    id: UUID
    title: AssignmentTitle
    description: str | None = None
    course_id: UUID
    submit_limit: SubmitLimit = Field(..., description="Максимальное количество отправок решения")
    date_start: date = Field(..., description="Дата начала приёма решений")
    date_end: date = Field(
        ..., description="Дата окончания приёма решений (не раньше `date_start`)"
    )
    materials_url: AnyUrl | None = None
    created_at: AwareDatetime
    updated_at: AwareDatetime


class AssignmentCreate(BaseInputModel):
    title: AssignmentTitle
    description: str | None = None
    course_id: UUID
    submit_limit: SubmitLimit
    date_start: date
    date_end: date
    materials_url: AnyUrl | None = None


class AssignmentEdit(BaseInputModel):
    title: AssignmentTitle | None = None
    description: str | None = None
    submit_limit: SubmitLimit | None = None
    date_start: date | None = None
    date_end: date | None = None
    materials_url: AnyUrl | None = None


class Assignments(BaseSchemaModel):
    data: list[Assignment]
    pagination: Pagination
