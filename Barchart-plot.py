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
#The 2008 - 2011 Icelandic Financial Crisis was a major economic and political event in Iceland. 
#Relative to the size of its economy, Iceland's systemic banking collapse was the largest experienced by any country in economic history.
#The crisis led to a severe economic depression in 2008 - 2011 and significant political unrest.

# Let's compare the number of Icelandic immigrants (country = 'Iceland') to Canada from year 1980 to 2013.
df_iceland = df_Canada.loc['Iceland', years]
print(df_iceland.tail())

# plot data
df_iceland.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot

plt.show()

# The bar plot above shows the total number of immigrants broken down by each year. We can clearly see the impact of the financial crisis; the number of immigrants to Canada started increasing rapidly after 2008.

# Let's annotate this on the plot using the annotate method of the scripting layer or the pyplot interface. We will pass in the following parameters:

# s: str, the text of annotation.
# xy: Tuple specifying the (x,y) point to annotate (in this case, end point of arrow).
# xytext: Tuple specifying the (x,y) point to place the text (in this case, start point of arrow).
# xycoords: The coordinate system that xy is given in - 'data' uses the coordinate system of the object being annotated (default).
# arrowprops: Takes a dictionary of properties to draw the arrow:
# arrowstyle: Specifies the arrow style, '->' is standard arrow.
# connectionstyle: Specifies the connection type. arc3 is a straight line.
# color: Specifies color of arrow.
# lw: Specifies the line width.

df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)  # rotate the xticks(labelled points on x-axis) by 90 degrees

plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',  # s: str. Will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )
# Annotate text
plt.annotate('2008 - 2011 Financial Crisis',  # text to display
             xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
             rotation=72.5,  # based on trial and error to match the arrow
             va='bottom',  # want the text to be vertically 'bottom' aligned
             ha='left',  # want the text to be horizontally 'left' algned.
             )

plt.show()
