# International Immigration Data Analysis and Visualization to Canada from 1980 to 2013

## Description
The dataset contains annual data on the flows of international immigrants as recorded by the countries of destination. The data presents both inflows and outflows according to the place of birth, citizenship, or place of previous/next residence for both foreigners and nationals. The current version presents data pertaining to 45 countries.

## Table of Contents
1. Exploring Dataset
2. Indexing and Filtering
3. Visualizing Dataset
4. Line Plot of Dataset
5. License
6. Contact

## Exploring Dataset
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
### _________________________________________________________________________________________________________________________
## Indexing and Filtering
pending....
## Visualizing Dataset
pending....
## Line Plot of Dataset
pending....
## License
This project is licensed under the IBM License - see the [LICENSE](https://1drv.ms/b/c/52d0424acc8434f6/EfoB2LBMLllIsL8CcNbGAAIBT8B6VQ_HgJ7_AzA2-nq90Q?e=0TmsS3) file for details.
## Contact
For any inquiries or feedback, please contact Mahmoud Mohamed Abdallah at Mahmoud_abdallah20@outlook.com.
