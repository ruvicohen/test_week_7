from app.db.database import session_maker
from app.db.models.mission import Mission


def get_missions():
    with session_maker() as session:
        return session.query(Mission).all()

print(get_missions())