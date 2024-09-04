from fastapi import FastAPI

from .cars import models
from .cars.router import router as cars_router
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(cars_router)
