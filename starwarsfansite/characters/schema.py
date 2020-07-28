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
    create_planet,
    get_planets_by_ids,
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


class InsertMovie(relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        episode_id = graphene.Int(required=True)
        opening_crawl = graphene.String(required=True)
        release_year = graphene.Int(required=True)
        director = graphene.String(required=True)
        producers = graphene.String(required=True)
        planets = graphene.List(graphene.Int, required=True)

    movie = graphene.Field(Movie)

    @classmethod
    def mutate_and_get_payload(
        cls,
        root,
        info,
        title,
        episode_id,
        opening_crawl,
        release_year,
        director,
        producers,
        planets,
        client_mutation_id=None
    ):  
        planets_list = get_planets_by_ids(planets)
        new_movie = create_movie(
            title,
            episode_id,
            opening_crawl,
            release_year,
            director,
            producers,
            planets_list,
        )
        return InsertMovie(movie=new_movie)
