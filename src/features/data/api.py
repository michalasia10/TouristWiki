import overpass

# with open("./test.geo.json", mode="w") as f:
#     geojson.dump(res, f)

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
