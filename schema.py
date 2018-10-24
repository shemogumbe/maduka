import graphene

from api.schema import  Mutation
import api.schema

class Query(
   api.schema.Query,
    ):
    pass


class Mutation(
    Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
