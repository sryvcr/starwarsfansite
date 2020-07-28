from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from starwarsfansite.characters.models import (
    Character as CharacterModel,
    Movie as MovieModel,
    Planet as PlanetModel
)


class Planet(DjangoObjectType):
    class Meta:
        model = PlanetModel
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'movies': ['exact'],
        }
        interfaces = (relay.Node, )


class Movie(DjangoObjectType):
    class Meta:
        model = MovieModel
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'characters': ['exact'],
        }
        interfaces = (relay.Node, )



class Character(DjangoObjectType):
    class Meta:
        model = CharacterModel
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    all_planets = DjangoFilterConnectionField(Planet)
    planet = relay.Node.Field(Planet)

    all_movies = DjangoFilterConnectionField(Movie)
    movie = relay.Node.Field(Movie)

    all_characters = DjangoFilterConnectionField(Character)
    character = relay.Node.Field(Character)

