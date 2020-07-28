import pytest
from ..schema import schema

pytestmark = pytest.mark.django_db


def test_get_characters_by_name():
    query = """
        query {
            allCharacters(name_Icontains: "Luke") {
                edges {
                    node {
                        name,
                        birthYear,
                        genre,
                        movies {
                            edges {
                                node {
                                title,
                                }
                            }
                        }
                    }
                }
            }
        }
    """
    expected = {
        "allCharacters": {
            "edges": [
                {
                    "node": {
                        "name": "Luke Skywalker",
                        "birthYear": "19BBY",
                        "genre": "male",
                        "movies": {
                            "edges": [
                                {
                                    "node": {
                                        "title": "A New Hope"
                                    }
                                },
                                {
                                    "node": {
                                        "title": "Revenge of the Sith"
                                    }
                                },
                                {
                                    "node": {
                                        "title": "The Empire Strikes Back"
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
    print("test_get_character_by_name OK")


test_get_characters_by_name()
