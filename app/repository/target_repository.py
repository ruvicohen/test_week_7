from typing import List
from returns.result import Success, Result, Failure
from sqlalchemy import func
from app.db.database import session_maker
from app.db.models import Mission
from app.db.models.target import Target

def get_targets() -> List[Target]:
    with session_maker() as session:
        return session.query(Target).all()

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
            raise Failure(str(e))

def delete_target_by_mission_id(mission_id: int) -> Result[int, str]:
    with session_maker() as session:
        try:
            session.query(Target).filter(Target.mission_id == mission_id).delete()
            session.commit()
            return Success(mission_id)
        except Exception as e:
            session.rollback()
            raise Failure(str(e))