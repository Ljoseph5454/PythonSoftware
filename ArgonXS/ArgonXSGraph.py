import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd


df = pd.read_csv("TotalArXS.csv")
df1 = pd.read_csv("ElasticArXS.csv")
df2 = pd.read_csv("CaptureArXS.csv")

print(df.head())
print(df1.head())
print(df2.head())

Etot = df[df['Energy']>=1]['Energy'].tolist()
XStot = df[df['Energy']>=1]['XS'].tolist()
Eel = df1[df1['Energy']>=1]['Energy'].tolist()
XSel = df1[df1['Energy']>=1]['XS'].tolist()
Ecap = df2[df2['Energy']>=1]['Energy'].tolist()
XScap = df2[df2['Energy']>=1]['XS'].tolist()

fig,ax = plt.subplots()
ax.plot(Etot,XStot,'-o', markersize=1, label='Total')
ax.plot(Eel,XSel,'-o', markersize=1, label='Elastic')
ax.plot(Ecap,XScap,'-o', markersize=1, label='Capture')
plt.xlabel('Incident Energy (eV)')
plt.ylabel('Cross Section (b)')
plt.title('18-Ar-40 XS')
ax.set_axisbelow(True)
plt.grid(linestyle='--')
plt.legend(loc='lower right')
ax.set_xscale('log')
ax.set_yscale('log')

#KEitemp = df['KE_i'].tolist()

