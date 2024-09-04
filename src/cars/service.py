from sqlalchemy.orm import Session

from . import models, schemas


def create_car(db: Session, car: schemas.CarCreate):
    try:
        db_car = models.Car(**car.model_dump())
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
        return True
    except:
        db.rollback()
        return False


def get_car(db: Session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()


def get_cars(db: Session, offset: int = None, limit: int = None):
    query = db.query(models.Car)

    if offset is not None and isinstance(offset, int):
        query = query.offset(offset)

    if limit is not None and isinstance(limit, int):
        query = query.limit(limit)

    return query.all()


def delete_car(db: Session, car_id: int):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if db_car:
        db.delete(db_car)
        db.commit()
    return db_car
