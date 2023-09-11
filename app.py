from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from controllers.user_controller import userController
from controllers.department_controller import departmentController
from controllers.ticket_controller import ticketController
from controllers.asset_controller import assetController

api = FastAPI()
api.include_router(userController)
api.include_router(departmentController)
api.include_router(ticketController)
api.include_router(assetController)


def custom_openapi():
    if api.openapi_schema:
        return api.openapi_schema
    openapi_schema = get_openapi(
        title="Eagle Co. API",
        version="1.0.0",
        description="This is the Eagle Co. API Documentation developed using **FastAPI** + **OpenAPI**",
        routes=api.routes,
    )
    api.openapi_schema = openapi_schema
    return api.openapi_schema


api.openapi = custom_openapi
