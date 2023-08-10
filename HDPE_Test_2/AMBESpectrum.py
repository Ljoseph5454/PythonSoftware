import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd

df = pd.read_csv('AMBESpectrum.csv')

print(df.head())

KE = df['KE'].tolist()
Number = df['Number'].tolist()

print(sum(Number))

Data = []

for i in range(len(KE)):
    Data.extend([KE[i]]*Number[i])
    
Data = [i+0.001 for i in Data]

bins = np.linspace(0,10.2,52)
print(bins)

print(Number)

data = plt.hist(Data, bins, histtype = "step")
#plt.bar(KE, Number, width=0.2)
plt.xticks(np.arange(0, 10.5, 0.5))
plt.tick_params(axis='x', labelrotation=60)
plt.xlabel('AMBE Neutron Energy (MeV)')
plt.ylabel('Number of Events')