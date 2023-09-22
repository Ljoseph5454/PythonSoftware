import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
import uproot
import math
#from matplotlib.ticker import (LogLocator, MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

def my_div(dividend, divisor):
    try:
        return dividend/divisor
    except ZeroDivisionError:
        if dividend == 0:
            raise ValueError('0/0 is undefined')
            # instead of raising an error, an alternative
            # is to return float('nan') as the result of 0/0

        if dividend > 0:
            return float('inf')
        else:
            return float('-inf')

filename = "CF25230cmWithFeCd.root"
file = uproot.open(filename)["tree"]
print(file.keys())
#print(file.keys())
thickness = filename[0:-5]
print(thickness)
df = file.arrays(["Hit", "x", "y", "z", "KEinitial", "KEescape", "px", "py", "pz"], library="pd")
#df = pd.read_csv(file)

KEi = df['KEinitial'].tolist()
Hit = df['Hit'].tolist()

KEetemp = df['KEescape'].tolist()

print(df.head())


KEe = []        
for i in range(len(KEetemp)):
    if KEetemp[i] > 0:
        KEe.append(KEetemp[i])

ratio = len(KEe)/len(Hit)

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

bottombin = 1e-9

binnumke = 100
bins = np.linspace(0,10.2,52)
bins1=np.logspace(np.log10(bottombin),np.log10(10), binnumke)



xlabels = ['$<10^{-9}$', '$10^{-8}$', '$<10^{-7}$', '$10^{-6}$', '$10^{-5}$', '$10^{-4}$', '$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$1$', '$10$']

fig1, ax1 = plt.subplots(figsize=(16,10))
#ax1.hist(KEe, bins1, histtype = "step", label = "Escape")
#ax1.xaxis.set_major_locator(LogLocator(base=10))
ax1.hist(np.clip(KEe, bottombin, 10), bins1, histtype = "step", label = "Escape")
ax1.hist(np.clip(KEi, bottombin, 10), bins1, histtype = "step", label = "Initial")
ax1.legend(loc="upper left", fontsize = 8)
ax1.set_xlabel('Cf252 Neutron Energy (MeV)')
ax1.set_ylabel('Number of Events')
plt.axvline(x = 0.001, color = 'red', linestyle = '--', alpha = 0.5, label = "Elastic Max")
ax1.set_title('Neutron Energy Spectrum of Cf252 Neutrons')
ax1.set_xscale('log')
ax1.set_yscale('log')
#start, end = ax1.get_xlim()
#print(start, end)
ax1.set_xlim(bottombin/2, 10)
ax1.xaxis.set_ticks(np.logspace(np.log10(bottombin), 1, num=1-int(np.log10(bottombin))+1))
ax1.legend(title='Escape Ratio = ' + str(round(ratio,3)) + '\n' + 'Good/Bad Ratio = ' + str(round(my_div(len(KEunderthreshold),len(KEoverthreshold)),3)), loc='upper left')
#print(labels)
#labels[2] = '$<10^{-7}$'
#ax1.set_xticklabels(labels)
#ax1.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=8))
#ax1.xaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=(0.2,0.4,0.6,0.8), numticks=5))
#ax1.xaxis.set_minor_formatter(ticker.FormatStrFormatter('%.2f'))
#plt.grid(True, which="both",ls="--")
ax1.xaxis.set_major_locator(ticker.LogLocator(numticks=999))
ax1.xaxis.set_minor_locator(ticker.LogLocator(numticks=999, subs="auto"))
plt.show()