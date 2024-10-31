from app.db.database import session_maker
from app.db.models.city import City


def get_all_cities():
    with session_maker() as session:
        return session.query(City).all()

print(get_all_cities())