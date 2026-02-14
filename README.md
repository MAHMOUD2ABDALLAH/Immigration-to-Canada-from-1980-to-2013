# 13`-Word Cloud Country Immigration Analysis  
This branch implements **country-specific word cloud visualizations** to analyze immigration patterns to Canada from 1980-2013, using frequency-based word clouds with no duplicates and reproducible layouts.

## Key Visualizations

### 1. Immigration Word Cloud - Single Instance per Country
<img width="600" height="500" alt="Proporation Cloud" src="https://github.com/user-attachments/assets/85f489d4-6c40-4c4b-ae71-0a4e2c7f1cec" />


**Code Reference (Lines 51-58):**
```python
# Create the word cloud using frequencies
wordcloud = WordCloud(background_color='white', width=800, height=400, random_state=10)
wordcloud.generate_from_frequencies(word_frequencies)

print('Word cloud created with no duplicates!')

# Display the cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Immigration by Country (1980-2013) - Each Country Once')
plt.show()
```

**Final Output Characteristics:**
- **No Duplicate Entries**: Each country appears exactly once in the visualization
- **Size Encoding**: Word size directly proportional to immigration numbers
- **Reproducible Layout**: Fixed `random_state=10` ensures same visualization each run
- **Color Scheme**: Default wordcloud colormap with white background
- **Resolution**: 800×400 pixels for clear visibility
- **Interpolation**: Bilinear smoothing for clean text rendering

## Data Processing Pipeline

### Step 1: Data Acquisition and Cleaning
```python
# Load Excel file with specific row skipping
repo_path = os.path.expanduser("Canada.xlsx")
df_Canada = pd.read_excel(os.path.join(repo_path), skiprows=range(20), skipfooter=29)

# Drop unnecessary columns
df_Canada.drop(["AREA", "REG", "DEV", "Type", "Coverage"], axis=1, inplace=True)

# Rename for clarity
df_Canada.rename(
    columns={"OdName": "Country", "AreaName": "Continent", "RegName": "Region"},
    inplace=True,
)
```

**Data Transformations:**
- **Skip Rows**: First 20 rows contain metadata
- **Skip Footer**: Last 29 rows contain summary statistics
- **Column Cleanup**: Remove administrative/geographic code columns
- **Renaming**: Human-readable column names

### Step 2: Column Type Conversion
```python
# Check if all columns are strings
all(isinstance(column, str) for column in df_Canada.columns)  # Returns False

# Convert all columns to strings
df_Canada.columns = list(map(str, df_Canada.columns))
```

**Why This Matters:**
- Year columns (1980-2013) are initially integers
- String conversion ensures consistent access
- Prevents indexing errors with mixed types

### Step 3: Index and Total Column Setup
```python
# Set country as index for easy lookup
df_Canada.set_index("Country", inplace=True)

# Add total immigration column (1980-2013)
df_Canada["Total"] = df_Canada.select_dtypes(include="number").sum(axis=1)
```

### Step 4: Immigration Total Calculation
```python
total_immigration = df_Canada['Total'].sum()
print(f"Total Immigration: {total_immigration}")
```

### Step 5: Frequency Dictionary Creation
```python
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
```

**Filtering Logic:**
- **Single-word countries only**: `country.count(" ") == 0`
- **Excluded examples**: "United Kingdom", "South Korea", "New Zealand"
- **Included examples**: "China", "India", "Pakistan", "Philippines"
- **Frequency values**: Raw immigration numbers (not scaled or repeated)

## Word Cloud Generation Details

### Configuration Parameters
```python
wordcloud = WordCloud(
    background_color='white',  # Clean, printable background
    width=800,                 # High resolution width
    height=400,                # High resolution height
    random_state=10            # Fixed seed for reproducibility
)
```

**Parameter Explanations:**
| Parameter | Value | Purpose |
|-----------|-------|---------|
| `background_color` | 'white' | Ensures text contrast and print compatibility |
| `width` | 800 | Adequate resolution for detail |
| `height` | 400 | Balanced aspect ratio (2:1) |
| `random_state` | 10 | Guarantees identical layout each run |

### Generation Method
```python
wordcloud.generate_from_frequencies(word_frequencies)
```

**Why `generate_from_frequencies()` Instead of `generate()`:**
- **Direct mapping**: Word size ←→ immigration number
- **No duplication**: Each country appears once in dictionary
- **Preserves proportions**: Raw numbers maintain accurate ratios
- **More efficient**: No string building with repetitions

## Visual Design Principles

**Size Encoding:**
- **Largest Text**: Highest immigration countries (China, India, Philippines)
- **Medium Text**: Moderate immigration countries (Pakistan, Bangladesh, Colombia)
- **Smallest Text**: Lower immigration countries (France, Germany, Guyana)

**Layout Algorithm:**
1. Words sorted by frequency (largest first)
2. Random placement attempts until space found
3. Fixed `random_state` ensures identical "random" placement each run
4. Collision detection prevents overlaps

**Readability Features:**
- **White background** maximizes contrast
- **Bilinear interpolation** smooths text rendering
- **No axis clutter** focuses on the visualization
- **Descriptive title** provides context

## Key Insights from Visualization

**Immigration Patterns Visible:**
- **Asian dominance**: China, India, Philippines, Pakistan prominently sized
- **European representation**: France, Germany, Portugal (smaller but present)
- **Caribbean presence**: Jamaica, Haiti, Guyana visible
- **Middle Eastern**: Israel, Egypt, Algeria represented
- **South American**: Colombia appears

**What the Visualization Reveals:**
1. **Top Sources**: Asian countries dominate Canadian immigration
2. **Geographic Diversity**: Immigrants from multiple continents
3. **Size Hierarchy**: Clear visual ranking of source countries
4. **Pattern Recognition**: Regional clusters visible

## Comparison with Duplicate-Based Approach

| Aspect | Duplicate-Based (Previous) | Frequency-Based (Current) |
|--------|----------------------------|---------------------------|
| **Generation** | `.generate(word_string)` | `.generate_from_frequencies()` |
| **Data Structure** | Repeated country names | Dictionary of frequencies |
| **Word Instances** | Multiple per country | One per country |
| **Visual Clutter** | "China China China..." text | Clean, single "China" |
| **Proportionality** | Integer-rounded repetitions | Exact immigration numbers |
| **Multi-word Handling** | Excluded | Excluded (limitation) |

## File Structure

```
word-cloud-country/
├── README.md
├── word-cloud-country.py              # Main visualization script
├── Canada.xlsx                        # Primary immigration dataset (1980-2013)
├── country-wordcloud.png               # Final word cloud visualization (lines 51-58)
├── requirements.txt                    # Python package dependencies
└── outputs/
    ├── single-word-countries.txt       # List of included countries
    ├── excluded-countries.txt          # Multi-word countries filtered out
    ├── immigration-frequencies.csv      # Frequency values by country
    └── top-10-countries.txt             # Highest immigration sources
```

## Requirements

```txt
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
wordcloud>=1.8.0
openpyxl>=3.0.0  # For Excel file handling
```
