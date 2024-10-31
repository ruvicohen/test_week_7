from graphene import ObjectType, String, Int

class CountryType(ObjectType):
    country_id = Int()
    country_name = String()