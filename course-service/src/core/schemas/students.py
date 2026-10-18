from uuid import UUID

from pydantic import AwareDatetime

from src.core.schemas.common import BaseInputModel, BaseSchemaModel, Pagination


class Student(BaseSchemaModel):
    student_id: UUID
    course_id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


class StudentAdd(BaseInputModel):
    student_id: UUID


class Students(BaseSchemaModel):
    data: list[Student]
    pagination: Pagination
