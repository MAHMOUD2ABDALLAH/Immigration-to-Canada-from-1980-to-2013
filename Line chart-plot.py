# In 2010, Haiti suffered a catastrophic magnitude 7.0 earthquake.
# The quake caused widespread devastation and loss of life and aout three million people were affected by this natural disaster.
# As part of Canada's humanitarian effort, the Government of Canada stepped up its effort in accepting refugees from Haiti.
# We can quickly visualize this effort using a Line plot:
from pkgutil import extend_path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

repo_path = os.path.expanduser('Canada.xlsx')

df_Canada = pd.read_excel(
    os.path.join(repo_path),
    skiprows=range(20),
    skipfooter=29
)

print('Data downloaded and read into a dataframe!')

years = list(map(str, range(1980, 2014)))
# Rename columns
df_Canada.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
df_Canada.set_index('Country', inplace=True)

# Ensure columns are strings
df_Canada.columns = df_Canada.columns.map(str)

# First, we will extract the data series for Haiti.
haiti = df_Canada.loc['Haiti', years]
print(haiti.head())
# let's change the index values of Haiti to type integer for plotting
haiti.index = haiti.index.map(int)
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.grid(True)
print("---------------------------------------------------------------------------------------------------")
# We can clearly observe a significant increase in the number of immigrants from Haiti starting in 2010,
# coinciding with Canada's increased efforts to accept Haitian refugees.
print("------------------------------Let's annotate this spike on the plot.-------------------------------")
plt.text(2000, 6000, "2010 Earthquake")
plt.show()

# We can easily add more countries to line plot to make meaningful comparisons immigration from different countries.
print("--------Let's compare the number of immigrants from India and China from 1980 to 2013.-------------")
# Let's compare the number of immigrants from India and China from 1980 to 2013.
df_CI = df_Canada.loc[['India', 'China'], years]
print(df_CI.head())
print("---------------------------------------------------------------------------------------------------")
# we must first transpose the dataframe to swap the row and columns.
df_CI = df_CI.transpose()
print(df_CI.head())
df_CI.index = df_CI.index.map(int)
df_CI.plot(kind='line')
plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()