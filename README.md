
# 3- Visualizing data for Canadian Immigration

This branch contains visualization scripts for analyzing immigration patterns to Canada from 1980-2013.

## Key Visualizations

1. **Global Immigration Trends**
   - Line plot showing immigration from all countries
   - Worldwide for Canada Line trending: 
![world](https://github.com/user-attachments/assets/865954ce-9e9c-4bb7-9845-92abf2384c43)
 

2. **Continental Immigration Analysis**  
   - Interactive line plots for:
     - Asia for Canada Line trending:
![Asia_plot](https://github.com/user-attachments/assets/4d266690-3694-4046-ac61-35ac3438be1c)

     - Europe for Canada Line trending:
![Europe_plot](https://github.com/user-attachments/assets/5ab0d8f3-d0b0-4604-9f74-6712ccf31498)

     - Africa for Canada Line trending:
![Africa_plot](https://github.com/user-attachments/assets/7cf8f374-dac8-4075-b968-e1952cb935bc)


## How to Use

1. Run the visualization script:
*bash*
## python scripts/visualize_immigration.py

# Main visualization workflow
```python
df = load_data('Canada.xlsx') 
plot_global_trends(df)  # Saves to plots/global_trends.png

continent = get_user_input()  # 1=Asia, 2=Europe, 3=Africa
plot_continent_trends(df, continent)  # Saves to respective plot file
```


## Repository Structure
```
visualizing-dataset/
├── data/
│ └── Canada.xlsx
├── scripts/
│ └── visualize_immigration.py
├── plots/
│ ├── global_trends.png
│ ├── asia_trends.png
│ ├── europe_trends.png
│ └── africa_trends.png
├── outputs/
│ └── sample_output.md
└── README.md
```
