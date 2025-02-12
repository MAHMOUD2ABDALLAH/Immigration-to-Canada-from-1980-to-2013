#### Indexing and Selection (slicing)===============================================================
import numpy as np
import pandas as pd
import openpyxl

df_Canada = pd.read_excel(
    'C:\\Users\Mahmoud\Microsoft-PowerUp\Mahmoud Mohamed Abdallah - Documents\introDataAnalyse\Canada.xlsx',
    skiprows=range(20), skipfooter=2)
print('Data downloaded and read into a dataframe!')

# before we start to filter we should rename the main headers we need
df_Canada.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)

# Filtering on the list of countries
print(df_Canada.Country)

# filtering on the list of countries ('Country') and the data for years: 1980 - 1985
print(df_Canada[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])

# setting the 'Country' column as the index to get the data of each country as itself
df_Canada.set_index('Country', inplace=True)
print(df_Canada.head(3))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++Let's us Start+++++++++++++++++++++++++++++++++++++++++++++++++

# 1. The full row data (all columns)

print(df_Canada.loc['Japan'])
df_Canada = df_Canada[df_Canada.index == 'Japan']  # showcase for data of Japan as index location in the table
print(df_Canada)

# 2. for year 2013
df_Canada = df_Canada.loc['Japan', 2013]
print(df_Canada)

# 3. for years 1980 to 1985
print(df_Canada.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1985]])