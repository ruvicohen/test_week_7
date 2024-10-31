from app.db.database import session_maker
from app.db.models.target_type import TargetType


def get_target_types():
    with session_maker() as session:
        return session.query(TargetType).all()

print(get_target_types())