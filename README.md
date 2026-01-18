# 10- Scatter Plot  
This branch uses **scatter plot visualizations** to analyze immigration trends to Canada from **1980 to 2013**, including linear regression for trend prediction.

## Key Visualizations

### 1. Total Immigration to Canada (1980–2013) with Linear Trend Line

<img width="800" height="600" alt="Linear line" src="https://github.com/user-attachments/assets/8b542527-898f-4c62-a5fb-a307c163518f" />

**Features:**
- Scatter plot showing total immigration per year (red points)
- Green linear regression line (best fit) with equation annotation
- Formula: `y = 556.82x - 1,092,357`
- Predicts immigration numbers for future years
- Shows clear upward trend in Canadian immigration

### 2. Immigration from Denmark, Norway, and Sweden (1980–2013)

<img width="800" height="600" alt="DNS" src="https://github.com/user-attachments/assets/6c81fbe4-3a85-4897-a72b-de619ff4bdee" />

**Insights:**
- Orange scatter points showing combined immigration from three Scandinavian countries
- Visualizes yearly totals with trend line
- Shows moderate but consistent immigration patterns
- Highlights variability across years

### 3. Example Immigration Scatter Plot

<img width="800" height="600" alt="First Scatter plot" src="https://github.com/user-attachments/assets/28a08ec3-0bb6-450f-a17d-dfd19fa99453" />

**Features:**
- Demonstrates basic scatter plot implementation
- Shows immigration numbers for specific years
- Illustrates data point distribution

## Data Insights

**Key Findings:**
1. **Overall Trend**: Steady increase in total immigration from 1980–2013
2. **Linear Model**: `Immigrants = 556.82 × Year - 1,092,357`
3. **2015 Prediction**: Approximately 280,000 immigrants
4. **Scandinavian Countries**: Consistent but moderate immigration flow
5. **Visual Patterns**: Clear positive correlation between year and immigration numbers

## Code Highlights

```python
# Create scatter plot with regression line
df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='red')

# Linear regression using numpy
x = df_tot['year']
y = df_tot['total']
fit = np.polyfit(x, y, deg=1)
plt.plot(x, fit[0] * x + fit[1], color='green')

# Annotate regression equation on plot
plt.annotate(f'y={fit[0]:.0f}x + {fit[1]:.0f}', xy=(2000, 150000))

# Multi-country scatter plot
df_countries = df_Canada.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_total = pd.DataFrame(df_countries.sum(axis=1))
df_total.plot(kind='scatter', x='year', y='total', color='orange')
```

## Regression Analysis

```python
# Print regression equation
print('No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1]))

# Predict for 2015
pred_2015 = fit[0] * 2015 + fit[1]
print(f'Predicted immigrants in 2015: {pred_2015:.0f}')

# Predict for 2020
pred_2020 = fit[0] * 2020 + fit[1]
print(f'Predicted immigrants in 2020: {pred_2020:.0f}')
```

## File Structure

```
scatter-plot-analysis/
├── README.md
├── scatter-plot-analysis.py
├── Canada.xlsx (main data source)
├── DNS.png (Scandinavian immigration data table)
├── Linear line.png (Regression analysis data table)
├── First Scatter plot.png (Example data table)
├── requirements.txt
└── images/
    ├── total-immigration-scatter.png
    ├── scandinavian-immigration-scatter.png
    └── example-scatter-plot.png
```
