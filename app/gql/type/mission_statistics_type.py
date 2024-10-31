from graphene import ObjectType, Float, Int

class MissionStatisticsByCityType(ObjectType):
    count_mission_by_city = Int()
    average_priority_targets_by_city = Float()

class MissionStatisticsByDateAndTargetTypeType(ObjectType):
    count_airborne = Int()
    count_attacking = Int()
    count_lost = Int()