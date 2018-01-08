#!/usr/bin/env/python3

import json
import ast
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



__author__ = 'sumansourav'


# Data Extraction -

# Part1 from ipynb arrays
with open('../2_Prepared_Data/country_life_expectancy_data.ipynb', 'r') as data_file:
    json_data = json.load(data_file)

# Due to string encoding of the list values, these steps are required.
Country_Code_str = json_data['cells'][2]['source'][1].split(" = ")[1].split("(")[1].split(")")[0]
Life_Expectancy_At_Birth_1960_str = json_data['cells'][2]['source'][2].split(" = ")[1].split("(")[1].split(")")[0]
Life_Expectancy_At_Birth_2013_str = json_data['cells'][2]['source'][3].split(" = ")[1].split("(")[1].split(")")[0]
Countries_2012_Dataset_str = json_data['cells'][4]['source'][1].split(" = ")[1].split("(")[1].split(")")[0]
Codes_2012_Dataset_str = json_data['cells'][4]['source'][2].split(" = ")[1].split("(")[1].split(")")[0]
Regions_2012_Dataset_str = json_data['cells'][4]['source'][3].split(" = ")[1].split("(")[1].split(")")[0]

Country_Code = ast.literal_eval(Country_Code_str)
Life_Expectancy_At_Birth_1960 = ast.literal_eval(Life_Expectancy_At_Birth_1960_str)
Life_Expectancy_At_Birth_2013 = ast.literal_eval(Life_Expectancy_At_Birth_2013_str)
Countries_2012_Dataset = ast.literal_eval(Countries_2012_Dataset_str)
Codes_2012_Dataset = ast.literal_eval(Codes_2012_Dataset_str)
Regions_2012_Dataset = ast.literal_eval(Regions_2012_Dataset_str)

# print(len(Country_Code))
# print(len(Life_Expectancy_At_Birth_1960))
# print(len(Life_Expectancy_At_Birth_2013))
# print(len(Countries_2012_Dataset))
# print(len(Codes_2012_Dataset))
# print(len(Regions_2012_Dataset))


# Part2 from csv
data = pd.read_csv('../2_Prepared_Data/DemographicData.csv')
# Remove spaces from Data Columns
new_column_names = []
for column_names in list(data.columns):
    new_column_names.append(column_names.replace(" ", ""))
data.columns = new_column_names


# Problem - Solution(Note: Refer to the problem_statement.pdf to check what the problem statements asks!)

# Create the plot colored by IncomeGroup
vis1 = sns.lmplot(data=data, x="Birthrate", y="Internetusers", fit_reg=False, hue="IncomeGroup")
plt.show()

# Add country data to the pandas dataframe
country_data = pd.DataFrame({"CountryName": np.array(Countries_2012_Dataset),
                             "CountryCode": np.array(Codes_2012_Dataset),
                             "CountryRegion": np.array(Regions_2012_Dataset)})

# Merge country_data with data dfs.
merged_data = pd.merge(left=data, right=country_data, how="inner", on="CountryCode")

# Create the plot colored by CountryRegion
vis2 = sns.lmplot(data=merged_data, x="Birthrate", y="Internetusers", fit_reg=False, hue="CountryRegion")
plt.show()

# Add life expectancy data to the pandas dataframe
life_exp_data = pd.DataFrame({"CountryCode": np.array(Country_Code),
                              "LifeExp1960": np.array(Life_Expectancy_At_Birth_1960),
                              "LifeExp2013": np.array(Life_Expectancy_At_Birth_2013)
                              })

# Merge life_exp_data with data dfs.
merged_data = pd.merge(left=merged_data, right=life_exp_data, how="inner", on="CountryCode")

# Any duplicate columns after merges tend to get the column names changed
# In this case CountryName changes to CountryName_x and CountryName_y
# Delete column
del merged_data['CountryName_y']
merged_data.rename(columns={'CountryName_y': 'CountryName'}, inplace=True)

# Create the BirthRate vs LifeExpectancy curve
vis3 = sns.lmplot(data=merged_data, x="Birthrate", y="LifeExp1960", fit_reg=False, hue="CountryRegion")
plt.show()
vis4 = sns.lmplot(data=merged_data, x="Birthrate", y="LifeExp2013", fit_reg=False, hue="CountryRegion")
plt.show()
