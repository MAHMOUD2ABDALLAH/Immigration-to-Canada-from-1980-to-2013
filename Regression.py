from pkgutil import extend_path
from string import printable
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from wordcloud import WordCloud, STOPWORDS
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

# we will explore seaborn and see how efficient it is to create regression lines and fits using this library!
print('Seaborn installed and imported!')

# Create a new dataframe that stores that total number of landed immigrants to Canada per year from 1980 to 2013
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_Canada[years].sum(axis=0))

# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
print (df_tot.head())

# create a regression plot using seaborn
sns.regplot(x='year', y='total', data=df_tot)
plt.tight_layout()
plt.show()

# change the color of the regression line to green
sns.regplot(x='year', y='total', data=df_tot, color='green')
plt.tight_layout()
plt.show()

# change the marker to a plus sign
sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+')
plt.show()

# change the size of the figure to 12 by 8 inches
plt.figure(figsize=(12, 8))
sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+')
plt.show()

# change the size of the markers to 100 and add x- and y-labels and a title
plt.figure(figsize=(12, 8))
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 100})
ax.set(xlabel='Year', ylabel='Total Immigration') # add x- and y-labels
ax.set_title('Total Immigration to Canada from 1980 - 2013') # add title
plt.show()

# change the size of the font to 1.5
plt.figure(figsize=(12, 8))

sns.set(font_scale=1.5)
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 100})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()

# change the style of the plot to 'ticks'
plt.figure(figsize=(12, 8))
sns.set(font_scale=1.5)
sns.set_style('ticks')  
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 100})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()

# change the style of the plot to 'whitegrid'
plt.figure(figsize=(12, 8))
sns.set(font_scale=1.5)
sns.set_style('whitegrid')
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 100})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()

# create a regression plot with the total from Scandinavian countries to Canada from 1980 - 2013
# create df_countries dataframe
df_countries = df_Canada.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()

# create df_total by summing across three countries for each year
df_total = pd.DataFrame(df_countries.sum(axis=1))

# reset index in place
df_total.reset_index(inplace=True)

# rename columns
df_total.columns = ['year', 'total']

# change column year from string to int to create scatter plot
df_total['year'] = df_total['year'].astype(int)

# define figure size
plt.figure(figsize=(12, 8))

# define background style and font size
sns.set(font_scale=1.5)
sns.set_style('whitegrid')

# generate plot and add title and axes labels
ax = sns.regplot(x='year', y='total', data=df_total, color='green', marker='+', scatter_kws={'s': 100})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigrationn from Denmark, Sweden, and Norway to Canada from 1980 - 2013')
plt.show()
