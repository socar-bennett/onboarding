from datetime import datetime

from pydantic import BaseModel


class CarBase(BaseModel):
    name: str
    number: str


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
