# The dataset contains annual data on the flows of international immigrants as recorded by the countries of destination.
# The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals.
# The current version presents data pertaining to 45 countries.

import numpy as np
import pandas as pd
import openpyxl

df_Canada = pd.read_excel(
    'C:\\Users\Mahmoud\Microsoft-PowerUp\Mahmoud Mohamed Abdallah - Documents\introDataAnalyse\Canada.xlsx',
    skiprows=range(20), skipfooter=2)
print('Data downloaded and read into a dataframe!')


def invalid_option():
    return "Invalid option"


def view (value):
    if value == '1':
        return df_Canada.head()  # Getting first 5 rows of the dataset
    elif value == '2':
        return df_Canada.tail()  # View the bottom 5 rows of the dataset
    elif value == '3':
        return df_Canada.info(verbose=False)  # Short summary about the dataframe
    elif value == '4':
        return df_Canada.columns  # Knowing headers
    elif value == '5':
        return df_Canada.index  # Indices
    elif value == '6':
        return type(df_Canada.columns.tolist()), type(df_Canada.index.tolist())  # Changing index and columns to list
    elif value == '7':
        return df_Canada.shape  # Showing the shape of the dataset
    elif value == '8':
        return df_Canada.drop(df_Canada, axis=1, inplace=True)  # Cleaning unnecessary and null values from it
    else:
        return invalid_option()

value = input("choose the visualization option:")
result = view(value)
print(result)
