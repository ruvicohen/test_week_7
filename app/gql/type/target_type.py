import graphene
from graphene import ObjectType, Int, String

from app.db.models.city import City


class TargetType(ObjectType):
    target_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

    city = graphene.Field("app.gql.type.city_type.CityType")
    target_type = graphene.Field("app.gql.type.target_type_type.TargetTypeType")

    @staticmethod
    def resolve_city(root, info):
        return ""

    @staticmethod
    def resolve_target_type(root, info):
        return ""