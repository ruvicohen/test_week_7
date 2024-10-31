from graphene import ObjectType, Field, String
from app.gql.type.mission_statistics_type import MissionStatisticsByCityType
from app.repository.city_repository import get_missions_by_city
from app.repository.target_repository import get_average_of_targets_by_city

class CityQuery(ObjectType):
    statistics_by_city = Field(MissionStatisticsByCityType, city_name=String())

    @staticmethod
    def resolve_statistics_by_city(parent, info, city_name):
        count_mission_by_city = len(get_missions_by_city(city_name))
        average_priority_by_city = get_average_of_targets_by_city(city_name).value_or(None)
        return MissionStatisticsByCityType(count_mission_by_city, average_priority_by_city)