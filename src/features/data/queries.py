

RESTAURANTS_QUERY = """
    area["ISO3166-1"={country}][admin_level={level}];
    (node["amenity"={category}](area);
    rel["amenity"={category}](area);
    );
    out center;
    """