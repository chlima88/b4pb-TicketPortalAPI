from fastapi import FastAPI

from controllers.user_controller import userController
from controllers.department_controller import departmentController
from controllers.ticket_controller import ticketController

api = FastAPI()
api.include_router(userController)
api.include_router(departmentController)
api.include_router(ticketController)
