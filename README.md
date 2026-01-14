# 9- Box Plot  
This branch uses **box plot visualizations** to analyze the distribution of immigration to Canada from selected countries between **1980 and 2013**.

## Key Visualizations

### 1. Box Plot of Japanese Immigrants (1980–2013)

<img width="600" height="400" alt="First Box Plot" src="https://github.com/user-attachments/assets/17110cb1-37c2-49a0-94bd-a7dfd207830f" />

**Features:**
- Visualizes the distribution of Japanese immigrants over 33 years
- Highlights median, quartiles, and potential outliers
- Shows relatively stable immigration numbers from Japan

### 2. Box Plots Comparing China and India (1980–2013)
<img width="600" height="400" alt="China vs  India" src="https://github.com/user-attachments/assets/f64a17c4-ab5f-429f-b0ac-c63b7fa658a2" />

**Insights:**
- India shows a wider spread and higher median immigration numbers
- China’s distribution is more compact with fewer extreme values
- Both countries show significant growth in immigration over time

### 3. Horizontal Box Plot Comparison
<img width="600" height="400" alt="Horizontal China vs  India" src="https://github.com/user-attachments/assets/e04bc6b1-8693-449e-a362-cc138b42fd29" />

**Alternative view providing:**
- Clear side-by-side comparison of distributions
- Easy reading of numerical scales
- Visual emphasis on distribution shapes

### 4. Combined Subplots: Box Plot and Line Plot
<img width="1506" height="600" alt="Subplots" src="https://github.com/user-attachments/assets/c9e74279-d0b0-4a12-b6f0-4e69a8f96255" />

**Dual visualization showing:**
- **Left**: Box plot distribution comparison
- **Right**: Line plot trend over time (1980–2013)
- China shows steady growth while India shows more volatility

### 5. Top 15 Countries by Decade (1980s, 1990s, 2000s)
<img width="800" height="600" alt="Decades 80&#39;s, 90&#39;s, 00&#39;s" src="https://github.com/user-attachments/assets/b4e7fc8f-e7f9-4535-a81b-5508177c67b1" />

**Decadal analysis reveals:**
- Increasing immigration volumes across decades
- 2000s shows highest median and spread
- Outliers identified in 2000s data (e.g., China, India)

## Data Insights

**Key Findings:**
1. **Japan**: Consistent but modest immigration (median ~800)
2. **China vs India**: India has higher median but China shows more consistent growth
3. **Top 15 Countries**: Immigration volumes increased significantly in 2000s
4. **Outliers**: China and India are outliers in 2000s data (>209,611 immigrants)

## Code Highlights

```python
# Box plot for single country
df_japan.plot(kind='box', figsize=(8, 6))

# Comparison box plot
df_CI.plot(kind='box', figsize=(10, 7))

# Decadal analysis
new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s': df_00s})
new_df.plot(kind='box', figsize=(10, 6))
```

## Outlier Analysis
```python
# Identify outliers in 2000s data
Q1 = new_df['2000s'].quantile(0.25)
Q3 = new_df['2000s'].quantile(0.75)
IQR = Q3 - Q1
outlier_threshold = Q3 + (1.5 * IQR)
print(new_df[new_df['2000s'] > outlier_threshold])
```

## File Structure

```
box-plot-analysis/
├── README.md
├── box-plot-analysis.py
├── First Box Plot.png
├── China vs. India.png
├── Horizontal China vs. India.png
├── Subplots.png
└── Decades 80's, 90's, 00's.png
```

## Usage
Run the Python script to generate all box plot visualizations and statistical summaries. 
The analysis helps identify immigration patterns, compare country distributions, and track changes across decades.
