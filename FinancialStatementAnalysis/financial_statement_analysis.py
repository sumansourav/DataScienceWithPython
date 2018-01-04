#!/usr/bin/env/python3

import json
import ast
from numpy import mean

__author__ = 'sumansourav'


# Data Extraction -
# extract the revenue and source from data_file
with open('data_file.ipynb', 'r') as data_file:
    data = json.load(data_file)

# Due to string encoding of the list values, these steps are required.
revenue_str = data['cells'][0]['source'][1].split(" = ")[1]
expense_str = data['cells'][0]['source'][2].split(" = ")[1]
revenue = ast.literal_eval(revenue_str)  # monthly data
expense = ast.literal_eval(expense_str)  # monthly data with one-to-one correspondence with revenue

# Problem - Solution(Note: Refer to the problem_statement.pdf to check what the problem statements asks!)

# Profit
if len(revenue) != len(expense):
    print("[ERR] Revenue or expense for atleast a month is missing. Re-check data source!")
    exit(1)
profit = []
for index in range(len(revenue)):
    profit.append(revenue[index] - expense[index])
print("Monthly Profit:", profit)

# Tax - 30% of profit, 2 dec places
if not profit:
    print("[ERR] Profit calculation error. Recheck data source!")
    exit(1)
tax = [round(monthly_profit*0.3, 2) for monthly_profit in profit]
print("Monthly Tax:", tax)

# Net Profit = profit - tax
net_profit = []
for index in range(len(profit)):
    net_profit.append(profit[index] - tax[index])
print("Net Profit:", net_profit)

# # Profit Margin = Net Profit - Revenue
# profit_margin = []
# for index in range(len(profit)):
#     profit_margin.append(profit_margin[index]/revenue[index])
# print("Profit Margin: ", profit_margin)

# Mean Profit after tax
net_profit_mean = mean(net_profit)
print("Mean of Net Profit:", net_profit_mean)

# Good Months if profit after tax > mean tax
good_months = [index+1 for index in range(len(net_profit)) if net_profit[index] > net_profit_mean]  # 1 based indexing
print(good_months)

# Bad Months if profit after tax < mean tax
bad_months = [index+1 for index in range(len(net_profit)) if net_profit[index] < net_profit_mean]  # 1 based indexing
print(bad_months)

best_month = net_profit.index(max(net_profit)) + 1
worst_month = net_profit.index(min(net_profit)) + 1

print("Best Month: ", best_month)
print("Worst Month: ", worst_month)

# TODO: print every $ value in units of thousands rounded to 2 decimal places. Ex: round(value/1000, 2)
