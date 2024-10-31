from app.db.database import session_maker
from app.db.models.target import Target


def get_targets():
    with session_maker() as session:
        return session.query(Target).all()

print(get_targets())