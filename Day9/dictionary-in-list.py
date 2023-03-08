travel_log = [
    {
        "country": "France",
        'cities_visited':['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    {
        "country": "Germany",
        'cities_visited':['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
    },
]
#TODO: Write the function that will allow new countries
#to be added to the travel_log.

def add_new_country(country, cities, visits):
    new_country = {}
    new_country['country'] = country
    new_country['cities_visited'] = cities
    new_country['total_visits'] = visits
    travel_log.append(new_country)




#🚨 Do not change the code below
add_new_country(country = "Russia", visits = 2, cities = ["Moscow", "Saint Petersburg"])
print(travel_log)