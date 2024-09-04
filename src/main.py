# src/main.py
from fastapi import FastAPI

from .cars import models
from .cars.router import router as cars_router
from .database import engine

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# cars 라우터 등록
app.include_router(cars_router)
