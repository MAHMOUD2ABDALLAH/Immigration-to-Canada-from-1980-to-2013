# Question: What is the frequency distribution of the number (population) of new immigrants from the various countries to Canada in 2013?

from string import printable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

repo_path = os.path.expanduser("Canada.xlsx")

df_Canada = pd.read_excel(os.path.join(repo_path), skiprows=range(20), skipfooter=29)
print("Data downloaded and read into a dataframe!")
print("dimensions before:", df_Canada.shape)
years = list(map(str, range(1980, 2014)))
# Rename columns
df_Canada.rename(
    columns={"OdName": "Country", "AreaName": "Continent", "RegName": "Region"},
    inplace=True,
)
df_Canada.set_index("Country", inplace=True)

# Ensure columns are strings
df_Canada.columns = df_Canada.columns.map(str)
# Clean up the dataset to remove columns that are not informative to us for visualization.
df_Canada.drop(["AREA", "REG", "DEV", "Type", "Coverage"], axis=1, inplace=True)
print(df_Canada.head())
print(
    "---------------------------------------------------------------------------------------------------"
)
# let's examine the types of the column labels
types = all(isinstance(column, str) for column in df_Canada.columns)
print(types)
print(
    "---------------------------------------------------------------------------------------------------"
)
# Add total column
df_Canada["Total"] = df_Canada.select_dtypes(include="number").sum(axis=1)
print(df_Canada["Total"])
print(
    "---------------------------------------------------------------------------------------------------"
)
print(
    "dimensions after:",
    df_Canada.shape,
    "Because of dropping 5 informative columns and 1 total column added and setting index for country 1 = 43-5+1-1=38 ",
)
print(
    "--------------------------------------get the top 5 entries----------------------------------------"
)
df_Canada = df_Canada.sort_values(["Total"], ascending=False, axis=0)
df_top = df_Canada.head()
df_top = df_top[years].transpose()
print(df_top.head())
print(
    "---------------------------------------------------------------------------------------------------"
)
# Before we proceed with creating the histogram plot, let's first examine the data split into intervals.
print(df_Canada["2013"].head())
print(
    "---------------------------------------------------------------------------------------------------"
)
# in this part we decide the parts of the histogram range=(0 to max immigrants) and frequency(bins number 0 - 10) only in 2013
count, bin_edges = np.histogram(df_Canada["2013"])
print(count)
print(bin_edges)
print(
    "---------------------------------------------------------------------------------------------------"
)
df_Canada["2013"].plot(kind="hist", figsize=(8, 5), xticks=bin_edges)
plt.title("Histogram of Immigration from 195 Countries in 2013")
plt.ylabel("Number of Countries")
plt.xlabel("Number of Immigrants")
plt.show()

# view the dataset
print(df_Canada.loc[["Denmark", "Norway", "Sweden"], years])
# generate histogram
df_Canada.loc[["Denmark", "Norway", "Sweden"], years].plot(kind="hist", figsize=(8, 5))
plt.title("Immigration from Denmark, Norway, and Sweden (1980-2013)")
plt.legend(fontsize=5, loc="upper right", bbox_to_anchor=(1, 1), borderpad=0.5)

plt.xlabel("Number of Immigrants")
plt.ylabel("Frequency")
plt.show()


# Instead of plotting the population frequency distribution of the population for the 3 countries
#  pandas instead plotted the population frequency distribution for the years

# transpose dataframe
df_scandinavia = df_Canada.loc[["Denmark", "Norway", "Sweden"], years].transpose()
print(df_scandinavia.head())

# generate histogram
df_scandinavia.plot(kind="hist", figsize=(10, 6))

plt.title("Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013")
plt.ylabel("Number of Years")
plt.xlabel("Number of Immigrants")

plt.show()

# Let's make a few modifications to improve the impact and aesthetics of the previous plot
# let's get the x-tick values
count, bin_edges = np.histogram(df_scandinavia, 15)

# un-stacked histogram
df_scandinavia.plot(
    kind="hist",
    figsize=(10, 6),
    bins=15,
    alpha=0.6,
    xticks=bin_edges,
    color=["coral", "darkslateblue", "mediumseagreen"],
)

plt.title("Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013")
plt.ylabel("Number of Years")
plt.xlabel("Number of Immigrants")
plt.show()

# stacked histogram
count, bin_edges = np.histogram(df_scandinavia, 15)
xmin = (
    bin_edges[0] - 10
)  #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes
xmax = (
    bin_edges[-1] + 10
)  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes

# stacked Histogram
df_scandinavia.plot(
    kind="hist",
    figsize=(10, 6),
    bins=15,
    xticks=bin_edges,
    color=["coral", "darkslateblue", "mediumseagreen"],
    stacked=True,
    xlim=(xmin, xmax),
)

plt.title("Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013")
plt.ylabel("Number of Years")
plt.xlabel("Number of Immigrants")

plt.show()

# Use the scripting layer to display the immigration distribution for Greece, Albania, and Bulgaria for years 1980 - 2013?
# Use an overlapping plot with 15 bins and a transparency value of 0.35.

# create a dataframe of the countries of interest (cof)
df_cof = df_Canada.loc[['Greece', 'Albania', 'Bulgaria'], years]
df_cof = df_cof.transpose() 
count, bin_edges = np.histogram(df_cof, 15)

# Un-stacked Histogram
df_cof.plot(kind ='hist',
                figsize=(10, 6),
                bins=15,
                alpha=0.35,
                xticks=bin_edges,
                color=['coral', 'darkslateblue', 'mediumseagreen']
                )

plt.title('Histogram of Immigration from Greece, Albania, and Bulgaria from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()

