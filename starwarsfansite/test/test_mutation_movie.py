import pytest
from ..schema import schema

pytestmark = pytest.mark.django_db


def test_mutation_movie():
    mutation = """
        mutation MyMutation {
            insertMovie( input: {
                clientMutationId:"1",
                title: "Attack of the Clones",
                episodeId: 2,
                openingCrawl: "There is unrest in the Galactic Senate. Several thousand solar systems have declared their intentions to leave the Republic.  This separatist movement, under the leadership of the mysterious Count Dooku, has made it difficult for the limited number of Jedi Knights to maintain  peace and order in the galaxy.  Senator Amidala, the former Queen of Naboo, is returning to the Galactic Senate to vote on the critical issue of creating an ARMY OF THE REPUBLIC to assist the overwhelmed Jedi....",
                releaseYear: 2002,
                director: "George Lucas",
                producers: "Rick McCallum",
                planets: [ 5 ],
            }) {
                movie {
                    title
                    episodeId
                    openingCrawl
                    releaseYear
                    director
                    producers
                    planets {
                        edges {
                            node {
                                name
                            }
                        }
                    }
                }
            }
        }
    """
    expected = {
        "insertMovie": {
            "movie": {
                "title": "Attack of the Clones",
                "episodeId": 2,
                "openingCrawl": "There is unrest in the Galactic Senate. Several thousand solar systems have declared their intentions to leave the Republic.  This separatist movement, under the leadership of the mysterious Count Dooku, has made it difficult for the limited number of Jedi Knights to maintain  peace and order in the galaxy.  Senator Amidala, the former Queen of Naboo, is returning to the Galactic Senate to vote on the critical issue of creating an ARMY OF THE REPUBLIC to assist the overwhelmed Jedi....",
                "releaseYear": 2002,
                "director": "George Lucas",
                "producers": "Rick McCallum",
                "planets": {
                    "edges": [
                        {
                            "node": {
                                "name": "Utapau"
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
    print("test_mutation_movie OK")


test_mutation_movie()
