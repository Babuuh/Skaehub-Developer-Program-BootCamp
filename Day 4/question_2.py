from geopy import distance
nairobi = ("1.2921° S, 36.8219° E")
cairo = ("30.0444° N, 31.2357° E")
print("The distance between Nairobi and Cairo is: ", distance.distance(nairobi, cairo).km," kms")