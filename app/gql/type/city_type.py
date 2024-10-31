import graphene
from graphene import ObjectType, Int, String

class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    longitude = String()
    latitude = String()

    country = graphene.Field("app.gql.type.country_type.CountryType")

    @staticmethod
    def resolve_country(root, info):
        return ""