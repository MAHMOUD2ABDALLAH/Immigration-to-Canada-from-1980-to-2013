# 13-Word Cloud - Intro
This branch implements **word cloud visualizations** to analyze text from Alice's Adventures in Wonderland, demonstrating how to create, customize, and shape word clouds using mask images and stopword filtering.

## Key Visualizations

### 1. Initial Word Cloud Generation
<img width="600" height="500" alt="First Cloud" src="https://github.com/user-attachments/assets/33f91927-a083-495f-932c-0248c6cdf828" />

**Code Reference (Lines 45-52):**
```python
# instantiate a word cloud object
alice_wc = WordCloud(background_color="white", max_words=2000, stopwords=stopwords)

# generate the word cloud
alice_wc.generate(alice_novel)

# display the word cloud
plt.imshow(alice_wc, interpolation="bilinear")
plt.axis("off")
plt.show()
```

**Final Output Characteristics:**
- **Background Color**: White
- **Maximum Words**: 2000 most frequent terms
- **Stopwords**: Default English stopwords
- **Visual Encoding**: Word size represents frequency in the text
- **Interpolation**: Bilinear smoothing for clean rendering

### 2. Word Cloud After Removing "Said"
<img width="600" height="500" alt="StopWord informative-Said" src="https://github.com/user-attachments/assets/7dcefc52-9b6c-4bd0-abf4-fbb79bd427e1" />

**Code Reference (Lines 57-65):**
```python
# "said" isn't really an informative word.
# So let's add it to our stopwords and re-generate the cloud.

stopwords.add("said")  # add the words said to stopwords

# re-generate the word cloud
alice_wc.generate(alice_novel)

# display the cloud
plt.imshow(alice_wc, interpolation="bilinear")
plt.axis("off")
plt.show()
```

**Process Breakdown:**
- **Stopword Addition**: "said" added to remove frequent dialogue tags
- **Frequency Shift**: Previously dominant word removed
- **Emergence**: Content words (Alice, Queen, King) become more prominent
- **Clarity**: More meaningful representation of novel content

### 3. Alice Mask Image Display
<img width="600" height="500" alt="Alice Mask" src="https://github.com/user-attachments/assets/b773375f-b34a-46f7-83f4-84b888b0fbd1" />

**Code Reference (Lines 68-77):**
```python
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
```

**Mask Characteristics:**
- **Source**: External PNG image from IBM course materials
- **Colormap**: Grayscale (plt.cm.gray)
- **Shape**: Silhouette of Alice character
- **Purpose**: Defines boundaries for shaped word cloud

### 4. Final Mask-Shaped Word Cloud
<img width="600" height="500" alt="Alice Cloud" src="https://github.com/user-attachments/assets/7ed963fe-9aa8-4d50-9ccb-fcd3cdc1b430" />

**Code Reference (Lines 80-90):**
```python
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
```

**Mask Integration:**
- **Mask Parameter**: `mask=alice_mask` constrains word placement
- **Shape Fitting**: Words fill only within mask boundaries
- **Background**: White background outside mask
- **Visual Effect**: Words form Alice silhouette

## Data Processing Pipeline

### Step 1: Text Acquisition
```python
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/alice_novel.txt"

try:
    response = requests.get(url)
    response.raise_for_status()
    alice_novel = response.text
    print(f"Successfully downloaded {len(alice_novel)} characters")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### Step 2: Stopword Configuration
```python
# Initialize with default stopwords
stopwords = set(STOPWORDS)

# Add domain-specific stopword
stopwords.add("said")
```

### Step 3: Mask Processing
```python
# Download and convert mask to numpy array
alice_mask = np.array(
    Image.open(
        urllib.request.urlopen(
            "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%204/images/alice_mask.png"
        )
    )
)
```

### Step 4: Word Cloud Generation Pipeline
```python
# Three-stage generation
# Stage 1: Basic cloud
alice_wc = WordCloud(background_color="white", max_words=2000, stopwords=stopwords)
alice_wc.generate(alice_novel)

# Stage 2: With added stopword
stopwords.add("said")
alice_wc.generate(alice_novel)

# Stage 3: With mask
alice_wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, stopwords=stopwords)
alice_wc.generate(alice_novel)
```

## Visual Design Principles

**Word Cloud Parameters:**
- **max_words=2000**: Balance between detail and clutter
- **background_color="white"**: Clean, printable background
- **interpolation="bilinear"**: Smooth rendering of text

**Mask Integration:**
1. **Shape Boundary**: Words constrained to silhouette
2. **Word Placement**: Algorithm fills available white space
3. **Size Scaling**: Word size reflects frequency within shape constraints

**Stopword Strategy:**
- **Default STOPWORDS**: Remove common English articles/prepositions
- **"said" Addition**: Eliminate frequent dialogue tags
- **Result**: Content words (characters, actions) become prominent

## Key Insights from Visualization

**Text Analysis Benefits:**
- **Frequency Visualization**: Most common words immediately visible
- **Character Prominence**: Alice, King, Queen, Hatter dominate
- **Theme Indication**: Words like "little", "large", "long" reveal narrative style

**Mask Advantages Over Standard Clouds:**
1. **Thematic Connection**: Alice shape reinforces novel association
2. **Visual Appeal**: More engaging than rectangular clouds
3. **Brand Recognition**: Shape itself conveys meaning
4. **Artistic Value**: Combines data visualization with illustration


## File Structure

```
word-cloud-intro/
├── README.md
├── word-cloud.py                      # Main visualization script
├── initial-wordcloud.png               # First word cloud (lines 45-52)
├── filtered-wordcloud.png              # After removing "said" (lines 57-65)
├── alice-mask.png                       # Mask display (lines 68-77)
├── masked-wordcloud.png                 # Final shaped cloud (lines 80-90)
├── requirements.txt                    # Python package dependencies
└── outputs/
    ├── stopwords-used.txt              # Complete stopword list
    ├── word-frequencies.csv             # Top word frequencies
    └── mask-dimensions.txt              # Mask array properties
```

## Requirements

```txt
numpy
pandas
matplotlib
wordcloud
Pillow
requests
urllib3
```
