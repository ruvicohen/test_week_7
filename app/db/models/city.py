from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class City(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.country_id'))
    longitude = Column(String)
    latitude = Column(String)

    country = relationship('Country',back_populates='cities')
    targets = relationship('Target',back_populates='city')