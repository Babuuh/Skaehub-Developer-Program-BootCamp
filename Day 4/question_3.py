from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

def city_state_country(coord):

    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return city, state, country

print(city_state_country("0.0917° S, 34.7680° E"))