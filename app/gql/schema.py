from graphene import ObjectType, Schema
from app.gql.mutation.mission_mutation import AddMission
from app.gql.mutation.target_mutation import AddTarget
from app.gql.query.mission_query import MissionQuery


class Mutations(ObjectType):
    add_mission = AddMission.Field()
    add_target = AddTarget.Field()

class Query(MissionQuery):
    pass

schema = Schema(query=Query, mutation=Mutations)