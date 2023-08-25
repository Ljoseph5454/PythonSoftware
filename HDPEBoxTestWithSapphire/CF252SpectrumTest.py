import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd

df = pd.read_csv('CF252.csv')

print(df.head())

def formatter(x, pos):
    del pos
    return str(round(x/(10*(16/6)),3))

KE = df['KE_i'].tolist()
Number = df['Event'].tolist()

n=0
for i in KE:
    if i == 0:
        n+=1
print(n)    
    
KE = [i for i in KE if i != 0]

bins = np.linspace(0,10.2,200)
print(bins)
print(max(KE))


fig, ax = plt.subplots()
values, bins, patches = plt.hist(KE, bins, histtype = "step")
#plt.bar(KE, Number, width=0.2)
plt.xticks(np.arange(0, 10.5, 0.5))
plt.tick_params(axis='x', labelrotation=60)
plt.xlabel('CF252 Neutron Energy (MeV)')
plt.ylabel('Number of Events')
plt.title('CF252 Spectrum in Geant4')
ax.yaxis.set_major_formatter(formatter)

plt.yscale
plt.show()

print(values)