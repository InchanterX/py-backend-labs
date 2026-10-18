import functools
from typing import final

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

"""
BaseSettings is a BaseModel object that search for the fields for itself in several sources:
1. Explicitly given arguments (Settings(app=...))
2. OS environment variabls
3. .env file
4. Default class values
It allow to make a unified class that can be used in different envirments with different values.
"""
"""
SettingsConfigDict is technicaly just a Dict but with determined keys that can be seen in IDE hints.
Always assigns to model_config variable of a class to setup its behaviors.
- env_file=".env" - read vars from file (route determines from the program starting point)
- env_file_encoding="utf-8" - files' encoding
- env_nested_delimiter="__" - how to split nesting levels
- extra="allow" - extra vars in .env will be added as attributes and won't cause a error
    For instance: APP_TITLE=VALUE will be transformed to app.title
"""


class AppSettings(BaseSettings):
    title: str = "Course service"
    description: str = "Course service API"
    summary: str = "Course service summary"
    version: str = "1.0.0"
    contact: dict[str, str] = Field(
        default_factory=lambda: {"name": "Тех. поддержка", "email": "support@yandex.ru"}
    )
    servers: list[dict[str, str]] = Field(
        default_factory=lambda: [{"url": "http://127.0.0.1:8000", "description": "Development"}]
    )
    debug: bool = False
    docs_url: str | None = "/docs"
    redoc_url: str | None = "/redoc"
    openapi_url: str | None = "/openapi.json"
    root_path: str = ""


"""
@Final marker for static analitics (mypy and etc.),
mark that it is prohibit to inherit from this class.
Otherwise analitics will return error.
Just intentions mark.
"""


@final
class Settings(BaseSettings):
    app: AppSettings = Field(default_factory=AppSettings)

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
    )


@functools.lru_cache
def get_settings():
    return Settings()
