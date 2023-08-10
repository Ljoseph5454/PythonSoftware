import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd

file = "10cm.csv"
thickness = file[0:-4]
print(thickness)
df = pd.read_csv(file)

KEitemp = df['KE_i'].tolist()
KEetemp = df['KE_e'].tolist()
Hittemp = df['Hit'].tolist()

print(df.head())

n = 0
for i in KEitemp:
    if i == 0:
        n+=1
print(n)

KEe = []
KEi = []
Hit = []
for i in range(len(Hittemp)):
    if Hittemp[i] == 1:
        KEe.append(KEetemp[i])

for i in KEitemp:
    if i != 0:
        KEi.append(i)
        Hit.append(Hittemp)        

print(len(Hit))
print(len(KEe))
print(len(KEi))

ratio = len(KEe)/len(Hit)

bins = np.linspace(0,10.2,52)
print(bins)
print(max(KEitemp))

fig1, ax1 = plt.subplots()
ax1.hist(KEe, bins, histtype = "step", label = "Escape")
ax1.hist(KEi, bins, histtype = "step", label = "Initial")
#plt.plot(xe,ye,'ro')
#plt.errorbar(xe,ye,ye_err,ecolor='r',ls='none', label='Experimental Data')
ax1.legend(loc="upper right", fontsize = 8)
#ax1.xticks(np.arange(0, 10.5, 0.5))
#ax1.tick_params(axis='x', labelrotation=60)
ax1.set_xlabel('AMBE Neutron Energy (MeV)')
ax1.set_ylabel('Number of Events')
ax1.legend(loc="upper right")
ax1.set_xscale('log')
ax1.set_title('Neutron Energy Spectrum of AMBE neutrons in a ' + thickness + ' HDPE box')
#ax1.set_yscale('log')
ax1.text(7.5, 20000, 'Ratio = ' + str(round(ratio,3)), ha='center', va='center')