from flask import Flask
from sqlalchemy import Column, Integer, Date, Float

from app.db.models import Base


class Mission(Base):
    __tablename__ = "missions"
    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(Date)
    airborne_aircraft = Column(Float)
    attacking_aircraft = Column(Float)
    bombing_aircraft = Column(Float)
    aircraft_returned = Column(Float)
    aircraft_failed = Column(Float)
    aircraft_damaged = Column(Float)
    aircraft_lost = Column(Float)
