from returns.result import Success, Result, Failure
from sqlalchemy import func
from app.db.database import session_maker
from app.db.models import Target, Country, City, TargetType
from app.db.models.mission import Mission
from app.repository.target_repository import delete_target_by_mission_id


def get_missions():
    with session_maker() as session:
        return session.query(Mission).all()

def get_mission_by_id(mission_id):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()

def get_missions_by_date(start_date, end_date):
    with session_maker() as session:
        return (session.query(Mission)
                .filter(Mission.mission_date >= start_date)
                .filter(Mission.mission_date <= end_date).all())

def get_missions_by_country(country_name):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target, Mission.mission_id == Target.mission_id)
                .join(City, Target.city_id == City.city_id)
                .join(Country, City.country_id == Country.country_id)
                .filter(Country.country_name == country_name).all())


def get_missions_by_target_industry(target_industry):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target, Target.mission_id == Mission.mission_id)
                .filter(Target.target_industry == target_industry).all())


def find_mission_by_target_type(target_type):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target, Target.mission_id == Mission.mission_id)
                .join(TargetType, TargetType.target_type_id == Target.target_type_id)
                .filter(TargetType.target_type_name == target_type).all())


def add_mission(**kwargs) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            mission = Mission(**kwargs)
            mission.mission_id = session.query(func.max(Mission.mission_id)).scalar() + 1
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except Exception as e:
            session.rollback()
            raise Failure(str(e))


def update_mission(mission_id, **kwargs) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            session.query(Mission).filter(Mission.mission_id == mission_id).update(kwargs)
            session.commit()
            return Success(get_mission_by_id(mission_id))
        except Exception as e:
            session.rollback()
            raise Failure(str(e))

def delete_mission(mission_id) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            mission = get_mission_by_id(mission_id)
            if mission:
                delete_target_by_mission_id(mission_id)
            session.query(Mission).filter(Mission.mission_id == mission_id).delete()
            session.commit()
            return Success(mission)
        except Exception as e:
            session.rollback()
            raise Failure(str(e))