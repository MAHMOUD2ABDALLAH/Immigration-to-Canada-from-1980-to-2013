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
print('dimensions before:', df_Canada.shape)
years = list(map(str, range(1980, 2014)))
# Rename columns
df_Canada.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
df_Canada.set_index('Country', inplace=True)

# Ensure columns are strings
df_Canada.columns = df_Canada.columns.map(str)
# Clean up the dataset to remove columns that are not informative to us for visualization.
df_Canada.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
print(df_Canada.head())
print("---------------------------------------------------------------------------------------------------")
# let's examine the types of the column labels
types = all(isinstance(column, str) for column in df_Canada.columns)
print(types)
print("---------------------------------------------------------------------------------------------------")
# Add total column
df_Canada['Total'] = df_Canada.select_dtypes(include='number').sum(axis=1)
print(df_Canada['Total'])
print("---------------------------------------------------------------------------------------------------")
print('dimensions after:', df_Canada.shape,
      'Because of dropping 5 informative columns and 1 total column added and setting index for country 1 = 43-5+1-1=38 ')
print("--------------------------------------get the top 5 entries----------------------------------------")
df_Canada = df_Canada.sort_values(['Total'], ascending=False, axis=0)
df_top = df_Canada.head()
df_top = df_top[years].transpose()
print(df_top.head())
print("-------------let's change the index values of df_top5 to type integer for plotting-----------------")
df_top.index = df_top.index.map(int)
df_top.plot(kind='area', alpha=1, figsize=(10, 5))
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.text(2007, 42000, "alpha=1 for better visualization")
plt.show()
print("------------------------get the 5 countries with the least contribution----------------------------")

# get the 5 countries with the least contribution
df_least5 = df_Canada.tail(5)
df_least5 = df_least5[years].transpose()
df_least5.index = df_least5.index.map(int)
df_least5.plot(kind='area', alpha=1, figsize=(10, 5))
plt.title('Immigration Trend of 5 Countries with Least Contribution to Immigration')
plt.ylabel('Number of Immigrants in thousands')
plt.xlabel('Years')
plt.show()
