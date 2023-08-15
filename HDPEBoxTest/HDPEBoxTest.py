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
bins1=np.logspace(np.log10(0.000001),np.log10(10))
print(max(KEitemp))
print(min(KEi))

KEthermal = []
KEmedium = []
KEfast = []
KEunderthreshold = []
KEoverthreshold = []
for i in KEe:
    if i <= 0.000001:
        KEthermal.append(i)
    elif 0.000001 <= i <= 0.1:
        KEmedium.append(i)
    elif 0.1<= i:
        KEfast.append(i)
    if i <= 0.001:
        KEunderthreshold.append(i)
    elif i > 0.001:
        KEoverthreshold.append(i)
        
print(len(KEunderthreshold))
print(len(KEoverthreshold))
        
print('Out of the', len(KEe), '/', len(KEi), 'escapees:', len(KEthermal), 'were thermal (<1eV),', len(KEmedium), 'were medium (>1eV and <100keV), and', len(KEfast), 'were fast (>100keV)')
print('So the ratio of thermal to fast is', round(len(KEthermal)/len(KEfast),3), 'and the ratio of thermal to non thermal is', round(len(KEthermal)/(len(KEfast)+len(KEmedium)),3))
print('If neutrons <1keV will not produce events, then we get a good/bad neutron ratio of:', round(len(KEunderthreshold)/len(KEoverthreshold),3))

fig1, ax1 = plt.subplots()
#ax1.hist(KEe, bins1, histtype = "step", label = "Escape")
ax1.hist(np.clip(KEe, 0.000001, 10), bins1, histtype = "step", label = "Escape")
ax1.hist(np.clip(KEi, 0.000001, 10), bins1, histtype = "step", label = "Initial")
ax1.legend(loc="upper right", fontsize = 8)
ax1.set_xlabel('AMBE Neutron Energy (MeV)')
ax1.set_ylabel('Number of Events')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_title('Neutron Energy Spectrum of AMBE neutrons in a ' + thickness + ' HDPE box')
fig1.canvas.draw()
labels = [item.get_text() for item in ax1.get_xticklabels()]
labels[2] = '$<10^{-6}$'
ax1.set_xticklabels(labels)
#ax1.set_yscale('log')
ax1.legend(title='Ratio = ' + str(round(ratio,3)), loc='upper center')