import overpass

from src.core.database import client
from src.features.data.queries import RESTAURANTS_QUERY


def osm_query(category: str, level: int, country: str):
    api = overpass.API(timeout=500)

    """pobranie danych z OSM o restauracjach w Polsce """
    res = api.get(RESTAURANTS_QUERY.format(category=category, level=level, country=country))

    return res


results = osm_query(category="restaurant", level=2, country="PL")
# osm_query(category="", level=2, country=" PL")


def data_to_db():
    """estabiling connection"""
    connect = client
    """connecting to DB"""
    db = connect.get_database('new_database')
    """connection to collection"""
    collection = db.new_collection
    """inserting data"""
    collection.insert_one(results)
    """checking if data is inserted corectly"""
    cursor = collection.find()
    print(cursor)
    """sprawdzenie co jest w kolekcji"""
    for x in collection.find():
        print(x)
    """zamknięcie połączenia"""
    connect.close()


data_to_db()
