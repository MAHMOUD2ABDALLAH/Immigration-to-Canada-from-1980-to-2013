# 8- Pie Chart Plot
This branch enhances pie chart visualizations to analyze immigration patterns by continent to Canada from **1980 to 2013**, including a special focus on the distribution for the year **2013**.

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

### 3. Immigration to Canada by Continent in 2013
<img width="800" height="600" alt="Pie Continent" src="https://github.com/user-attachments/assets/a386611c-dc1f-4500-85cc-be00ee05a90f" />

**2013 Continental Distribution:**
- Africa: **65.0%**
- Asia: **8.7%**
- Europe: **15.4%**
- Latin America & Caribbean: **10.1%**
- Northern America: **0.0%**
- Oceania: **0.8%**

**Features:**
- Exploded wedges for emphasis on smaller contributing continents
- Clean legend placement
- Percentage labels for precise interpretation
- Shows dramatic shift in continental contributions for 2013 compared to long-term trends

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

**2013 Anomaly:**
- Africa accounted for 65% of immigrants in 2013, a significant increase from its 13.1% long-term average
- Asia's contribution dropped to only 8.7% in 2013 compared to 59.9% long-term average

## Code Highlights

```python
# Data grouping by continent
continent_group = df_Canada.groupby('Continent')
print(continent_group.sum())

# Pie chart visualization for total period
df_continents['Total'].plot(kind='pie', autopct='%1.1f%%')
plt.title('Immigration to Canada by Continent [1980 - 2013]')

# 2013-specific pie chart with exploded wedges
explode_list = [0.0, 0, 0, 0.1, 0.1, 0.2]
df_continents['2013'].plot(kind='pie',
                           figsize=(10, 8),
                           autopct='%1.1f%%', 
                           startangle=90,    
                           explode=explode_list)
plt.title('Immigration to Canada by Continent in 2013', y=1.05)
plt.legend(labels=df_continents.index, bbox_to_anchor=(1.1, -0.1), loc="lower right")
```

## File Structure

```
pie-group-enhancements/
├── README.md
├── pie-group-enhancements.py
├── First Pie Group.png
├── Pie Group Enhancements.png
└── Pie Continent 2013.png
```
