import overpass

from main_app.src.core.database import word_objects_collection, db
from main_app.src.core.queries import OSM_QUERY


def osm_query(key: str, value: str, admin_level: int, country: str) -> list:
    """ Download data from osm by query """

    api = overpass.API(timeout=500)
    res = api.get(OSM_QUERY.format(key=key, value=value, admin_level=admin_level, country=country))

    return res['features']


def data_to_db(key: str, value: str, admin_level: int, country: str):
    result = osm_query(key, value, admin_level, country)
    return word_objects_collection.insert_many(result)
