def city_country(city, country, population):
    """A simple function that takes in a city name and the country and returns a neatly formatted output."""
    joined = f"{city} {country} - {population}"
    return joined.title()


asia = city_country("Beijing", "China", 1000000)
print(asia)
