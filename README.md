# 1- Exploring Canada Immigration Dataset

This repository contains an analysis of international immigration flows to Canada from 1980-2013.

## Dataset Description
- Contains annual data on international immigrant flows
- Records both inflows and outflows by:
  - Place of birth
  - Citizenship
  - Place of previous/next residence
- Covers data for 45 countries
- Time period: 1980-2013

## Analysis Script
The `explore_canada_immigration.py` script performs the following operations:

1. **Data Loading**:
   - Reads the Excel file with proper skipping of header/footer rows
   - Uses openpyxl engine for Excel file handling

2. **Data Exploration**:
   - Displays first/last 5 rows
   - Shows dataframe info and structure
   - Examines column headers and indices
   - Checks dataframe shape

3. **Data Cleaning**:
   - Drops columns with null values
   - Renames key columns for clarity:
     - 'OdName' → 'Country'
     - 'AreaName' → 'Continent'
     - 'RegName' → 'Region'

4. **Feature Engineering**:
   - Adds 'Total' column summing immigration across all years

5. **Data Quality Checks**:
   - Identifies null values
   - Provides statistical summary

## Data Exploration

### First 5 Rows
| Type       | Coverage   | OdName          | AREA | ... | 2010 | 2011 | 2012 | 2013 |
|------------|------------|-----------------|------|-----|------|------|------|------|
| Immigrants | Foreigners | Afghanistan     | 935  | ... | 1758 | 2203 | 2635 | 2004 |
| Immigrants | Foreigners | Albania         | 908  | ... | 561  | 539  | 620  | 603  |
| Immigrants | Foreigners | Algeria         | 903  | ... | 4752 | 4325 | 3774 | 4331 |
| Immigrants | Foreigners | American Samoa  | 909  | ... | 0    | 0    | 0    | 0    |
| Immigrants | Foreigners | Andorra         | 908  | ... | 0    | 0    | 1    | 1    |

### Last 5 Rows
| Type       | Coverage   | OdName            | AREA | ... | 2010 | 2011 | 2012 | 2013 |
|------------|------------|-------------------|------|-----|------|------|------|------|
| Immigrants | Foreigners | State of Palestine| 935  | ... | 654  | 555  | 533  | 462  |
| Immigrants | Foreigners | Sudan             | 903  | ... | 612  | 531  | 444  | 343  |
| Immigrants | Foreigners | Suriname          | 904  | ... | 13   | 11   | 16   | 4    |
| Immigrants | Foreigners | Swaziland         | 903  | ... | 3    | 13   | 17   | 39   |
| Immigrants | Foreigners | Sweden            | 908  | ... | 159  | 134  | 140  | 140  |

## Data Structure
- **Shape**: (168, 43)
- **Columns**: ['Type', 'Coverage', 'OdName', 'AREA', 'AreaName', 'REG', 'RegName', 'DEV', 'DevName', 1980, ..., 2013]
- **Index**: RangeIndex (0-167)

## Data Cleaning
- Dropped NA columns
- Renamed columns:
  - 'OdName' → 'Country'
  - 'AreaName' → 'Continent'
  - 'RegName' → 'Region'

## Summary Statistics
| Metric | AREA    | REG      | ... | 2013    | Total     |
|--------|---------|----------|-----|---------|-----------|
| count  | 168.00  | 168.00   | ... | 168.00  | 168.00    |
| mean   | 912.36  | 1219.82  | ... | 1377.18 | 34246.48  |
| std    | 12.86   | 1136.59  | ... | 4500.73 | 88606.52  |
| min    | 903.00  | 905.00   | ... | 0.00    | 2726.00   |
| max    | 935.00  | 5501.00  | ... | 34129.00| 699242.00 |

## Requirements
- Python 3.x
- pandas
- numpy
- openpyxl

Install requirements with:
```bash
pip install pandas numpy openpyxl
