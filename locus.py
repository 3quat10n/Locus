import pandas as pd
import folium
from folium.plugins import MiniMap, Fullscreen

print('\t"Big Brother is watching you"\n\t\t\t-George Orwell')

db_file = "france_cam.csv"

lat_m, lon_m = map(float, input("[+]Enter min latitude and min longitude: ").split(","))
lat_M, lon_M = map(float, input("[+]Enter max latitude and max longitude: ").split(","))
circle_radius = float(input("[+]Enter cercle radius: "))

count = 0

map_object = folium.Map(location=[0.5*(lat_m+lat_M), 0.5*(lon_m+lon_M)], zoom_start=13)
dataFrame = pd.read_csv("db/"+db_file, sep=';',encoding="UTF-8")

print("[+]db File:",db_file)
print("[+]Searching ...")

def is_in_area(lat, lon):
    return lat_m <= lat <= lat_M and lon_m <= lon <= lon_M

def plot(n,latitude, longitude):
    # Plot point on the map
    folium.Marker(location=[latitude, longitude],popup=n,icon=folium.Icon(color="blue", icon="camera", prefix="fa")).add_to(map_object)
    folium.Circle(
        location=[latitude, longitude],
        radius=circle_radius,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.2,
        weight=1
    ).add_to(map_object)

for _, row in dataFrame.iterrows():
    if is_in_area(row["lat"],row["lon"]):
        plot((row["lat"],row["lon"]),row["lat"],row["lon"])
        count+=1

print("[+]N° Of Systems Found:",count)
file_name = str(0.5*(lat_m+lat_M))+str(0.5*(lon_m+lon_M))+"_map.html"
map_object.save(file_name)
print("[+]File",file_name,"Created")
