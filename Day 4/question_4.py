from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

state = str(input('Enter a State: '))
print("State Name:",state)
location = geolocator.geocode(state)
print("State/Country: ", location.address)
