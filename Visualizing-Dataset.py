# In 2010, Haiti suffered a catastrophic magnitude 7.0 earthquake.
# The quake caused widespread devastation and loss of life and aout three million people were affected by this natural disaster.
# As part of Canada's humanitarian effort, the Government of Canada stepped up its effort in accepting refugees from Haiti.
# We can quickly visualize this effort using a Line plot:
from pkgutil import extend_path

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

# First, we will extract the data series for Haiti.
# haiti = df_Canada.loc['Haiti', years]
# print(haiti.head())
# let's change the index values of Haiti to type integer for plotting
# haiti.index = haiti.index.map(int)
# haiti.plot(kind='line')
# plt.title('Immigration from Haiti')
# plt.ylabel('Number of immigrants')
# plt.xlabel('Years')
# plt.grid(True)
# plt.show() <---- Uncomment me if you want the previous visual
# print("---------------------------------------------------------------------------------------------------")
# We can clearly observe a significant increase in the number of immigrants from Haiti starting in 2010,
# coinciding with Canada's increased efforts to accept Haitian refugees.
# print("------------------------------Let's annotate this spike on the plot.-------------------------------")
# plt.text(2000, 6000, "2010 Earthquake")
# plt.show() <---- Uncomment me if you want the previous visual

# We can easily add more countries to line plot to make meaningful comparisons immigration from different countries.
# print("--------Let's compare the number of immigrants from India and China from 1980 to 2013.-------------")
# # Let's compare the number of immigrants from India and China from 1980 to 2013.
# # df_CI = df_Canada.loc[['India', 'China'], years]
# # print(df_CI.head())
# # print("---------------------------------------------------------------------------------------------------")
# # # we must first transpose the dataframe to swap the row and columns.
# # df_CI = df_CI.transpose()
# # print(df_CI.head())
# # df_CI.index = df_CI.index.map(int)
# # df_CI.plot(kind='line')
# # plt.title('Immigrants from China and India')
# # plt.ylabel('Number of Immigrants')
# # plt.xlabel('Years')
# # plt.show()
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
