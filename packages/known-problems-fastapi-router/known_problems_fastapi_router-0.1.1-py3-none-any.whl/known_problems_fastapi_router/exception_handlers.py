from fastapi.exceptions import RequestValidationError
from starlette import status
from fastapi import Request
from starlette.responses import JSONResponse

from known_problems_fastapi_router.types import KnownProblemResponse


def standard_validation_exception_handler(
    base_uri: str, request: Request, exc: RequestValidationError
):
    detail = ", ".join(
        [f"{error.get('loc')[1]}: {error.get('msg')}" for error in exc.errors()]
    )
    instance = f"{request.method}:/{request.url}"
    response = KnownProblemResponse(
        type=f"problem:{base_uri}/unprocessable-entity",
        title="Schema validation failed",
        status=422,
        detail=detail,
        instance=instance,
    )

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=response.dict()
    )
