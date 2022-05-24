import overpass

from src.core.database import client
from src.core.settings import CONNECTION_STRING

"""zrobić funkcję: przyjmuje argument: kategoria, level, kraj
 funkcja zwraca jsona (res), nie plik! """


def osm_query(category: str, level: int, country: str):
    api = overpass.API(timeout=500)

    res = api.get("""
    area["ISO3166-1"={country}][admin_level={level}];
    (node["amenity"={category}](area);
    rel["amenity"={category}](area);
    );
    out center;
    """.format(category=category, level=level, country=country))

    return res


osm_query(category="restaurant", level=2, country=" PL")
osm_query(category="castle", level=2, country=" PL")


def data_to_db():
    client()
    db = client.get_database("TouristWiki")


    return
