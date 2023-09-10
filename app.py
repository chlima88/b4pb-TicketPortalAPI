from fastapi import FastAPI

from controllers.user_controller import userController
from controllers.department_controller import departmentController
from controllers.ticket_controller import ticketController
from controllers.asset_controller import assetController

api = FastAPI()
api.include_router(userController)
api.include_router(departmentController)
api.include_router(ticketController)
api.include_router(assetController)
