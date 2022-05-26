OSM_QUERY = """
    area["ISO3166-1"={country}][admin_level={admin_level}];
    (node["{key}"={value}](area);
    rel["{key}"={value}](area);
    );
    out center;
    """
