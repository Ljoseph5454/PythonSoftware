import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
from math import log10, floor

file = "10cmNCrystal.csv"
thickness = file[:4]
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
        
for i in range(len(KEitemp)):
    if KEitemp[i] != 0:
        KEi.append(KEitemp[i])
        Hit.append(Hittemp[i])

print(len(Hit))
print(len(KEe))
print(len(KEi))

ratio = len(KEe)/len(Hit)
a = (len(KEe))**0.5/len(Hit)
ratio_err = round(a, -int(floor(log10(abs(a)))))

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

goodbad = len(KEunderthreshold)/len(KEoverthreshold)
b = (len(KEe)/(len(KEe)-len(KEunderthreshold))**2)*(len(KEunderthreshold))**0.5
goodbad_err = round(b, -int(floor(log10(abs(b)))))
        
print('Out of the', len(KEe), '/', len(KEi), 'escapees:', len(KEthermal), 'were thermal (<1eV),', len(KEmedium), 'were medium (>1eV and <100keV), and', len(KEfast), 'were fast (>100keV)')
print('So the ratio of thermal to fast is', round(len(KEthermal)/len(KEfast),3), 'and the ratio of thermal to non thermal is', round(len(KEthermal)/(len(KEfast)+len(KEmedium)),3))
print('If neutrons <1keV will not produce events, then we get a good/bad neutron ratio of:', round(goodbad,3))

fig1, ax1 = plt.subplots()
#ax1.hist(KEe, bins1, histtype = "step", label = "Escape")
ax1.hist(np.clip(KEe, 0.000001, 10), bins1, histtype = "step", label = "Escape")
ax1.hist(np.clip(KEi, 0.000001, 10), bins1, histtype = "step", label = "Initial")
ax1.legend(loc="upper right", fontsize = 8)
ax1.set_xlabel('AMBE Neutron Energy (MeV)')
ax1.set_ylabel('Number of Events')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_title('Neutron Spectrum of AMBE neutrons in a ' + thickness + ' HDPE (NCrystal) box')
fig1.canvas.draw()
labels = [item.get_text() for item in ax1.get_xticklabels()]
labels[2] = '$<10^{-6}$'
ax1.set_xticklabels(labels)
#ax1.set_yscale('log')
ax1.legend(title='Escape Ratio = ' + str(round(ratio,3)) + '±' + str(ratio_err) + '\n' + 'Good/Bad Ratio = ' + str(round(goodbad,3)) + '±' + str(goodbad_err), loc='upper center')
