from src.web.routers.assignments import assignments_router
from src.web.routers.courses import courses_router
from src.web.routers.reviews import reviews_router
from src.web.routers.service import service_router
from src.web.routers.students import students_router
from src.web.routers.submissions import submissions_router

# All routers of the service, in the order they appear in Swagger.
ROUTERS = (
    service_router,
    courses_router,
    students_router,
    assignments_router,
    submissions_router,
    reviews_router,
)

__all__ = [
    "ROUTERS",
    "assignments_router",
    "courses_router",
    "reviews_router",
    "service_router",
    "students_router",
    "submissions_router",
]
