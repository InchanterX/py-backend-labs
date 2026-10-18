import uuid
from pathlib import Path

import pytest
import yaml

OPENAPI_SPEC = Path(__file__).parent.parent / "openapi.yaml"
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}


def spec_operations():
    with open(OPENAPI_SPEC, encoding="UTF-8") as file:
        spec = yaml.safe_load(file)
    return [
        (method, path)
        for path, item in spec["paths"].items()
        for method in item
        if method in HTTP_METHODS
    ]


@pytest.mark.parametrize(
    "url_path,status,response_json",
    (
        ("/", 404, {"detail": "Not Found"}),
        ("/api/v1/health", 200, {"healthy": True})
    )
)
def test_get(app_client, url_path, status, response_json):
    response = app_client.get(url_path)
    assert response.status_code == status
    assert response.json() == response_json


def test_get_openapi(app_client):
    response = app_client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json().get("openapi") == "3.1.0"


def test_get_swagger(app_client):
    response = app_client.get("/docs")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text


@pytest.mark.parametrize("method,path", spec_operations())
def test_spec_operation_registered(app_client, method, path):
    paths = app_client.get("/openapi.json").json()["paths"]
    assert method in paths.get(path, {})


@pytest.mark.parametrize(
    "method,path",
    (
        ("get", "/api/v1/courses"),
        ("get", f"/api/v1/courses/{uuid.uuid4()}"),
        ("delete", f"/api/v1/submissions/{uuid.uuid4()}"),
        ("get", f"/api/v1/submissions/{uuid.uuid4()}/review"),
    )
)
def test_not_implemented(app_client, method, path):
    response = app_client.request(method, path)
    assert response.status_code == 501


def test_create_course_requires_idempotency_key(app_client):
    body = {"title": "Python backend course", "teacher_id": str(uuid.uuid4())}
    response = app_client.post("/api/v1/courses", json=body)
    assert response.status_code == 422


def test_create_course_forbids_extra_fields(app_client):
    body = {"title": "Python backend course", "teacher_id": str(uuid.uuid4()), "extra": 1}
    headers = {"Idempotency-Key": str(uuid.uuid4())}
    response = app_client.post("/api/v1/courses", json=body, headers=headers)
    assert response.status_code == 422


def test_list_courses_validates_limit(app_client):
    response = app_client.get("/api/v1/courses", params={"limit": 1000})
    assert response.status_code == 422
