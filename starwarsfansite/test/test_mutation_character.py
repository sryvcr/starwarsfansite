import pytest
from ..schema import schema

pytestmark = pytest.mark.django_db


def test_mutation_character():
    mutation = """
        mutation MyMutation {
            insertCharacter(input: { 
                clientMutationId: "1",
                name: "Ayla Secura",
                birthYear: "48BBY",
                genre: "female",
                movies: [2, 4]
            }) {
                character {
                    name
                    birthYear
                    genre
                    movies {
                        edges {
                            node {
                                title
                            }
                        }
                    }
                }
            }
        }
    """
    expected = {
        "insertCharacter": {
            "character": {
                "name": "Ayla Secura",
                "birthYear": "48BBY",
                "genre": "female",
                "movies": {
                    "edges": [
                        {
                            "node": {
                                "title": "Revenge of the Sith"
                            }
                        },
                        {
                            "node": {
                                "title": "Attack of the Clones"
                            }
                        }
                    ]
                }
            }
        }
    }
    result = schema.execute(mutation)
    assert not result.errors
    assert result.data == expected
    print("test_mutation_character OK")


test_mutation_character()
