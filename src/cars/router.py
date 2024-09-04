from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from . import schemas, service

router = APIRouter(
    prefix="/cars",
    tags=["cars"],
)


@router.post("/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return service.create_car(db=db, car=car)


@router.get("/", response_model=list[schemas.Car])
def read_cars(offset: int = None, limit: int = None, db: Session = Depends(get_db)):
    return service.get_cars(db, offset=offset, limit=limit)


@router.get("/{car_id}", response_model=schemas.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    db_car = service.get_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car


# @router.delete("/{car_id}", response_model=schemas.Car)
# def delete_car(car_id: int, db: Session = Depends(get_db)):
#     db_car = service.delete_car(db, car_id=car_id)
#     if db_car is None:
#         raise HTTPException(status_code=404, detail="Car not found")
#     return db_car
