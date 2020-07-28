import graphene
import starwarsfansite.characters.schema
# from cookbook.ingredients.schema import IntroduceCategory, IntroduceIngredient


class Query(starwarsfansite.characters.schema.Query, graphene.ObjectType):
    pass


# class Mutation(graphene.ObjectType):
#     introduce_category = IntroduceCategory.Field()
#     introduce_ingredient = IntroduceIngredient.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
