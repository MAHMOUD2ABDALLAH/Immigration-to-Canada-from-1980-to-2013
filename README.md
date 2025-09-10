# 2- Indexing and Filtering Dataset

This branch demonstrates advanced pandas operations for:
- Column-based filtering
- Index manipulation
- Boolean indexing
- Multi-criteria selection

## Key Operations
1. **Basic Filtering**: Select specific columns/years
2. **Index Selection**: Retrieve records using `.loc[]`
3. **Conditional Filtering**: 
   - Filter by continent (Asia)
   - Filter by region (Southern Asia)
4. **Data Conversion**: Convert numeric columns to strings

## Files
- `Indexing-Filtering.py`: Main script
- `OUTPUT.md`: Expected output preview

## Usage

python Indexing-Filtering.py

# Operations Output
## Basic Filtering
### Country List (First 5)

#### 1 Afghanistan
#### 2 Albania
#### 3 Algeria
#### 4 American Samoa
#### 5 Andorra
#### Name: Country, Length: 168

### 1980-1985 Data Sample
| Country          | 1980 | 1981 | 1982 | 1983 | 1984 | 1985 |
|------------------|------|------|------|------|------|------|
| Afghanistan      | 16   | 39   | 39   | 47   | 71   | 340  |
| Albania          | 1    | 0    | 0    | 0    | 0    | 0    |

## Index-Based Selection
### Japan's Immigration Data
- **2013**: 982 immigrants
- **1980-1985**:
#### 1980 -> 701
#### 1981 -> 756
#### 1982 -> 598
#### 1983 -> 309
#### 1984 -> 246
#### 1985 -> 198

## Advanced Filtering
### Asian Countries (40 countries)
Sample:
- Afghanistan (2004 immigrants in 2013)
- China (34,129 immigrants in 2013)
- Japan (982 immigrants in 2013)

### Southern Asia Countries (9 countries)
1. Afghanistan
2. Bangladesh
3. Bhutan
4. India
5. Iran
6. Maldives
7. Nepal
8. Pakistan
9. Sri Lanka

## Final Dataset Structure
- **Dimensions**: 168 countries × 42 columns
- **Columns**: ['Type', 'Coverage', 'AREA', ..., '2013']
```
Indexing-and-Filtering/
├── data/
│   └── Canada.xlsx
├── scripts/
│   └── Indexing-Filtering.py
├── output/
│   └── OUTPUT.md
└── README.md
```
