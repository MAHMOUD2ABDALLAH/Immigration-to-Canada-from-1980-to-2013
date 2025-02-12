# The dataset contains annual data on the flows of international immigrants as recorded by the countries of destination.
# The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals.
# The current version presents data pertaining to 45 countries.

import numpy as np
import pandas as pd
import openpyxl

df_Canada = pd.read_excel(
    'C:\\Users\Mahmoud\Microsoft-PowerUp\Mahmoud Mohamed Abdallah - Documents\introDataAnalyse\Canada.xlsx',
    skiprows=range(20), skipfooter=2)
print('Data downloaded and read into a dataframe!')

# Getting first 5 rows of the dataset
print(df_Canada.head())

# View the bottom 5 rows of the dataset
print(df_Canada.tail())

# Short summary about the dataframe
df_Canada.info(verbose=False)

# Knowing headers
print(df_Canada.columns)

# getting Indices
print(df_Canada.index)

# Changing index and columns to list
print(type(df_Canada.columns.tolist()), type(df_Canada.index.tolist()))

# Showing the shape of the dataset
print(df_Canada.shape)

# Cleaning unnecessary and null values from it
df_Canada.dropna(axis=1, inplace=True)
print(df_Canada)

# using Dic to rename the headers of dataset (feature)
df_Canada.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
print(df_Canada.columns)

# add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013
df_Canada['Total'] = df_Canada.sum(axis=1, numeric_only=True)
print(df_Canada)

# check to see how many null objects we have in the dataset
print(df_Canada.isnull().sum())

# Finally, let's view a quick summary of each column in our dataframe
print(df_Canada.describe())
