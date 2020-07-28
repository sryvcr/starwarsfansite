import pytest
from ..schema import schema

pytestmark = pytest.mark.django_db


def test_get_planets_by_name():
    query = """
        query {
            allPlanets(name_Icontains: "Alderaan") {
                edges {
                    node {
                        name,
                        climate,
                        terrain,
                        population
                    }
                }
            }
        }
    """
    expected = {
        "allPlanets": {
            "edges": [
                {
                    "node": {
                        "name": "Alderaan",
                        "climate": "temperate",
                        "terrain": "grasslands, mountains",
                        "population": 2000000000
                    }
                }
            ]
        }
    }
    result = schema.execute(query)
    assert not result.errors
    assert result.data == expected
    print("test_get_planets_by_name OK")


test_get_planets_by_name()
