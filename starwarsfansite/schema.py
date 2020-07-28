import graphene
import starwarsfansite.characters.schema
from starwarsfansite.characters.schema import InsertPlanet


class Query(starwarsfansite.characters.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    insert_planet = InsertPlanet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
