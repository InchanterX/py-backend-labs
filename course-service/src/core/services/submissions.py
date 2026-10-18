# pylint: disable=unused-argument
# Stubs: arguments are kept to fix the signatures for the future implementation.
from uuid import UUID

from src.core.schemas import Artifacts, Submission, SubmissionCreate, SubmissionEdit
from src.core.services.common import not_implemented


def create_submission(body: SubmissionCreate, idempotency_key: str) -> Submission:
    not_implemented()


def get_submission(submission_id: UUID) -> Submission:
    not_implemented()


def update_submission(submission_id: UUID, body: SubmissionEdit) -> Submission:
    not_implemented()


def delete_submission(submission_id: UUID) -> None:
    not_implemented()


def get_submission_artifacts(submission_id: UUID) -> Artifacts:
    not_implemented()
