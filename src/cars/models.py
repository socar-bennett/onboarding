from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from ..database import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500))
    number = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
