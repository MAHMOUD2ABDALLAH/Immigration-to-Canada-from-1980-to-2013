# Canada Immigration Data Analysis

## Project Overview
This project analyzes international immigration flows to Canada using a dataset containing annual data on inflows and outflows. The dataset includes information from 45 countries and covers the period from 1980 to 2013.

## Dataset
**File:** Canada.xlsx

**Description:** Contains immigration data for Canada, including country of origin, continent, and region.

### Columns:
- **Type:** Type of immigration (e.g., Immigrants)
- **Coverage:** Coverage type (e.g., Foreigners)
- **Country:** Origin country of immigrants
- **Continent:** Continent of the origin country
- **Region:** Region of the origin country
- **Year Columns (1980-2013):** Number of immigrants per year
- **Total:** Total number of immigrants from 1980 to 2013

## Requirements
- Python 3.x
- Required libraries:
  - numpy
  - pandas
  - openpyxl

## Setup Instructions
1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure the `Canada.xlsx` dataset is placed in the correct directory.

## Script Usage

### analyze_data.py
- Reads and cleans the dataset
- Provides statistical summaries
- Renames columns for better readability
- Adds a Total column to sum up immigration data for each country

#### Steps in `analyze_data.py`
1. Load necessary libraries (numpy, pandas, openpyxl).
2. Read the Excel file into a Pandas DataFrame.
3. Display the first and last five rows to inspect data.
4. Get a concise summary of the dataset using `info()`.
5. Retrieve column headers and index values.
6. Convert index and columns to lists for better manipulation.
7. Display the shape of the dataset (rows, columns).
8. Remove unnecessary/null values to clean the dataset.
9. Rename columns (OdName to Country, AreaName to Continent, etc.).
10. Add a Total column summing immigration numbers (1980-2013).
11. Check for null values to ensure data integrity.
12. Generate statistical summaries using `describe()`.

## Features
- Reads Excel data into a Pandas DataFrame.
- Cleans unnecessary and null values.
- Renames columns for better readability.
- Summarizes immigration data with key statistics.
- Adds a total column for immigration data from 1980-2013.

## Contact
**Author:** Mahmoud Mohamed Abdallah  
**Email:** [Mahmoud_abdallah20@outlook.com](mailto:Mahmoud_abdallah20@outlook.com)
