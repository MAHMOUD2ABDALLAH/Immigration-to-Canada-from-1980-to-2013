from pkgutil import extend_path
from string import printable
import numpy as np
import pandas as pd
import seaborn as sns
import json
import os
import folium

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

# add total column
df_Canada["Total"] = df_Canada.select_dtypes(include="number").sum(axis=1)

# let's view the first five elements and see how the dataframe was changed
print(df_Canada.head())
print(df_Canada.shape)
#__________________________________________________________________________________

# Load the GeoJSON file
repo_path = os.path.expanduser("world_countries.json")  # Adjust filename

# Load GeoJSON for the map
with open(repo_path, 'r') as file:
    df_world = json.load(file)

# create a plain world map
world_map = folium.Map(location=[0, 0], zoom_start=2)
# generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
# Generate choropleth map using folium.Choropleth (not as a method)
choropleth_layer = folium.Choropleth(
    geo_data=df_world,
    data=df_Canada,  # Note: you had "data_df_can" but should be your dataframe variable
    columns=["Country", "Total"],
    key_on="feature.properties.name",  # Use the correct key from your GeoJSON
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Immigration to Canada"
).add_to(world_map)  # Add the choropleth layer to the map

# display map
world_map.show_in_browser()
# world_map.save("choropleth_world_map.html")

