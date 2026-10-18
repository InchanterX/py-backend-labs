from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

"""
BaseModel is a base pydantic class that gives:
- cheks and type convertion for class fields
- serialization: model.model_dump() returns a dict and model.model_dump_json() returns a JSON-string
- creation from data: Model.model_validate(dict_or_obj)
- JSON Schema, used by FastAPI to build /docs
"""
"""
ConfigDict identical to SettingsConfigDict but uset for common models.
    Also stores dict of settings in model_config class field.
    - from_attributes=Ture - allow to create a model not only from a dict,
        but also from an object with attributes.
    - validate_assignment=True - turn on checks not only for a model creation,
        but also for assignments to it fileds.
    - populate_by_name=True - allow to assign using aliases.
"""


class BaseSchemaModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        populate_by_name=True,
    )


"""
Base for request bodies: extra="forbid" rejects unknown fields with 422.
Configs of parent and child are merged by pydantic.
"""


class BaseInputModel(BaseSchemaModel):
    model_config = ConfigDict(extra="forbid")


"""
Annotated aliases keep repeated constraints in one place.
"""
IdempotencyKey = Annotated[str, StringConstraints(min_length=36, max_length=36)]


class ServiceInfo(BaseSchemaModel):
    healthy: bool = True


class PageParams(BaseSchemaModel):
    """Query parameters shared by every list route."""

    offset: Annotated[int, Field(ge=0)] = 0
    limit: Annotated[int, Field(ge=1, le=100)] = 10
    sort: str | None = None


class Pagination(BaseSchemaModel):
    offset: int
    limit: int
    total: int


class ErrorDetail(BaseSchemaModel):
    code: str = Field(..., examples=["COURSE_NOT_FOUND"])
    message: str = Field(..., examples=["Курс не существует"])
    status: int = Field(..., examples=[404])
    path: str = Field(..., examples=["/api/v1/courses/"])
    request_id: UUID = Field(..., examples=["00000000-0000-0000-0000-000000000000"])


class Error(BaseSchemaModel):
    error: ErrorDetail
