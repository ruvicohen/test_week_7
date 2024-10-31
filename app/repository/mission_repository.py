from returns.result import Success, Result, Failure

from app.db.database import session_maker
from app.db.models import Target, Country, City, TargetType
from app.db.models.mission import Mission


def get_missions():
    with session_maker() as session:
        return session.query(Mission).all()

# Queries (Infinite)
# 1. Find a mission by Mission ID: Retrieves full mission details.
def get_mission_by_id(mission_id):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_id == mission_id).first()

# 2. Find missions within a date range: Returns a list of relevant mission details.
def get_missions_by_date(start_date, end_date):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.start_date >= start_date).filter(Mission.start_date <= end_date).all()
# 3. Find a mission by country involved: Returns a list of details for all matching missions.
def get_missions_by_country(country_id):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target, Mission.mission_id == Target.mission_id)
                .join(City, Target.city_id == City.city_id)
                .join(Country, City.country_id == Country.country_id)
                .filter(Country.country_id == country_id).all())


# 4. Find a mission by Target Industry: Returns a list of details for all relevant missions.
def get_missions_by_target_industry(target_industry):
    with session_maker() as session:
        return session.query(Mission).join(Target, Target.mission_id == Mission.mission_id).filter(Target.target_industry == target_industry).all()
# 5. Find all aircraft by mission: Returns a list of all relevant aircraft.

# 6. Find attack results by type of attack: Returns a list of attack outcomes, including:
#    - returned_aircraft
#    - failed_aircraft
#    - damaged_aircraft
#    - lost_aircraft
#    - damage_assessment

def find_mission_by_target_type(target_type):
    with session_maker() as session:
        return session.query(Mission).join(Target, Target.mission_id == Mission.mission_id).join(TargetType, TargetType.target_type_id == Target.target_type_id).filter(TargetType.target_type_name == target_type).all()

# Mutations
# 1. Add a new mission (with all details).
# 2. Add a target (linked to a mission).
def add_mission(**kwargs) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            mission = Mission(**kwargs)
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except Exception as e:
            session.rollback()
            raise Failure(str(e))
# 3. Add an attack result (linked to a mission).
def add_target(**kwargs) -> Result[Target, str]:
    with session_maker() as session:
        try:
            target = Target(**kwargs)
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
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
# 4. Update an attack result (can update any of the 5 fields listed above).
# 5. Delete a mission (including all its links).
def delete_mission(mission_id) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            session.query(Mission).filter(Mission.mission_id == mission_id).delete()
            session.commit()
            return Success(get_mission_by_id(mission_id))
        except Exception as e:
            session.rollback()
            raise Failure(str(e))



