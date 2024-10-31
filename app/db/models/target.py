from sqlalchemy import String, ForeignKey, Column, Integer
from sqlalchemy.orm import relationship

from app.db.models import Base


class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(primary_key=True, autoincrement=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    target_industry = Column(String)
    city_id = Column(String, ForeignKey('cities.city_id'))
    target_type_id = Column(String, ForeignKey('target_types.target_type_id'))
    target_priority = Column(String)

    city = relationship('City',back_populates='targets')
    target_type = relationship('TargetType')
    mission = relationship('Mission')

