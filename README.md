# International Immigration Data Analysis and Visualization to Canada from 1980 to 2013

## Description
The dataset contains annual data on the flows of international immigrants as recorded by the countries of destination. The data presents both inflows and outflows according to the place of birth, citizenship, or place of previous/next residence for both foreigners and nationals. The current version presents data pertaining to 45 countries.

## Table of Contents
1. Exploring Dataset
2. Indexing and Filtering
3. Visualizing Dataset
4. Line Plot of Dataset
5. Area Plot of Dataset
6. Histogram Plot of Dataset
7. Bar chart Plot of Dataset
### _______________________________________________________________________________________
# 1- Exploring Dataset
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
### _______________________________________________________________________________________
# 2- Indexing and Filtering

## Overview
This script demonstrates various techniques for **indexing and selecting data** from a dataset using **Pandas**. The dataset used in this example is an Excel file (`Canada.xlsx`) containing migration data.

## Requirements
Before running the script, ensure you have the following libraries installed:
- `numpy`
- `pandas`
- `openpyxl`
- `keras`

You can install the missing packages using:
```sh
pip install numpy pandas openpyxl keras
```

## Script Functionality
1. **Reading and Preprocessing the Dataset**
   - The dataset is loaded from an Excel file using `pd.read_excel()`.
   - Unnecessary rows and footers are skipped.
   - Column names are renamed for better clarity.

2. **Filtering Data**
   - Extracting the list of countries from the dataset.
   - Selecting specific columns (years 1980-1985) for all countries.

3. **Indexing Operations**
   - Setting the `Country` column as the index.
   - Retrieving full row data for a specific country (e.g., `Japan`).
   - Selecting a specific year for a country.
   - Extracting multiple years for a country.

4. **Converting Column Names to Strings**
   - Ensuring column names are of string type to prevent ambiguity in indexing.

5. **Filtering with Conditions**
   - Extracting data for Asian countries (`Continent = Asia`).
   - Applying multiple conditions to filter data further (e.g., `Southern Asia` region).

6. **Final Review of Data**
   - Displaying data dimensions and column names.
   - Showing the first few rows of the modified dataset.

## Running the Script
Simply execute the script in a Python environment:
```sh
python script_name.py
```
Make sure to update the file path for `Canada.xlsx` before running.

## Output
The script prints various filtered views of the dataset to the console, demonstrating different indexing and selection techniques in Pandas.

## Notes
- The dataset path should be adjusted based on your local directory structure.
- If encountering issues with `openpyxl`, ensure the package is installed properly.

This script serves as a practical guide for working with Pandas DataFrames, focusing on **indexing, slicing, and filtering data efficiently**.
### _______________________________________________________________________________________
# 3- Visualizing Dataset

## Overview
This repository contains visualizations of immigration trends from different continents over time. The graphs represent the number of immigrants from Africa, Asia, Europe, and the world to a specific country or region.

## Files
The following plots are included:

1. Displays immigration trends from African countries.
![Africa_plot](https://github.com/user-attachments/assets/89a395de-d558-48d5-b3fe-fe8de3ccc812)

2. Shows immigration trends from Asian countries.
![Asia_plot](https://github.com/user-attachments/assets/1e90c443-10df-4f8b-8a08-75ede9770962)

3. Illustrates immigration trends from European countries.
![Europe_plot](https://github.com/user-attachments/assets/4af652d6-45bb-4271-b25a-32cefe2e8403)

4. Represents immigration trends from all over the world.
![world](https://github.com/user-attachments/assets/059e6ccc-40b6-4785-8320-3d1491fb63ef)

## Description
Each graph plots the number of immigrants over a period of time (1980 - 2013), categorized by country. The trends help visualize migration patterns and how they evolved over the years.

## Usage
- Use these images to analyze migration trends from different continents.
- Compare the immigration rates from different regions.
- Identify peaks and declines in immigration numbers.
### _______________________________________________________________________________________
# 4- Line Plot of Dataset

## Overview
This project contains visualizations of immigration data from different countries over time. The included images showcase trends and significant events affecting immigration patterns.

## Images

### 1. China & India Immigration Trends
![China India](https://github.com/user-attachments/assets/039a1b5a-0dfa-43a9-8aba-e74be59e177f)

**Description:**
This line plot compares the number of immigrants from **China** and **India** to Canada from **1980 to 2013**. The trends highlight significant increases over time, with some fluctuations reflecting policy changes and global events.

### 2. Haiti Immigration Trends
![haiti_1](https://github.com/user-attachments/assets/c0b879bb-4683-4d23-bf57-463ab5106cdd)

**Description:**
This visualization displays immigration trends from **Haiti** to Canada over the years. The data indicates fluctuations in migration numbers, with notable variations across different periods.

### 3. Haiti Immigration and 2010 Earthquake Impact
![Haiti2010_1](https://github.com/user-attachments/assets/0eab1334-ef94-4d8a-80e9-202b5629999a)

**Description:**
This chart highlights immigration from **Haiti**, emphasizing the spike in **2010** due to the devastating **Haiti Earthquake**. The graph includes an annotation marking this significant event, demonstrating how humanitarian crises influence migration patterns.
### _______________________________________________________________________________________
# 5- Area Plot of Dataset
pending...

### _______________________________________________________________________________________
# 6- Histogram Plot of Dataset
pending...

### _______________________________________________________________________________________
# 7- Bar chart Plot of Dataset
pending...

### _______________________________________________________________________________________
## Usage
These images can be used for:
- Understanding historical immigration trends
- Analyzing the impact of global events on migration
- Supporting research or presentations on immigration patterns

## License
This project is licensed under the IBM License - see the [LICENSE](https://1drv.ms/b/c/52d0424acc8434f6/EfoB2LBMLllIsL8CcNbGAAIBT8B6VQ_HgJ7_AzA2-nq90Q?e=0TmsS3) file for details.
## Contact
For any inquiries or feedback, please contact Mahmoud Mohamed Abdallah at Mahmoud_abdallah20@outlook.com.
