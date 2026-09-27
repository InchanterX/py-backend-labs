from pydantic import BaseModel, ConfigDict

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


class ServiceInfo(BaseSchemaModel):
    healthy: bool = True
