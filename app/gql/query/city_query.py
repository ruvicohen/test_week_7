
from graphene import ObjectType, Field, String

from app.gql.type.mission_statistics_type import MissionStatisticsByCityType
from app.repository.city_repository import get_missions_by_city


class CityQuery(ObjectType):
    statistics_by_city = Field(MissionStatisticsByCityType, city_name=String())

    @staticmethod
    def resolve_statistics_by_city(parent, info, city_name):
        count_mission_by_city = get_missions_by_city(city_name)
        average_priority_by_city = get_missions_by_city(city_name)
        return count_mission_by_city, average_priority_by_city