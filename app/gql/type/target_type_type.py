from graphene import ObjectType, String, Int


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()