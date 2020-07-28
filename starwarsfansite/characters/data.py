from .models import Character, Movie, Planet


def get_planet(_id):
    return Planet.objects.get(id=_id)


def create_planet(
    name,
    climate,
    terrain,
    population,
):
    new_planet = Planet(
        name=name,
        climate=climate,
        terrain=terrain,
        population=population,
    )
    new_planet.save()
    return new_planet


def get_movie(_id):
    return Movie.objects.get(id=_id)


def create_movie(
    title,
    episode_id,
    opening_crawl,
    release_year,
    director,
    producers,
    planets,
):
    new_movie = Movie(
        title=title,
        episode_id=episode_id,
        opening_crawl=opening_crawl,
        release_year=release_year,
        director=director,
        producers=producers,
        planets=planets,
    )
    new_movie.save()
    return new_movie


def get_character(_id):
    return Character.objects.get(id=_id)


def create_character(
    name,
    birth_year,
    genre,
    movies,
):
    new_character = Character(
        name,
        birth_year,
        genre,
        movies,
    )
    new_character.save()
    return new_character
