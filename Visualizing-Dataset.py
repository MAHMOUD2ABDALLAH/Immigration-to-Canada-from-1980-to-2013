import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df_Canada = pd.read_excel(
    'C:\\Users\Mahmoud\Microsoft-PowerUp\Mahmoud Mohamed Abdallah - Documents\introDataAnalyse\Canada.xlsx',
    skiprows=range(20), skipfooter=2)
print('Data downloaded and read into a dataframe!')

years = list(map(str, range(1980, 2014)))
# Rename columns
df_Canada.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
df_Canada.set_index('Country', inplace=True)

# Ensure columns are strings
df_Canada.columns = df_Canada.columns.map(str)

# print("--------Let's compare the number of immigrants from all countries from 1980 to 2013.--------------")
#
df_all = df_Canada[years]
print(df_all.head())
print("---------------------------------------------------------------------------------------------------")
# we must first transpose the dataframe to swap the row and columns.
df_all = df_all.transpose()
print(df_all.head())
df_all.index = df_all.index.map(int)
df_all.plot(kind='line')
plt.title('Immigrants from All over the world')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.xlim(1980, 2013)
plt.ylim(0, 70000)
plt.legend(fontsize='5', loc='upper right', ncol=8)
plt.grid(True)
plt.show()
# print("--------Let's compare the number of immigrants of each Asia,Europe and Africa from 1980 to 2013.--------------")
# # Prompt the user for their choice
# choice_num = int(input(" 1-Asia\n 2-Europe\n 3-Africa\nEnter the number corresponding to your choice: "))
#
# # Check if the choice is valid and handle each region accordingly
# if choice_num == 1:
#     condition = df_Canada['Continent']=='Asia'
#     df_condition = df_Canada.loc[condition, years]
#     df_condition = df_condition.transpose()
#     print(df_condition.head())
#     print("---------------------------------------------------------------------------------------------------")
#     df_condition.plot(kind='line')
#     plt.title('Immigrants from Asia')
#     plt.ylabel('Number of Immigrants')
#     plt.xlabel('Years')
#     plt.xlim(0, 33)
#     plt.ylim(0, 70000)
#     plt.legend(fontsize='5', loc='upper right', ncol=8)
#     plt.grid(True)
#     plt.show()
# elif choice_num == 2:
#     condition = df_Canada['Continent'] == 'Europe'
#     df_condition = df_Canada.loc[condition, years]
#     df_condition = df_condition.transpose()
#     print(df_condition.head())
#     print("---------------------------------------------------------------------------------------------------")
#     df_condition.plot(kind='line')
#     plt.title('Immigrants from Europe')
#     plt.ylabel('Number of Immigrants')
#     plt.xlabel('Years')
#     plt.xlim(0, 33)
#     plt.ylim(0, 70000)
#     plt.legend(fontsize='5', loc='upper right', ncol=8)
#     plt.grid(True)
#     plt.show()
# elif choice_num == 3:
#     condition = df_Canada['Continent'] == 'Africa'
#     df_condition = df_Canada.loc[condition, years]
#     df_condition = df_condition.transpose()
#     print(df_condition.head())
#     print("---------------------------------------------------------------------------------------------------")
#     df_condition.plot(kind='line')
#     plt.title('Immigrants from Africa')
#     plt.ylabel('Number of Immigrants')
#     plt.xlabel('Years')
#     plt.xlim(0, 33)
#     plt.ylim(0, 70000)
#     plt.legend(fontsize='5', loc='upper right', ncol=8)
#     plt.grid(True)
#     plt.show()
