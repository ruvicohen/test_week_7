from app.db.database import session_maker
from app.db.models.country import Country


def get_countries():
    with session_maker() as session:
        return session.query(Country).all()

print(get_countries())