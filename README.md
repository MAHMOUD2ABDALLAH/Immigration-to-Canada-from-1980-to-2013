# 5- Area Plot

This branch uses **stacked area plots** to analyze immigration patterns from:
1. Top 5 contributing countries
2. Bottom 5 contributing countries

## Key Visualizations

### 1. Top 5 Countries Immigration Trend
![Top 5 country](https://github.com/user-attachments/assets/8b18d6f2-a731-4e9e-b4be-f2af7ba3b375)

**Countries**: India, China, Philippines, Pakistan, Iran  
**Features**:  
- Clear volume comparison with `alpha=1` transparency  
- Dominance of India (blue) and China (orange) visible  

### 2. Least 5 Contributing Countries  
![Least 5 country](https://github.com/user-attachments/assets/cce1efe0-892e-4bd7-8826-f2f83326211b)


**Countries**: American Samoa, New Caledonia, San Marino, Marshall Islands, Palau  
**Insights**:  
- Minimal immigration volumes (note y-axis scale in thousands)  
- Some years show zero immigration  

## Code Highlights
```python
# Top 5 Analysis
df_top = df_Canada.sort_values('Total', ascending=False).head(5)
df_top[years].transpose().plot(kind='area', alpha=1)

# Bottom 5 Analysis 
df_least5 = df_Canada.sort_values('Total').head(5)
df_least5[years].transpose().plot(kind='area')
```

### File Structure:
```
area-plot/
├── README.md
├── Area-plot.py
├── top5_countries.png
└── least5_countries.png
```
