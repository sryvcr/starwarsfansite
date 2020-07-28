import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from starwarsfansite.characters.models import (
    Character as CharacterModel,
    Movie as MovieModel,
    Planet as PlanetModel
)
from .data import (
    create_character,
    create_movie,
    create_planet
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


class InsertPlanet(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        climate = graphene.String(required=True)
        terrain = graphene.String(required=True)
        population = graphene.Int(required=True)

    planet = graphene.Field(Planet)

    @classmethod
    def mutate_and_get_payload(
        cls,
        root,
        info,
        name,
        climate,
        terrain,
        population,
        client_mutation_id=None
    ):
        new_planet = create_planet(name, climate, terrain, population)
        return InsertPlanet(planet=new_planet)
