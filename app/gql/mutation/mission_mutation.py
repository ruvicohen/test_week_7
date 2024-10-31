from graphene import Mutation, Float, Date, Int, Field
from app.gql.type.mission_type import MissionType
from app.repository.mission_repository import add_mission, update_mission, delete_mission


class AddMission(Mutation):
    class Arguments:
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
        mission = add_mission(**kwargs).value_or(None)
        return AddMission(mission=mission)

class UpdateMission(Mutation):
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
        mission = update_mission(**kwargs).value_or(None)
        return UpdateMission(mission=mission)

class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id):
        mission = delete_mission(mission_id).value_or(None)
        return DeleteMission(mission=mission)

