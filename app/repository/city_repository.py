from app.db.database import session_maker
from app.db.models import City, Mission, Target

def get_missions_by_city(city_name):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target, Mission.mission_id == Target.mission_id)
                .join(City, Target.city_id == City.city_id)
                .filter(City.city_name == city_name).all())