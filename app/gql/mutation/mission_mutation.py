from graphene import Mutation, Float, Date, Int, Field
from app.gql.type.mission_type import MissionType
from app.repository.mission_repository import add_mission


class AddMission(Mutation):
    class Arguments:
        mission_id = Int()
        mission_date = Date()
        airborne_aircraft = Float()
        attacking_aircraft = Float()
        bombing_aircraft = Float()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, **kwargs):
        mission = add_mission(**kwargs)
        return AddMission(mission=mission)

