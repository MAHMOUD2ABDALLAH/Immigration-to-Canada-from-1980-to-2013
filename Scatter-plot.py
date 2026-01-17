from pkgutil import extend_path
from string import printable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
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

# Using a scatter plot,
# let's visualize the trend of total immigrantion to Canada (all countries combined) for the years 1980 - 2013.

# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_Canada[years].sum(axis=0))

# change the years to type int (useful for regression later on)
df_tot.index = map(int, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ["year", "total"]

# view the final dataframe
print(df_tot.head())

# create scatter plot
df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='red')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

# plt.show()

#let's try to plot a linear line of best fit, and use it to predict the number of immigrants in 2015 ( y= a * x + b).
x = df_tot['year']      # year on x-axis
y = df_tot['total']     # total on y-axis
fit = np.polyfit(x, y, deg=1)

print(fit)

# plot line of best fit
plt.plot(x, fit[0] * x + fit[1], color='green') # recall that x is the Years
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

plt.show()

# print out the line of best fit
print('No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1])) 

# Create a scatter plot of the total immigration from Denmark, Norway, and Sweden to Canada from 1980 to 2013

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

# show resulting dataframe
print(df_total.head())

# generate scatter plot
df_total.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='orange')

# add title and label to axes
plt.title('Immigration from Denmark, Norway, and Sweden to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

# show plot
plt.show()