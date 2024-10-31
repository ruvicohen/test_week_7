from graphene import ObjectType, Schema


class Mutations(ObjectType):
    pass

class Query(ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutations)