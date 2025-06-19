# Line Plot Analysis: Immigration to Canada (1980-2013)

This branch visualizes immigration trends from Haiti, China, and India using Matplotlib line plots.

## Key Plots

### 1. Haiti Immigration (2010 Earthquake Impact)
![Haiti2010](https://github.com/user-attachments/assets/ed009b7c-5559-4f69-9076-f1e16e4b12d9)

**Notable Feature**:  
- Sharp increase post-2010 earthquake (annotated in red)  
- Demonstrates Canada's humanitarian response  

### 2. China vs. India Immigration Comparison  
![China India](https://github.com/user-attachments/assets/f8503791-9043-4cd6-89fc-b7955603a0e6)

**Key Insights**:  
- India shows steady growth (blue line)  
- China has earlier peaks (orange line)  

## Code Overview
```python
# Haiti Analysis
haiti = df_Canada.loc['Haiti', years]
haiti.plot(kind='line')
plt.text(2000, 6000, "2010 Earthquake")  # Critical annotation

# China-India Comparison 
df_CI = df_Canada.loc[['India', 'China'], years].transpose()
df_CI.plot(kind='line')
```

### File Structure for Branch:
line-plot/
├── README.md 
├── Line-plot.py 
├── haiti2010_plot.png
└── china_india_plot.png 
