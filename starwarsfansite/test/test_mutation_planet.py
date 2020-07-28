import pytest
from ..schema import schema

pytestmark = pytest.mark.django_db


def test_mutation_planet():
    mutation = """
        mutation MyMutation {
            insertPlanet( input: { 
                clientMutationId: "1",
                name: "Utapau",
                climate: "temperate, arid, windy",
                terrain: "scrublands, savanna, canyons, sinkholes",
                population: 95000000,
            }) {
                planet {
                    name
                    climate
                    terrain
                    population
                }
            }
        }
    """
    expected = {
        "insertPlanet": {
            "planet": {
                "name": "Utapau",
                "climate": "temperate, arid, windy",
                "terrain": "scrublands, savanna, canyons, sinkholes",
                "population": 95000000
            }
        }
    }
    result = schema.execute(mutation)
    assert not result.errors
    assert result.data == expected
    print("test_mutation_planet OK")


test_mutation_planet()
