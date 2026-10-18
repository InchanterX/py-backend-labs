# pylint: disable=unused-argument
# Stubs: arguments are kept to fix the signatures for the future implementation.
from uuid import UUID

from src.core.schemas import PageParams, Review, ReviewCreate, ReviewEdit, Reviews
from src.core.services.common import not_implemented


def create_review(submission_id: UUID, body: ReviewCreate, idempotency_key: str) -> Review:
    not_implemented()


def list_reviews(submission_id: UUID, page: PageParams) -> Reviews:
    not_implemented()


def get_review(submission_id: UUID, review_id: UUID) -> Review:
    not_implemented()


def update_review(submission_id: UUID, review_id: UUID, body: ReviewEdit) -> Review:
    not_implemented()
