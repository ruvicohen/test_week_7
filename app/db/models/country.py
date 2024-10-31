from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from app.db.models import Base


class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(primary_key=True, autoincrement=True)
    country_name = Column(String)

    cities = relationship('City',back_populates='country')