# 6- Histogram Plot: Immigration to Canada

This branch uses **histogram plots** to analyze the distribution of immigration to Canada from 195 countries, with a focus on the year **2013**.

## Data Processing Summary

### Initial Dataset
- **Original dimensions:** (168, 43)
- **Columns:** Country, Continent, Region, DevName, and yearly immigration data from 1980-2013
- **Processing:** Set 'Country' as index and removed non-informative columns (AREA, REG, DEV, Type, Coverage)
- **Final dimensions:** (168, 38) → Calculated as: 43 - 5 + 1 - 1 = 38 columns

### Top Immigration Sources (2013)
- **China:** 34,129 immigrants
- **India:** 33,087 immigrants
- **Philippines:** 29,544 immigrants
- **Pakistan:** 12,603 immigrants
- **Iran (Islamic Republic of):** 11,291 immigrants

### Scandinavian Countries (1980-1984 Sample)
- **Denmark:** 93-299 immigrants annually
- **Norway:** 31-116 immigrants annually  
- **Sweden:** 128-308 immigrants annually

## Key Visualizations

### 1. Global Immigration Distribution in 2013
<img width="800" height="500" alt="all immigrates in 2013" src="https://github.com/user-attachments/assets/8cb05618-678e-4284-aa46-d0c297d01e1a" />

**Frequency Distribution Analysis:**
- **153 countries** sent fewer than 3,413 immigrants
- **10 countries** sent between 3,413-6,826 immigrants
- **Only 5 countries** sent more than 10,239 immigrants
- **Bin edges:** [0.0, 3412.9, 6825.8, 10238.7, 13651.6, 17064.5, 20477.4, 23890.3, 27303.2, 30716.1, 34129.0]
- **Frequency distribution:** [153, 10, 0, 2, 0, 0, 0, 0, 1, 2]

**Insights:**
- Distribution is **highly right-skewed** with extreme inequality
- Majority of countries (153/168 = 91%) contribute minimal immigration
- Top 2 countries (China & India) account for approximately 20% of total immigration
- Follows a **power-law distribution** rather than normal distribution

### 2. Scandinavian Countries Immigration Patterns
**Initial Attempt - Incorrect Interpretation:**

<img width="800" height="500" alt="3 countries frequences" src="https://github.com/user-attachments/assets/ac6de749-272f-4b83-aa6d-db36a94c5997" />

*Issue: First plot incorrectly showed year frequency instead of immigration distribution*

**Corrected Analysis - Unstacked Histogram:**
<img width="800" height="500" alt="3 countries pins " src="https://github.com/user-attachments/assets/acbbf3cc-c317-4ea1-9664-47e26e32c2b8" />

**Key Findings:**
- **Denmark:** Most frequent immigration range: 90-120 immigrants per year
- **Norway:** Most frequent immigration range: 40-70 immigrants per year  
- **Sweden:** Most frequent immigration range: 140-180 immigrants per year
- Sweden consistently receives more immigrants than Denmark and Norway

**Stacked Histogram Comparison:**
<img width="800" height="500" alt="3 countries stacked" src="https://github.com/user-attachments/assets/89332a28-7389-4fad-9edf-988199d49baf" />

**Comparative Analysis:**
- **Sweden:** Peak years with 270-310 immigrants occurred in early 1980s
- **Denmark:** Shows more consistent distribution across years
- **Norway:** Lowest overall immigration among the three countries

### 3. Balkan Region Analysis (Greece, Albania, Bulgaria)
<img width="800" height="500" alt="3 other countries applying task " src="https://github.com/user-attachments/assets/c2475c6a-e78b-47d2-a395-3c016e9aa0fb" />

**Transparency Analysis (alpha=0.35):**
- **Greece:** Wider distribution with significant decline post-1990
- **Albania:** Sharp increase in early 1990s following political changes
- **Bulgaria:** Steady but lower immigration levels throughout the period

**Regional Patterns:**
- Greece shows the highest historical immigration (peaking in 1980s)
- Albania demonstrates the most dramatic change over time
- All three countries show declining trends in recent years

## Methodological Insights

### Histogram Binning Strategy
- **Automatic binning:** Used numpy.histogram for optimal bin determination
- **Custom bin edges:** Applied for better interpretability on skewed distributions
- **Transparency effects:** Utilized alpha parameter for overlapping histogram visualization

### Data Transformation Requirements
- **Transposition necessity:** Required for correct time-series vs. frequency analysis
- **Country filtering:** Enabled focused regional comparisons
- **Statistical summary:** Combined with visual analysis for comprehensive insights

## Key Technical Outcomes

1. **Distribution Characterization:** Successfully quantified the extreme skew in immigration sources
2. **Regional Comparison:** Developed methodology for comparing immigration patterns across country groups
3. **Temporal Analysis:** Demonstrated how histogram plots can reveal migration trend changes
4. **Visual Optimization:** Implemented transparency and stacking for multi-country comparisons

## Project Structure
```
├── README.md
├── Histogram-plot.py
├── Canada.xlsx
└── assets/
    ├── all_immigrants_2013.png
    ├── scandinavian_initial.png
    ├── scandinavian_unstacked.png
    ├── scandinavian_stacked.png
    └── balkan_countries.png
```

## Policy Implications
- **Resource allocation:** Immigration services should focus resources on top source countries
- **Trend monitoring:** Histograms provide early warning for changing migration patterns
- **Regional strategies:** Different regions require tailored immigration approaches based on their distribution patterns
- **Forecasting:** Skewed distributions suggest unpredictable changes from small number of countries

This analysis demonstrates how histogram visualization combined with statistical analysis provides actionable insights for immigration policy planning and resource allocation.
