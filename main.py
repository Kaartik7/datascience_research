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

x = []
with open('medical.csv') as CSV_FILE2:
    med_data = csv.reader(CSV_FILE2)
    next(med_data)  # to skip the first row
    for row in med_data:
        x.append((float(row[3]),float(row[6])))
print(calculate_r_squared(x))
