import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

North = ["Jammu & Kashmir", "Punjab", "Delhi", "Himachal Pradesh", "Uttarakhand", "Haryana", "Uttar Pradesh", "Chandigarh"]
South = ["Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh", "Telangana", "Puducherry"]
East = []
West = []

datafr = pd.read_csv("medical.csv")
dn = datafr.loc[datafr['State'].isin(North)]
ds = datafr.loc[datafr['State'].isin(South)]
dn.plot(x='State', y='fatality', kind='line')
ds.plot(x='State', y='fatality', kind='line')

#1.48
#0.88
