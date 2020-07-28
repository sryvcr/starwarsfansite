import graphene
import starwarsfansite.characters.schema
from starwarsfansite.characters.schema import InsertPlanet, InsertMovie, InsertCharacter


class Query(starwarsfansite.characters.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    insert_planet = InsertPlanet.Field()
    insert_movie = InsertMovie.Field()
    insert_character = InsertCharacter.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
