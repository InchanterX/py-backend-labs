from src.core.schemas.assignments import (
    Assignment,
    AssignmentCreate,
    AssignmentEdit,
    Assignments,
)
from src.core.schemas.common import (
    BaseInputModel,
    BaseSchemaModel,
    Error,
    ErrorDetail,
    IdempotencyKey,
    PageParams,
    Pagination,
    ServiceInfo,
)
from src.core.schemas.courses import Course, CourseCreate, CourseEdit, Courses, CourseStatus
from src.core.schemas.reviews import (
    Review,
    ReviewCreate,
    ReviewEdit,
    Reviews,
    ReviewStatus,
    ReviewType,
)
from src.core.schemas.students import Student, StudentAdd, Students
from src.core.schemas.submissions import (
    Artifacts,
    Submission,
    SubmissionCreate,
    SubmissionEdit,
    SubmissionStatus,
)

__all__ = [
    "Artifacts",
    "Assignment",
    "AssignmentCreate",
    "AssignmentEdit",
    "Assignments",
    "BaseInputModel",
    "BaseSchemaModel",
    "Course",
    "CourseCreate",
    "CourseEdit",
    "CourseStatus",
    "Courses",
    "Error",
    "ErrorDetail",
    "IdempotencyKey",
    "PageParams",
    "Pagination",
    "Review",
    "ReviewCreate",
    "ReviewEdit",
    "ReviewStatus",
    "ReviewType",
    "Reviews",
    "ServiceInfo",
    "Student",
    "StudentAdd",
    "Students",
    "Submission",
    "SubmissionCreate",
    "SubmissionEdit",
    "SubmissionStatus",
]
