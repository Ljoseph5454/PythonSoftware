import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd

df = pd.read_csv('AMBE1.csv')

print(df.head())

KE = df['Hit'].tolist()
Number = df['Event'].tolist()

n=0
for i in KE:
    if i == 0:
        n+=1
print(n)    
    
KE = [i for i in KE if i != 0]

bins = np.linspace(0,10.2,52)
print(bins)
print(max(KE))

values, bins, patches = plt.hist(KE, bins, histtype = "step")
#plt.bar(KE, Number, width=0.2)
plt.xticks(np.arange(0, 10.5, 0.5))
plt.tick_params(axis='x', labelrotation=60)
plt.xlabel('AMBE Neutron Energy (MeV)')
plt.ylabel('Number of Events')

print(values)