#### Indexing and Selection (slicing)===============================================================
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
# before we start to filter we should rename the main headers we need
df_Canada.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
print("---------------------------------------------------------------------------------------------------")
# Filtering on the list of countries
print(df_Canada.Country)
print("---------------------------------------------------------------------------------------------------")
# filtering on the list of countries ('Country') and the data for years: 1980 - 1985
print(df_Canada[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])
print("---------------------------------------------------------------------------------------------------")
# setting the 'Country' column as the index to get the data of each country as itself
df_Canada.set_index('Country', inplace=True)
print(df_Canada.head(3))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++Let's Start+++++++++++++++++++++++++++++++++++++++++++++++++
print("---------------------------1. The full row data (all columns)------------------")
print(df_Canada.loc['Japan'])
print("---------------------------2. for year 2013-----------------------------------")
print(df_Canada.loc['Japan', 2013])
print("---------------------------3. for years 1980 to 1985---------------------------")
print(df_Canada.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1985]])
# if I know the index of each features in table i can use
# Alternative Method
# df_can.iloc[87, [3, 4, 5, 6, 7, 8]]
print("---------------------------------------------------------------------------------------------------")
# let's convert the column names into strings: '1980' to '2013',to avoid this ambuigity.
df_Canada.columns = list(map(str, df_Canada.columns))
for i in df_Canada.columns:
    print(type(i))
print("---------------------------------------------------------------------------------------------------")
# Let's filter the dataframe to show the data on Asian countries (AreaName = Asia).
print("------------------------------1. create the condition boolean series-------------------------------")
condition = df_Canada['Continent'] == 'Asia'
print(condition)
print("------------------------------2. pass this condition into the dataFrame----------------------------")
print(df_Canada[condition])
print("------------------------------3. passing multiple criteria in the dataFrame----------------------------")
condition2 = df_Canada[(df_Canada['Continent'] == 'Asia') & (df_Canada['Region'] == 'Southern Asia')]
print(condition2)
print("-------------------------------------------------------------------------------------------------------")
# finally lets review the changes we made
print('data dimensions:', df_Canada.shape)
print(df_Canada.columns)
print(df_Canada.head(5))