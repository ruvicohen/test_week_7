from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from app.db.models import Base


class TargetType(Base):
    __tablename__ = "target_types"
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String, unique=True)

