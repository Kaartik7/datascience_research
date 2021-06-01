import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('medical.csv')
df.sort_values(by=['deceased'], inplace=True, ascending=False)
kf = df.head(10)
product_data = kf["State"]
bug_data = kf["deceased"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]

plt.pie(bug_data, labels=product_data, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.show()
