from graphene import  Int, String, Field, Mutation
from app.gql.type.target_type import TargetType
from app.repository.target_repository import add_target

class AddTarget(Mutation):
    class Arguments:
        mission_id = Int()
        target_industry = String()
        city_id = Int()
        target_type_id = Int()
        target_priority = Int()

    Target = Field(TargetType)

    @staticmethod
    def mutate(root, info, **kwargs):
        inserted_target = add_target(**kwargs).value_or(None)
        return AddTarget(Target=inserted_target)