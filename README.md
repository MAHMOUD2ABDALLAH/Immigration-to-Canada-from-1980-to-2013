# 8- Pie Group
This branch enhances pie chart visualizations to analyze immigration patterns by continent to Canada from **1980 to 2013**.

## Key Visualizations

### 1. Immigration to Canada by Continent [1980 - 2013]
<img width="700" height="600" alt="First Pie Group" src="https://github.com/user-attachments/assets/b05e824d-a973-40b7-b3b7-ba11429cefed" />

**Continents:**
- Africa
- Asia  
- Europe
- Latin America and the Caribbean
- Northern America
- Oceania

**Features:**
- Clear percentage distribution per continent
- Asia dominates with **59.9%** of total immigration
- Europe second with **15.0%**
- Africa third with **13.1%**
- Minimal contributions from Northern America and Oceania

### 2. Immigration to Canada by Continent [1980 - 2013]
<img width="800" height="600" alt="Pie Group Enhancements" src="https://github.com/user-attachments/assets/44b98d73-66d4-42e1-a3a3-544da7ebec02" />

**Alternative visualization showing:**
- Color-coded continental breakdown
- Total immigration volume context
- Regional grouping clarity

## Data Insights

From the processed data, we can see:

**Top Contributing Continents (Total 1980-2013):**
1. Asia: 3,140,206 immigrants
2. Europe: 787,722 immigrants  
3. Africa: 571,597 immigrants
4. Latin America & Caribbean: 689,150 immigrants

**Minimal Contributions:**
- Northern America: 20 immigrants
- Oceania: Very low numbers (e.g., American Samoa: 6 total)

## Code Highlights

```python
# Data grouping by continent
continent_group = df_Canada.groupby('Continent')
print(continent_group.sum())

# Pie chart visualization
df_continents['Total'].plot(kind='pie', autopct='%1.1f%%')
plt.title('Immigration to Canada by Continent [1980 - 2013]')
```

## File Structure

```
pie-group-enhancements/
├── README.md
├── pie-group-enhancements.py
├── Pie Group Enhancements.png
└── First Pie Group.png
```
