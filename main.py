from fastapi import FastAPI

from controllers.user_controller import userController
from controllers.department_controller import departmentController
from controllers.ticket_controller import ticketController

app = FastAPI()
app.include_router(userController)
app.include_router(departmentController)
app.include_router(ticketController)
