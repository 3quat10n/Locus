from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.reverse((48.8584,2.2945), language="fr")

rue = location.raw.get("address", {}).get("road", None)
print(rue)

