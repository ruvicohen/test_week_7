from graphene import ObjectType, Float, Int


class MissionStatisticsByCityType(ObjectType):
    count_mission_by_city = Int()
    average_priority_targets_by_city = Float()
    