from graphene import ObjectType, Date, List, String, Int, Field
from app.gql.type.mission_type import MissionType
from app.repository.mission_repository import get_mission_by_id, get_missions_by_date, get_missions_by_country, \
    get_missions_by_target_industry


class MissionQuery(ObjectType):
    mission_by_id = Field(MissionType, id=Int())
    missions_by_range_dates = List(MissionType, start_date=Date(), end_date=Date())
    missions_by_country = List(MissionType, country=String())
    missions_by_target_industry = List(MissionType, target_industry=String())

    @staticmethod
    def resolve_mission_by_id(root, info, id):
        return get_mission_by_id(id)

    @staticmethod
    def resolve_missions_by_range_dates(root, info, start_date, end_date):
        return get_missions_by_date(start_date, end_date)

    @staticmethod
    def resolve_missions_by_country(root, info, country):
        return get_missions_by_country(country)

    @staticmethod
    def resolve_missions_by_target_industry(root, info, target_industry):
        return get_missions_by_target_industry(target_industry)