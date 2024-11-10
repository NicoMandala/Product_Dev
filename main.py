from fastapi import FastAPI
from routers.Task1.main import router as task1_router
from routers.TaskA.main import router as taskA_router

app = FastAPI()

app.include_router(task1_router)
app.include_router(taskA_router)