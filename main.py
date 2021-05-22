import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from regression import calculate_r_squared


datafr = pd.read_csv("medical.csv")
worst_fatality = datafr.sort_values(by=['fatality'], ascending=False).head(5)
#worst_fatality.plot(x='State', y='fatality', kind='line')
best_fatality = datafr.sort_values(by=['fatality']).head(5)
#best_fatality.plot(x='State', y='fatality', kind='line')

dict = {}
dict_heading = {'Hospitals':2, 'Hospital beds':3, 'ICU beds':4, 'Ventilators':5, 'fatality':6,
                     'population':7, 'deceased':8}
z = ['Hospitals', 'Hospital beds', 'ICU beds', 'Ventilators', 'fatality', 'population', 'deceased']
y = [(a, b) for a in z for b in z if a != b]
for i in y:
    x = []
    index1 = dict_heading[i[0]]
    index2 = dict_heading[i[1]]
    with open('medical.csv') as CSV_FILE2:
        med_data = csv.reader(CSV_FILE2)
        next(med_data)  # to skip the first row
        for row in med_data:
            #if str(row[1]) == "Delhi" or row[1] == "Punjab" or row[1] == "Sikkim" or row[1] == "Uttarakhand" or row[1] == "Goa":
                x.append((float(row[index1]), float(row[index2])))
    dict[i] = calculate_r_squared(x)

print(dict)
