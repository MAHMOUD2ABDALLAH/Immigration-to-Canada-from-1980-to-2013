import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import folium

# define the world map
world_map = folium.Map()

# define the world map centered around Canada with a low zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
# print(world_map.show_in_browser())
# world_map.save("world_map.html")

# define the world map centered around Canada with a higher zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)
# print(world_map.show_in_browser())
# world_map.save("world_map.html")

# define Mexico's geolocation coordinates
mexico_latitude = 23.6345
mexico_longitude = -102.5528

# define the world map centered around Canada with a higher zoom level
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=4)
# print(mexico_map.show_in_browser())
# world_map.save("mexico_map.html")

# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(
    location=[56.130, -106.35], zoom_start=4, tiles="CartoDB positron"
)

# print(world_map.show_in_browser())
# world_map.save("Toner_map.html")

# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(
    location=[56.130, -106.35], zoom_start=4, tiles="CartoDB voyager"
)
# print(world_map.show_in_browser())
# world_map.save("Terrain_map.html")

#define Mexico's geolocation coordinates
mexico_latitude = 23.6345 
mexico_longitude = -102.5528

# define the world map centered around Canada with a higher zoom level
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=6, tiles='CartoDB voyager')

print(mexico_map.show_in_browser())
mexico_map.save("mexico_Terrain_map_.html")
