# 11- Bubble Plot  
This branch uses **bubble plot visualizations** to analyze immigration trends to Canada from **1980 to 2013**, featuring normalized data and comparative country analysis through varying bubble sizes.

## Key Visualizations

### 1. Brazil vs. Argentina Immigration (1980–2013)

<img width="800" height="600" alt="Brazil vs  Argentina" src="https://github.com/user-attachments/assets/9b6964e7-61db-4cd7-adf8-901c02ee55c1" />

**Features:**
- **Brazil**: Green bubbles (#009739)
- **Argentina**: Blue bubbles (#75AADB)
- **Bubble sizes**: Normalized and scaled (2000x + 5) to show relative immigration numbers
- **Y-axis range**: 0 to 3000 immigrants
- **X-axis range**: 1979 to 2014
- Both countries show similar patterns with Argentina having slightly higher peaks

### 2. China vs. India Immigration (1980–2013)

<img width="800" height="600" alt="China vs  India" src="https://github.com/user-attachments/assets/ccd81063-1186-4ff7-9d31-31231a9f17d1" />

**Insights:**
- **China**: Red bubbles (#DE2910)
- **India**: Orange bubbles (#FF9933)
- **Bubble sizes**: Reflect normalized immigration data
- **Y-axis range**: 0 to 50,000 immigrants
- **X-axis range**: 1975 to 2015
- China shows rapid growth post-2000
- India demonstrates steady increase with notable acceleration in late 2000s

## Data Insights

**Key Findings:**
1. **Normalization**: Data normalized using min-max scaling for fair comparison
2. **Bubble Sizing**: Bubble size = `(normalized_value × 2000) + 5`
3. **Brazil & Argentina**: Both show moderate immigration (0–3000 range) with Argentina typically higher
4. **China & India**: Both show exponential growth, especially post-2000
5. **Comparative Advantage**: Bubble plots reveal both magnitude and trend simultaneously

## Code Highlights

```python
# Create Brazil bubble plot
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Brazil',
                    figsize=(12, 8),
                    alpha=0.8,
                    color='#009739',
                    s=norm_brazil * 2000 + 5,  # Size scaling
                    xlim=(1979, 2014),
                    ylim=(0, 3000))

# Add Argentina bubbles to same plot
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Argentina',
                    alpha=0.8,
                    color="#75AADB",
                    s=norm_argentina * 2000 + 5,
                    ax=ax0)
```

## Normalization Formula

```python
# Min-Max Normalization
normalized_value = (value - min_value) / (max_value - min_value)

# Bubble Size Calculation
bubble_size = normalized_value * scaling_factor + minimum_size
# Example: norm_brazil * 2000 + 5
```

## File Structure

```
bubble-plot-analysis/
├── README.md
├── bubble-plot-analysis.py
├── Canada.xlsx (main data source)
├── China vs. India.png (comparative bubble plot)
├── Brazil vs. Argentina.png (comparative bubble plot)
├── requirements.txt
└── data-tables/
    ├── china-india-data.csv
    └── brazil-argentina-data.csv
```

