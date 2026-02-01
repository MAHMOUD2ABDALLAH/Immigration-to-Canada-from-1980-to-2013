# 12-Waffle Plot  
This branch implements **waffle chart visualizations** to analyze immigration totals from Scandinavian countries to Canada, using a tile-based representation with custom color schemes and legends.

## Key Visualizations

### 1. Waffle Chart Creation

<img width="800" height="200" alt="creating" src="https://github.com/user-attachments/assets/b96b70d1-846c-4192-8a05-3ed3b5cd1859" />

**Final Output Characteristics:**
- **Color Scheme**: 
  - Denmark: `#C60C30` (Red)
  - Sweden: `#FECC00` (Yellow)
  - Norway: `#00205B` (Blue)
- **Grid Layout**: 40 columns × 10 rows (400 total tiles)
- **Visual Encoding**: Each colored tile represents proportional immigration data
- **Grid Lines**: White borders for clear tile separation
- **Compact Design**: Optimized figure size (9×2.5 inches)

### 2. Tile Splitting and Distribution Process

<img width="800" height="200" alt="splitting" src="https://github.com/user-attachments/assets/2869e391-2dd3-417a-81f6-d7eebed89b87" />

**Process Breakdown:**
- **Total Tiles**: 400 (40 × 10 grid)
- **Proportional Allocation**: Based on each country's immigration percentage
- **Tile Assignment**: Sequential population from left to right, top to bottom
- **Category Mapping**: Integer values (1, 2, 3) correspond to Denmark, Sweden, Norway
- **Distribution Logic**: Tiles allocated according to calculated proportions

### 3. Legend and Color Scale Reference

<img width="900" height="250" alt="Legend" src="https://github.com/user-attachments/assets/b6d005bc-b43b-49a5-b6d1-29e093a916b6" />

**Reference Guide:**
- **Countries Represented**: Denmark, Norway, Sweden
- **Color Mapping**: 
  - Red (#C60C30) → Denmark
  - Yellow (#FECC00) → Sweden  
  - Blue (#00205B) → Norway
- **Color Scale**: Discrete values from 1.0 to 3.0 for data intensity
- **Legend Placement**: Integrated into chart for immediate recognition

## Data Processing Pipeline

### Step 1: Scandinavian Data Extraction
```python
# Filter for Scandinavian countries
df_dsn = df_Canada.loc[["Denmark", "Norway", "Sweden"], :]

# Calculate proportions
total_values = df_dsn["Total"].sum()
category_proportions = df_dsn["Total"] / total_values
```

### Step 2: Grid and Tile Configuration
```python
width = 40    # Columns
height = 10   # Rows
total_num_tiles = width * height  # 400 tiles

# Calculate tile distribution
tiles_per_category = (category_proportions * total_num_tiles).round().astype(int)
```

### Step 3: Matrix Population Algorithm
```python
# Initialize empty matrix
waffle_chart = np.zeros((height, width), dtype=np.uint)

# Sequential tile assignment
category_index = 0
tile_index = 0

for col in range(width):
    for row in range(height):
        tile_index += 1
        # Move to next category when tile quota reached
        if tile_index > sum(tiles_per_category[0:category_index]):
            category_index += 1
        waffle_chart[row, col] = category_index
```

### Step 4: Visualization with Custom Colors
```python
# National color mapping
colors = ["#C60C30", "#FECC00", "#00205B"]  # Denmark, Sweden, Norway

# Create custom colormap
scandi_cmap = mcolors.LinearSegmentedColormap.from_list("scandi_flags", colors)

# Render waffle chart
plt.matshow(waffle_chart, cmap=scandi_cmap)
```

## Visual Design Principles

**Grid System (400 Tiles):**
- **Resolution Balance**: 40×10 provides sufficient detail without clutter
- **Proportional Accuracy**: Each tile ≈ 0.25% of total immigration
- **Readability**: Tile size optimized for visual recognition

**Color Strategy:**
1. **National Identity**: Flag colors enable immediate country association
2. **Contrast Optimization**: High contrast between adjacent colors
3. **Colorblind Consideration**: Distinct hues for accessibility

**Legend Implementation:**
- **Proxy Artists**: Custom rectangles for legend items
- **Compact Placement**: Right-side positioning preserves chart space
- **Clear Labeling**: Direct country-color mapping

## Key Insights from Visualization

**Immigration Distribution:**
- **Proportional Representation**: Tile counts reflect actual immigration ratios
- **Visual Comparison**: Relative sizes immediately apparent
- **Pattern Recognition**: Distribution patterns visible at a glance

**Advantages Over Traditional Charts:**
1. **Intuitive Understanding**: Part-to-whole relationships easily grasped
2. **Aesthetic Appeal**: Visually engaging compared to bar/pie charts
3. **Space Efficiency**: High data density in compact format
4. **Pattern Visibility**: Distribution patterns emerge naturally

## Complete Implementation Example

```python
# Create comprehensive waffle chart with legend
plt.figure(figsize=(9, 2.5))

# Display waffle matrix
plt.matshow(waffle_chart, cmap=scandi_cmap, fignum=plt.gcf().number)

# Add grid lines
ax = plt.gca()
ax.set_xticks(np.arange(0.5, width, 1), minor=True)
ax.set_yticks(np.arange(0.5, height, 1), minor=True)
ax.grid(which="minor", color="w", linestyle="-", linewidth=1)

# Create and position legend
legend_elements = [
    plt.Rectangle((0, 0), 1, 1, facecolor=colors[i], 
                  edgecolor="w", linewidth=0.5)
    for i in range(len(df_dsn))
]

ax.legend(legend_elements, df_dsn.index.tolist(),
          loc="best", bbox_to_anchor=(1.0, 1.0),
          title="Countries", fontsize=8)

plt.title("Waffle Chart of Scandinavian Immigration to Canada")
plt.tight_layout()
plt.show()
```

## File Structure

```
waffle-plot-analysis/
├── README.md
├── waffle-plot.py                    # Main visualization script
├── Canada.xlsx                       # Primary immigration dataset
├── creating.png                      # Final waffle chart (40×10 grid)
├── splitting.png                     # Tile distribution process
├── legend.png                        # Color legend and scale reference
├── requirements.txt                  # Python package dependencies
└── outputs/
    ├── scandinavian-data.csv         # Filtered Scandinavian immigration
    ├── tile-calculation.csv          # Proportional tile allocations
    └── waffle-matrix.csv             # Generated 10×40 matrix values
```
