from pkgutil import extend_path
from string import printable
import numpy as np
import pandas as pd
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

total_immigration = df_Canada['Total'].sum()
print(f"Total Immigration: {total_immigration}")

# Create a frequency dictionary instead of duplicate strings
word_frequencies = {}

for country in df_Canada.index.values:
    # Check if country's name is a single-word name
    if country.count(" ") == 0:
        # Use the actual immigration number as the frequency
        word_frequencies[country] = df_Canada.loc[country, 'Total']

# Display the frequencies
print("Country Frequencies:")
for country, freq in list(word_frequencies.items()):
    print(f"{country}: {freq}")

# Create the word cloud using frequencies
wordcloud = WordCloud(background_color='white', width=800, height=400, random_state=10)
wordcloud.generate_from_frequencies(word_frequencies)

print('Word cloud created with no duplicates!')

# Display the cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Immigration by Country (1980-2013) - Each Country Once')
plt.show()