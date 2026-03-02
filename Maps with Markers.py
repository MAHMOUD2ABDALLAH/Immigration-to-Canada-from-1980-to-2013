from pkgutil import extend_path
from string import printable
from turtle import color
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import folium
from folium import plugins
import os

repo_path = os.path.expanduser("Police_Department_Incidents_-_Previous_Year__2016_.csv")

df_Police = pd.read_csv(os.path.join(repo_path))
print(df_Police.head())
print("Data downloaded and read into a dataframe!")

# IncidntNum: Incident Number
# Category: Category of crime or incident
# Descript: Description of the crime or incident
# DayOfWeek: The day of week on which the incident occurred
# Date: The Date on which the incident occurred
# Time: The time of day on which the incident occurred
# PdDistrict: The police department district
# Resolution: The resolution of the crime in terms whether the perpetrator was arrested or not
# Address: The closest address to where the incident took place
# X: The longitude value of the crime location
# Y: The latitude value of the crime location
# Location: A tuple of the latitude and the longitude values
# PdId: The police department ID

print(df_Police.shape)
#  let's just work with the first 100 incidents in this dataset.
df_Police = df_Police.iloc[0:100, :]
print(df_Police.shape)

# Let's create a map of San Francisco and plot the locations of the crimes on it.
# Create a map of San Francisco
latitude = 37.77
longitude = -122.42
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)
# print(sanfran_map.show_in_browser())
# sanfran_map.save("sanfran_map.html")

# Add markers to the map
incidents = folium.map.FeatureGroup()
# loop through the 100 crimes and add each to the incidents feature group
for (
    lat,
    lng,
) in zip(df_Police.Y, df_Police.X):
    incidents.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=7.5,
            color="black",
            fill=True,
            fill_color="red",
            fill_opacity=10,
        )
    )

# add incidents to map
sanfran_map.add_child(incidents)
# print(sanfran_map.show_in_browser())
# sanfran_map.save("sanfran_crimes_map.html")


# Add markers to the map
incidents = folium.map.FeatureGroup()
# loop through the 100 crimes and add each to the incidents feature group
for (
    lat,
    lng,
) in zip(df_Police.Y, df_Police.X):
    incidents.add_child(
        folium.features.CircleMarker(
            [lat, lng],
            radius=7.5,
            color="black",
            fill=True,
            fill_color="red",
            fill_opacity=10,
        )
    )


# add pop-up text to each marker on the map
latitudes = list(df_Police.Y)
longitudes = list(df_Police.X)
labels = list(df_Police.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker(
        [lat, lng], popup=label, icon=folium.Icon(color="red", icon="exclamation-sign")
    ).add_to(sanfran_map)

# add incidents to map
sanfran_map.add_child(incidents)
# print(sanfran_map.show_in_browser())
# sanfran_map.save("sanfran_crimes_map_markers.html")




# let's just work with the first 100 incidents in this dataset.
# Create clusters to group nearby crime markers on the map
# Each cluster shows the total number of crimes in that neighborhood
# This helps identify high-crime "pockets" in San Francisco for separate analysis
# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)
incidents = plugins.MarkerCluster().add_to(sanfran_map)
for lat, lng, label, in zip(df_Police.Y, df_Police.X, df_Police.Category):
    folium.Marker(
        location=[lat, lng],
        icon=folium.Icon(color="red", icon="exclamation-sign"),
        popup=label,
    ).add_to(incidents)

print(sanfran_map.show_in_browser())
sanfran_map.save("sanfran_crimes_map_markers_clustered.html")