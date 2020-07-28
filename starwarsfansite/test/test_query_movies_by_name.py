import pytest
from ..schema import schema

pytestmark = pytest.mark.django_db


def test_get_movies_by_name():
    query = """
        query {
            allMovies(title_Icontains: "Revenge") {
                edges {
                    node {
                        title,
                        episodeId,
                        openingCrawl,
                        releaseYear,
                        director,
                        producers,
                        planets {
                            edges {
                                node {
                                    name,
                                }
                            }
                        }
                    }
                }
            }
        }
    """
    expected = {
        "allMovies": {
            "edges": [
                {
                    "node": {
                        "title": "Revenge of the Sith",
                        "episodeId": 3,
                        "openingCrawl": "War! The Republic is crumbling under attacks by the ruthless Sith Lord, Count Dooku. There are heroes on both sides. Evil is everywhere.  In a stunning move, the fiendish droid leader, General Grievous, has swept into the Republic capital and kidnapped Chancellor Palpatine, leader of the Galactic Senate.  As the Separatist Droid Army attempts to flee the besieged capital with their valuable hostage, two Jedi Knights lead a desperate mission to rescue the captive Chancellor....",
                        "releaseYear": 2005,
                        "director": "George Lucas",
                        "producers": "Rick McCallum",
                        "planets": {
                            "edges": [
                                {
                                    "node": {
                                        "name": "Yavin IV"
                                    }
                                },
                                {
                                    "node": {
                                        "name": "Dagobah"
                                    }
                                }
                            ]
                        }
                    }
                }
            ]
        }
    }
    result = schema.execute(query)
    assert not result.errors
    assert result.data == expected
    print("test_get_movies_by_name OK")


test_get_movies_by_name()
