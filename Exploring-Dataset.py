# The dataset contains annual data on the flows of international immigrants as recorded by the countries of destination.
# The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals.
# The current version presents data pertaining to 45 countries.

import numpy as np
import pandas as pd
import openpyxl
import os

repo_path = os.path.expanduser('Canada.xlsx')

df_Canada = pd.read_excel(
    os.path.join(repo_path),
    skiprows=range(20),
    skipfooter=29
)
print('Data downloaded and read into a dataframe!')
print("---------------------------------------------------------------------------------------------------")
# Getting first 5 rows of the dataset
print(df_Canada.head())
print("---------------------------------------------------------------------------------------------------")
# View the bottom 5 rows of the dataset
print(df_Canada.tail())
print("---------------------------------------------------------------------------------------------------")
# Short summary about the dataframe
df_Canada.info(verbose=False)
print("---------------------------------------------------------------------------------------------------")
# Knowing headers
print(df_Canada.columns)
print("---------------------------------------------------------------------------------------------------")
# getting Indices
print(df_Canada.index)
print("---------------------------------------------------------------------------------------------------")
# Changing index and columns to list
print(type(df_Canada.columns.tolist()), type(df_Canada.index.tolist()))
print("---------------------------------------------------------------------------------------------------")
# Showing the shape of the dataset
print(df_Canada.shape)
print("---------------------------------------------------------------------------------------------------")
# Cleaning unnecessary and null values from it
df_Canada.dropna(axis=1, inplace=True)
print(df_Canada)
print("---------------------------------------------------------------------------------------------------")
# using Dic to rename the headers of dataset (feature)
df_Canada.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
print(df_Canada.columns)
print("---------------------------------------------------------------------------------------------------")
# add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013
df_Canada['Total'] = df_Canada.sum(axis=1, numeric_only=True)
print(df_Canada)
print("---------------------------------------------------------------------------------------------------")
# check to see how many null objects we have in the dataset
print(df_Canada.isnull().sum())
print("---------------------------------------------------------------------------------------------------")
# Finally, let's view a quick summary of each column in our dataframe
print(df_Canada.describe())
print("---------------------------------------------------------------------------------------------------")
