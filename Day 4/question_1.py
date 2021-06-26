from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="geoapiExercises")

zipcode = str(input('Enter a valid zipcode:'))

print(zipcode)
location = geolocator.geocode(zipcode)
print("Details of the said pincode:")
print(location.address) 
