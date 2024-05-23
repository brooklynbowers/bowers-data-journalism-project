# Getting to Know the Data

# referencing the excel file separately

# import necessary packages
!pip install openai
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker
import os

from openai import OpenAI

# first tasks: 
# import the data
# check the data types
# check data rows/ column headers
# check data delimiter types

########################

# import the data

# pd.read_csv() directly reads the data from the CSV file and automatically converts it into a pandas DataFrame
av_hourly_wages_female = pd.read_csv('')
av_hourly_wages_male = pd.read_csv('')
av_hourly_wages_overall = pd.read_csv('', sep ='\t')
av_hourly_wages_full_time = pd.read_csv('')
av_hourly_wages_part_time = pd.read_csv('')
total_employee_wages = pd.read_csv('')

# check data types

# this function can be called to print the data types
def print_data_types(df, category):
    print(f'Data Types for {category}: ')
    print(df.dtypes)
    print('\n')

# calling the function to print data types for each category
print_data_types(hourly_wages_female, 'Average Female Hourly Wages')
print_data_types(hourly_wages_male, 'Average Male Hourly Wages')
print_data_types(hourly_wages_overall, 'Average Overall Hourly Wages')
print_data_types(hourly_wages_full_time, 'Average Full Time Hourly Wages')
print_data_types(hourly_wages_part_time, 'Average Part Time Hourly Wages')
print_data_types(total_employee_wages, 'Total Employee Wages')

# function to print the row headers of the dataframe
# using 'dataframe.index'
def print_row_headers(df, category):
  print(f'Row headers for {category}: ')
  print(df.index)
  print('/n')

# calling the function to print row headers for each category
print_row_headers(hourly_wages_female, 'Average Female Hourly Wages')
print_row_headers(hourly_wages_male, 'Average Male Hourly Wages')
print_row_headers(hourly_wages_overall, 'Average Overall Hourly Wages')
print_row_headers(hourly_wages_full_time, 'Average Full Time Hourly Wages')
print_row_headers(hourly_wages_part_time, 'Average Part Time Hourly Wages')
print_row_headers(total_employee_wages, 'Total Employee Wages')

# function to print the column headers of the dataframe
# using 'dataframe.columns'
def print_column_headers(df, category):
  print(f'Column headers for {category}: ')
  print(df.index)
  print('/n')

# calling the function to print column headers for each category
print_column_headers(hourly_wages_female, 'Average Female Hourly Wages')
print_column_headers(hourly_wages_male, 'Average Male Hourly Wages')
print_column_headers(hourly_wages_overall, 'Average Overall Hourly Wages')
print_column_headers(hourly_wages_full_time, 'Average Full Time Hourly Wages')
print_column_headers(hourly_wages_part_time, 'Average Part Time Hourly Wages')
print_column_headers(total_employee_wages, 'Total Employee Wages')

# checking the delimeter types to specify the separation between the data
def find_delimiter(filename):
    sniffer = csv.Sniffer()
    with open(filename) as fp:
        delimiter = sniffer.sniff(fp.read(5000)).delimiter
    return delimiter

print('the delimiter used in the Average_Hourly_Wages_Female_Canadian csv file is: ')
print(find_delimiter('/content/drive/My Drive/Lonely Octopus Files/projects/Project 16 - Data Journalism/Average_Hourly_Wages_Female_Canadian.csv'))
print('\n')
#
print('the delimiter used in the Average_Hourly_Wages_Male_Canadian csv file is: ')
print(find_delimiter('/content/drive/My Drive/Lonely Octopus Files/projects/Project 16 - Data Journalism/Average_Hourly_Wages_Male_Canadian.csv'))
print('\n')
#
print('the delimiter used in the Average_Hourly_Wages_Overall_Canadian csv file is: ')
print(find_delimiter('/content/drive/My Drive/Lonely Octopus Files/projects/Project 16 - Data Journalism/Average_Hourly_Wages_Overall_Canadian.csv'))
print('\n')

print('the delimiter used in the Average_Weekly_Wages_Full-time_Canadian csv file is: ')
print(find_delimiter('/content/drive/My Drive/Lonely Octopus Files/projects/Project 16 - Data Journalism/Average_Weekly_Wages_Full-time_Canadian.csv'))
print('\n')

print('the delimiter used in the Average_Weekly_Wages_Part-time_Canadian csv file is: ')
print(find_delimiter('/content/drive/My Drive/Lonely Octopus Files/projects/Project 16 - Data Journalism/Average_Weekly_Wages_Part-time_Canadian.csv'))
print('\n')

print('the delimiter used in the Total_Employee_Wages_Canadian csv file is: ')
print(find_delimiter('/content/drive/My Drive/Lonely Octopus Files/projects/Project 16 - Data Journalism/Total_Employee_Wages_Canadian.csv'))
print('\n')
