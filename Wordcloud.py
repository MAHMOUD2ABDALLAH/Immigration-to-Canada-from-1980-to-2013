from pkgutil import extend_path
from string import printable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as mcolors
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

# Let's revisit the previous case study about Denmark, Norway, and Sweden.
df_dsn = df_Canada.loc[["Denmark", "Norway", "Sweden"], :]
print(df_dsn)

# Now, let's plot a waffle chart, we will learn how to create them from scratch.
# Step 1___________________________________________________________
# compute the proportion of each category with respect to the total
total_values = df_dsn["Total"].sum()
category_proportions = df_dsn["Total"] / total_values

# print out proportions
print(pd.DataFrame({"Category Proportion": category_proportions}))

# Step 2__________________________________________________________
# The second step is defining the overall size of the waffle chart.
width = 40
height = 10

total_num_tiles = width * height  # total number of tiles

print(f"\nTotal number of tiles is {total_num_tiles}.")
# Step 3__________________________________________________________________________________________
# The third step is using the proportion of each category to determe it respective number of tiles
# compute the number of tiles for each category
tiles_per_category = (category_proportions * total_num_tiles).round().astype(int)
# print out number of tiles per category
print(pd.DataFrame({"Number of tiles": tiles_per_category}))

# Step 4________________________________________________________________________________
# The fourth step is creating a matrix that resembles the waffle chart and populating it
# initialize the waffle chart as an empty matrix
waffle_chart = np.zeros((height, width), dtype=np.uint)

# define indices to loop through waffle chart
category_index = 0
tile_index = 0

# populate the waffle chart
for col in range(width):
    for row in range(height):
        tile_index += 1

        # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
        if tile_index > sum(tiles_per_category[0:category_index]):
            # ...proceed to the next category
            category_index += 1

        # set the class value to an integer, which increases with class
        waffle_chart[row, col] = category_index

print("\nWaffle chart populated!\n", waffle_chart)

# Step 5_________________________________
# use matshow to display the waffle chart

# Define Scandinavian flag colors
colors = ["#C60C30", "#FECC00", "#00205B"]  # Denmark  # Sweden  # Norway

# Create custom colormap
scandi_cmap = mcolors.LinearSegmentedColormap.from_list("scandi_flags", colors)

# Minimize figure dimensions
plt.figure(figsize=(8, 2))  # Smaller figure size
plt.matshow(waffle_chart, cmap=scandi_cmap, fignum=plt.gcf().number)
plt.colorbar(shrink=0.8)  # Make colorbar smaller too
plt.tight_layout()  # Adjust layout to minimize white space
plt.show()

# Step 6____________
# Prettify the chart
# Minimize figure dimensions
plt.figure(figsize=(8, 2))  # Smaller figure size

# use matshow to display the waffle chart
plt.matshow(waffle_chart, cmap=scandi_cmap, fignum=plt.gcf().number)
plt.colorbar(shrink=0.8)  # Make colorbar smaller

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(0.5, (width), 1), minor=True)
ax.set_yticks(np.arange(0.5, (height), 1), minor=True)

# add gridlines based on minor ticks
ax.grid(which="minor", color="w", linestyle="-", linewidth=1)

plt.xticks([])
plt.yticks([])
plt.tight_layout()  # Minimize white space
plt.show()

# step 7______
# Add a legend
# compute cumulative sum of individual categories to match color schemes between chart and legend

# Minimize figure dimensions - slightly larger to accommodate legend
plt.figure(figsize=(9, 2.5))  # Adjusted for legend

plt.matshow(waffle_chart, cmap=scandi_cmap, fignum=plt.gcf().number)
plt.colorbar(shrink=0.8)  # Make colorbar smaller

# get the axis
ax = plt.gca()

# set minor ticks
ax.set_xticks(np.arange(0.5, (width), 1), minor=True)
ax.set_yticks(np.arange(0.5, (height), 1), minor=True)

# add gridlines based on minor ticks
ax.grid(which="minor", color="w", linestyle="-", linewidth=1)

plt.xticks([])
plt.yticks([])

# Create legend
# Create proxy artists for the legend
legend_elements = [
    plt.Rectangle((0, 0), 1, 1, facecolor=colors[i], edgecolor="w", linewidth=0.5)
    for i in range(len(df_dsn))
]

# Get the category names from the dataframe
category_names = df_dsn.index.tolist()

# Add the legend to the chart
ax.legend(
    legend_elements,
    category_names,
    loc="best",
    bbox_to_anchor=(1.0, 1.0),
    title="Countries",
    fontsize=8,  # Smaller font
    title_fontsize=10,  # Smaller title font
    frameon=True,
    fancybox=True,
    shadow=True,
)

# Adjust layout to make room for the legend
plt.tight_layout()
plt.title("Waffle Chart of Scandinavian Countries", fontsize=10)  # Smaller title
plt.show()