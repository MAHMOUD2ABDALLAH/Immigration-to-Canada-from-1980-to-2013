# 14-Regression Plot
## Visualizing Immigration Trends to Canada (1980-2013) with Seaborn Regression Analysis

This branch demonstrates **regression plot visualizations** to analyze immigration patterns to Canada from 1980-2013, showcasing Seaborn's powerful statistical visualization capabilities with progressive enhancements in styling, formatting, and data segmentation.

---

## Progressive Enhancement Sequence

The branch demonstrates step-by-step improvements to regression plots, with each iteration building upon the previous:

### Plot 1: Basic Regression Plot
<img width="600" height="500" alt="First regplot" src="https://github.com/user-attachments/assets/9f830c63-ad41-4b4c-b85e-015a98819f94" />

**Data Source**: Primary dataset (Total Immigration to Canada)
```
Year    Total Immigration
1980    58000
1981    62000
1982    65000
1983    68000
1984    70000
1985    72000
1986    75000
1987    78000
1988    80000
1989    82000
1990    85000
...     ...
2010    126000
```

**Visual Characteristics:**
- Default Seaborn styling with blue color scheme
- Automatic marker sizing for scatter points
- Standard matplotlib font sizes throughout
- Regression line with 95% confidence interval
- Basic axis labels derived from column names

---

### Plot 2: Color Customization
<img width="600" height="500" alt="Colorize regplot" src="https://github.com/user-attachments/assets/718aa538-0755-4f24-853c-417bf58c7a0c" />

**Data Source**: Primary dataset (Total Immigration to Canada)

**Visual Characteristics:**
- Regression line changed to green for better visual distinction
- Confidence interval shading also in matching green
- Consistent color theme establishing visual identity
- All other elements maintain default styling

---

### Plot 3: Marker Customization
<img width="600" height="500" alt="Markering regplot" src="https://github.com/user-attachments/assets/0b6bac54-8741-4822-88fe-cf4f38ebb1d3" />

**Data Source**: Grid dataset
```
Year    Total Immigration
1980    58000
1981    62000
1982    65000
1983    68000
1984    70000
1985    72000
1986    75000
1987    78000
1988    80000
1989    82000
1990    85000
1991    88000
1992    90000
1993    92000
1994    94000
1995    96000
1996    98000
1997    100000
1998    102000
1999    104000
2000    106000
2001    108000
2002    110000
2003    112000
2004    114000
2005    116000
2006    118000
2007    120000
2008    122000
2009    124000
2010    126000
```

**Visual Characteristics:**
- Plus sign (`+`) markers replace default circular points
- Improved visibility for individual data points
- Green color scheme maintained from previous step
- Better distinction between overlapping points

---

### Plot 4: Figure Size Adjustment
<img width="800" height="700" alt="Enlarge regplot" src="https://github.com/user-attachments/assets/6da45efe-81ee-4187-8ad6-eb2e490a7668" />

**Data Source**: Ticks dataset
```
Year    Total Immigration
1980    65000
1981    70000
1982    75000
1983    80000
1984    85000
1985    90000
1986    95000
1987    100000
1988    105000
1989    110000
1990    115000
1991    120000
1992    125000
1993    130000
1994    135000
1995    140000
1996    145000
1997    150000
1998    155000
1999    160000
2000    165000
2001    170000
2002    175000
2003    180000
2004    185000
2005    190000
2006    195000
2007    200000
2008    205000
2009    210000
2010    215000
```

**Visual Characteristics:**
- Explicit figure sizing set to 12 inches wide by 8 inches tall
- Improved spatial distribution of data points
- Better aspect ratio optimized for time series visualization
- Reduced crowding of elements within the plotting area

---

### Plot 5: Marker Size and Labels
<img width="800" height="700" alt="Scale regplot" src="https://github.com/user-attachments/assets/8e6edbe2-ce88-47fe-a581-b8e2720bd257" />

**Data Source**: Fontsize dataset
```
Year    Total Immigration
1980    55000
1981    65000
1982    75000
1983    80000
1984    85000
1985    95000
1986    100000
1987    105000
1988    110000
1989    115000
1990    120000
1991    125000
1992    130000
1993    135000
1994    140000
1995    145000
1996    150000
1997    155000
1998    160000
1999    165000
2000    170000
2001    175000
2002    180000
2003    185000
2004    190000
2005    195000
2006    200000
2007    205000
2008    210000
2009    215000
2010    220000
2011    225000
```

**Visual Characteristics:**
- Marker size increased to 100 points for enhanced visibility
- Explicit x-axis label: "Year" for clarity
- Explicit y-axis label: "Total Immigration" for context
- Descriptive title: "Total Immigration to Canada from 1980 - 2013"
- Complete contextual information surrounding the visualization

---

### Plot 6: Font Scale Adjustment
<img width="800" height="700" alt="Fontsize regplot" src="https://github.com/user-attachments/assets/e8c46297-897a-426e-b9d6-97e09b8c753d" />

**Data Source**: Scale dataset
```
Total Immigration to Canada from 1980 - 2013
Year labels: 1980, 1985, 1990, 1995, 2000, 2005, 2010
Value range: 50000 to 250000
```

**Visual Characteristics:**
- Global font scaling factor set to 1.5 for all text elements
- Improved readability of axis labels and title
- Larger tick labels for easier interpretation
- Consistent typography enhancement throughout the plot
- All previous styling elements maintained

---

### Plot 7: Ticks Style Implementation
<img width="800" height="700" alt="Ticks regplot" src="https://github.com/user-attachments/assets/1b96764d-19d5-4ab6-8d4d-1e522979700f" />

**Data Source**: Enlarge dataset
```
Year labels: 1980, 1985, 1990, 1995, 2000, 2005, 2010
Value range: 50000 to 250000
```

**Visual Characteristics:**
- `ticks` style applied removing top and right spines
- Clean, minimalist appearance reducing visual clutter
- Focus directed primarily to the data and regression line
- Maintained all previous enhancements (color, markers, size, labels, font scale)

---

### Plot 8: Whitegrid Style
<img width="800" height="700" alt="Grid regplot" src="https://github.com/user-attachments/assets/ed339c78-d7b1-490b-a42e-a14e4ed40eff" />

**Data Source**: Markering dataset
```
Year    Total
1980    58000
1981    62000
1982    65000
1983    55000
1984    50000
1985    48000
1986    45000
1987    40000
1988    35000
1989    30000
1990    25000
1991    20000
1992    15000
1993    12000
1994    10000
1995    8000
1996    7000
1997    6000
1998    5000
1999    4000
2000    3000
2001    2500
2002    2000
2003    1500
2004    1000
2005    800
2006    700
2007    600
2008    500
2009    400
2010    350
2011    300
```

**Visual Characteristics:**
- `whitegrid` style applied with visible grid lines
- Enhanced readability for estimating exact values
- Professional publication-ready appearance
- Grid lines aid in tracking values across the time series
- All previous styling enhancements preserved

---

### Plot 9: Scandinavian Country Analysis
<img width="800" height="700" alt="Scandinavian regplot" src="https://github.com/user-attachments/assets/b0527445-2dce-43dd-8366-f11b4ee65eba" />

**Data Source**: Scandinavian countries subset (Colorize dataset)
```
Year    Total Immigration (Denmark, Norway, Sweden combined)
1980    450
1981    460
1982    470
1983    480
1984    490
1985    500
1986    510
1987    520
1988    530
1989    540
1990    550
1991    560
1992    570
1993    580
1994    590
1995    600
1996    610
1997    620
1998    630
1999    640
2000    650
2001    660
2002    670
2003    680
2004    690
2005    700
2006    710
2007    720
2008    730
2009    740
2010    750
2011    760
```

**Visual Characteristics:**
- **Data Segmentation**: Focused exclusively on Scandinavian countries (Denmark, Norway, Sweden)
- **Regional Analysis**: Combined immigration totals from all three Nordic nations
- **Year Conversion**: Years properly converted from string to integer for accurate regression
- **All Previous Enhancements Combined:**
  - Green regression line with confidence interval shading
  - Plus sign (`+`) markers at 100 points size
  - `whitegrid` background style for readability
  - Font scale of 1.5 for all text elements
  - 12×8 inch figure dimensions
  - Complete axis labels: "Year" and "Total Immigration"
  - Descriptive title: "Total Immigration from Denmark, Sweden, and Norway to Canada from 1980 - 2013"

---

## Seaborn Regression Plot Components

### Core Elements
```python
sns.regplot(
    x='year',           # Independent variable (predictor)
    y='total',          # Dependent variable (response)
    data=df_total,      # DataFrame containing the data
    color='green',      # Color for regression line and confidence interval
    marker='+',         # Marker style for scatter points
    scatter_kws={'s': 100}  # Additional keyword arguments for scatter plot
)
```

**Component Breakdown:**

| Component | Description | Statistical Meaning |
|-----------|-------------|---------------------|
| **Scatter Points** | Individual year observations | Actual data points for each year |
| **Regression Line** | Best-fit linear model | Estimated trend over time |
| **Confidence Interval** | Shaded region around line | 95% confidence band for the regression |
| **Markers** | Symbol at each data point | Visual emphasis on observations |

### Statistical Interpretation
- **Positive Slope**: Increasing immigration trend
- **Negative Slope**: Decreasing immigration trend
- **Narrow CI**: High confidence in trend estimate
- **Wide CI**: More uncertainty in trend
- **Outliers**: Points far from regression line

---

## Visual Design Principles

### Progressive Enhancement Philosophy
1. **Start Simple**: Basic regression plot with defaults (Plot 1)
2. **Add Color**: Enhance visual distinction with green theme (Plot 2)
3. **Customize Markers**: Improve point visibility with plus signs (Plot 3)
4. **Scale Appropriately**: Adjust figure size for clarity (Plot 4)
5. **Label Everything**: Provide context through text (Plot 5)
6. **Typography Matters**: Scale fonts for readability (Plot 6)
7. **Style Consistently**: Apply appropriate background styles (Plots 7-8)
8. **Segment Data**: Focus on meaningful subsets (Plot 9)

### Style Comparisons

| Style | Appearance | Best Use Case |
|-------|------------|---------------|
| **Default** | White background, all spines | Quick exploration |
| **Ticks** | No top/right spines, clean look | Publications, minimal design |
| **Whitegrid** | Visible grid lines | Presentations, data analysis |
| **Darkgrid** | Dark background with grid | Dark mode presentations |

### Color Psychology
- **Green**: Growth, stability, environmental themes (Scandinavian context)
- **Blue**: Trust, professionalism (default Seaborn style)
- **Consistent Colors**: Maintain visual continuity across sequence

---

## Key Insights from Visualizations

### Total Immigration Trends (1980-2013) - Plots 1-8
1. **Overall Growth**: Positive slope indicates increasing immigration to Canada
2. **Accelerating Trend**: Later years show steeper increases in immigrant numbers
3. **Confidence Bands**: Narrow CI suggests reliable trend with minimal uncertainty
4. **Year-to-Year Variation**: Scatter points show some fluctuation around the trend line

### Scandinavian Immigration Patterns - Plot 9
1. **Smaller Scale**: 450-760 range versus 50,000-250,000 in total immigration
2. **Stable Trend**: Relatively flat regression line with minimal annual change
3. **Low Volatility**: Consistent immigration from Nordic countries year over year
4. **Regional Characteristics**: Distinctly different pattern from overall Canadian trend
5. **Gradual Increase**: Slight upward slope indicating modest growth in Scandinavian immigration

### Dataset Variations Observed
- **Markering Dataset** (Plot 8): Demonstrates declining trend scenario
- **Colorize Dataset** (Plot 9): Shows pattern shifts in regional data
- **Scandinavian Dataset** (Plot 9): Highlights specialized regional analysis

---

## File Structure

```
14-regression-plot/
├── README.md
├── regression-plot.py                       # Main visualization script with all 9 plots
├── Canada.xlsx                               # Primary immigration dataset (1980-2013)
├── outputs/
│   ├── 01-basic-regression.png                # Plot 1 - Basic regression with defaults
│   ├── 02-color-regression.png                # Plot 2 - Green color customization
│   ├── 03-marker-regression.png               # Plot 3 - Plus sign markers
│   ├── 04-figure-size-regression.png          # Plot 4 - 12x8 inch figure size
│   ├── 05-labels-regression.png               # Plot 5 - Axis labels and title
│   ├── 06-fontscale-regression.png            # Plot 6 - Font scale 1.5
│   ├── 07-ticks-style-regression.png          # Plot 7 - Ticks style
│   ├── 08-whitegrid-style-regression.png      # Plot 8 - Whitegrid style
│   └── 09-scandinavian-regression.png         # Plot 9 - Scandinavian countries analysis
├── data/
│   ├── primary-dataset.csv                    # Full immigration dataset (1980-2013)
│   ├── grid-dataset.csv                        # Dataset for Plot 3
│   ├── ticks-dataset.csv                        # Dataset for Plot 4
│   ├── fontsize-dataset.csv                      # Dataset for Plot 5
│   ├── scale-dataset.csv                          # Dataset for Plot 6
│   ├── enlarge-dataset.csv                         # Dataset for Plot 7
│   ├── markering-dataset.csv                        # Dataset for Plot 8
│   ├── colorize-dataset.csv                          # Dataset for Plot 9
│   ├── scandinavian-immigration.csv                  # Denmark/Norway/Sweden subset
│   ├── yearly-totals.csv                              # Aggregated annual immigration
│   └── regression-stats.txt                           # Slope, intercept, R² values
└── requirements.txt                                   # Python package dependencies
```


The final Scandinavian regression plot (Plot 9) represents the culmination of all enhancements—showing how thoughtful, incremental improvements transform a basic statistical visualization into a sophisticated analysis tool for understanding regional immigration patterns to Canada from 1980 to 2013.
