def city_country(city, country, population=None, language=None):
    
    if population is not None and language is not None:
        return f"{city}, {country} - population {population}, {language}"
    elif language is None and population is not None:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"

print(city_country("Santiago", "Chile", 6100000,"Spanish"))
print(city_country ("Paris", "France", 2100000))
print(city_country ("Sydney", "Australia"))   