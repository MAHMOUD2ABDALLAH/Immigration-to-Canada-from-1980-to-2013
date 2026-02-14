from pkgutil import extend_path
from string import printable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as mcolors
from wordcloud import WordCloud, STOPWORDS
import requests
import urllib.request
from PIL import Image

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/alice_novel.txt"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    alice_novel = response.text
    print(f"Successfully downloaded {len(alice_novel)} characters")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

stopwords = set(STOPWORDS)

# instantiate a word cloud object
alice_wc = WordCloud(background_color="white", max_words=2000, stopwords=stopwords)

# generate the word cloud
alice_wc.generate(alice_novel)

# display the word cloud
plt.imshow(alice_wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# "said" isn't really an informative word.
# So let's add it to our stopwords and re-generate the cloud.

stopwords.add("said")  # add the words said to stopwords

# re-generate the word cloud
alice_wc.generate(alice_novel)

# display the cloud

plt.imshow(alice_wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# Alice Mask
alice_mask = np.array(
    Image.open(
        urllib.request.urlopen(
            "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%204/images/alice_mask.png"
        )
    )
)
# Let's take a look at how the mask looks like
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

# Shaping the word cloud according to the mask is straightforward using word_cloud package. 
# For simplicity, we will continue using the first 2000 words in the novel.
# instantiate a word cloud object
alice_wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, stopwords=stopwords)

# generate the word cloud
alice_wc.generate(alice_novel)

# display the word cloud

plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()