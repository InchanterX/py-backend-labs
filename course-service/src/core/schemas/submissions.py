from enum import StrEnum
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, Field

from src.core.schemas.common import BaseInputModel, BaseSchemaModel


class SubmissionStatus(StrEnum):
    SUBMITTED = "SUBMITTED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class Submission(BaseSchemaModel):
    id: UUID
    assignment_id: UUID
    submitted_at: AwareDatetime
    review_id: UUID | None = Field(None, description="Появляется после создания проверки")
    repository_url: AnyUrl
    status: SubmissionStatus
    artifacts_url: AnyUrl | None = Field(None, description="Появляется после завершения проверки")
    created_at: AwareDatetime
    updated_at: AwareDatetime


class SubmissionCreate(BaseInputModel):
    assignment_id: UUID
    repository_url: AnyUrl


class SubmissionEdit(BaseInputModel):
    repository_url: AnyUrl | None = None


class Artifacts(BaseSchemaModel):
    submission_id: UUID
    artifacts_url: AnyUrl
