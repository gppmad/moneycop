from datetime import datetime
from typing import List
import pytz
from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Payments(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    location = Column(String)
    datetime = Column(DateTime)

    def __repr__(self):
        return f"Payment(id={self.id!r}, amount={self.amount!r}, location={self.location!r}, datetime={self.datetime!r})"

#Create DB
engine = create_engine("sqlite://", echo=True, future=True)
Base.metadata.create_all = engine

def save(amount:float , location:str, dt: datetime) -> List:
    with Session(engine) as session:
        first = Payments (amount=amount, location=location, datetime= dt )
        session.add_all([first])
        session.commit()

if __name__ == "__main__":
    save(1,'pr',datetime.now(pytz.utc))
    session = Session(engine)
    stmt = select(Payments)

    for payment in session.scalars(stmt):
         print(payment)

