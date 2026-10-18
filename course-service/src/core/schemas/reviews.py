from enum import StrEnum
from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, Field

from src.core.schemas.common import BaseInputModel, BaseSchemaModel, Pagination

Mark = Annotated[float, Field(ge=10.0, le=100.0)]


class ReviewType(StrEnum):
    AUTO = "auto"
    MANUAL = "manual"


class ReviewStatus(StrEnum):
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"


class Review(BaseSchemaModel):
    id: UUID
    type: ReviewType
    feedback: str | None = None
    mark: Mark | None = None
    status: ReviewStatus
    created_at: AwareDatetime
    updated_at: AwareDatetime


class ReviewCreate(BaseInputModel):
    type: ReviewType = ReviewType.MANUAL
    feedback: str
    mark: Mark


class ReviewEdit(BaseInputModel):
    feedback: str | None = None
    mark: Mark | None = None
    status: ReviewStatus | None = None


class Reviews(BaseSchemaModel):
    data: list[Review]
    pagination: Pagination
