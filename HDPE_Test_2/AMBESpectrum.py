import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd

df = pd.read_csv('AMBESpectrum.csv')

print(df.head())

KE = df['KE'].tolist()
Number = df['Number'].tolist()

Data = []

for i in range(len(KE)):
    Data.extend([KE[i]]*Number[i])

bins = np.linspace(0,10,50)

data = plt.hist(Data, bins, histtype = "step")
plt.xticks(np.arange(0, 10.5, 0.5))
plt.tick_params(axis='x', labelrotation=60)
plt.xlabel('AMBE Neutron Energy (MeV)')
plt.ylabel('Number of Events')