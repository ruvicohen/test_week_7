from typing import List
from returns.maybe import Maybe
from returns.result import Success, Result, Failure
from sqlalchemy import func
from app.db.database import session_maker
from app.db.models import Mission, City
from app.db.models.target import Target

def get_targets() -> List[Target]:
    with session_maker() as session:
        return session.query(Target).all()

def get_average_of_targets_by_city(city_name: str) -> Maybe[float]:
    with session_maker() as session:
        average_value = (session.query(func.avg(Target.target_priority))
                         .join(City, City.city_id == Target.city_id)
                         .filter(City.city_name == city_name).scalar())
        return Maybe.from_optional(average_value)

def add_target(**kwargs) -> Result[Target, str]:
    with session_maker() as session:
        try:
            mission_id = kwargs.get('mission_id')
            mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            if not mission:
                return Failure("mission not found")
            target = Target(**kwargs)
            target.target_id = session.query(func.max(Target.target_id)).scalar() + 1
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

def delete_target_by_mission_id(mission_id: int) -> Result[int, str]:
    with session_maker() as session:
        try:
            session.query(Target).filter(Target.mission_id == mission_id).delete()
            session.commit()
            return Success(mission_id)
        except Exception as e:
            session.rollback()
            return Failure(str(e))