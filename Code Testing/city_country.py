def city_country(city, country, population =""):
    """A simple function that takes in a city name and the country and returns a neatly formatted output."""
    if population:
        joined = f"{city} {country} - {population}"
        return joined.title()
    else:
        joined = f"{city} {country}"
        return joined.title()


asia = city_country("Beijing", "China", )
print(asia)
