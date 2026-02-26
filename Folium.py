from pkgutil import extend_path
from string import printable
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import folium
import os

repo_path = os.path.expanduser("Canada.xlsx")

df_Canada = pd.read_excel(os.path.join(repo_path), skiprows=range(20), skipfooter=29)

print("Data downloaded and read into a dataframe!")

years = list(map(str, range(1980, 2014)))

# drop unnecessary columns
df_Canada.drop(["AREA", "REG", "DEV", "Type", "Coverage"], axis=1, inplace=True)
# rename columns
df_Canada.rename(
    columns={"OdName": "Country", "AreaName": "Continent", "RegName": "Region"},
    inplace=True,
)

# let's examine the types of the column labels
all(isinstance(column, str) for column in df_Canada.columns)

# it returns False, we need to convert them to strings
df_Canada.columns = list(map(str, df_Canada.columns))

# set the country name as index - useful for quickly looking up countries using .loc method
df_Canada.set_index("Country", inplace=True)

# add total column
df_Canada["Total"] = df_Canada.select_dtypes(include="number").sum(axis=1)

# let's view the first five elements and see how the dataframe was changed
print(df_Canada.head())

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
# world_map.save("mexico_Terrain_map_.html")
