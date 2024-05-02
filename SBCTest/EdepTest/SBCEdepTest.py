import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
import uproot
import math
#from matplotlib.ticker import (LogLocator, MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

filename = "Data1.root" #EdepSap5cmx7.5cm3cmPad10cm25cmAmLi
file = uproot.open(filename)["tree1"]
print(file.keys())
df = file.arrays(["EDep", "EventNo"], library="pd")

EDep = df['EDep'].tolist()
EDep = [i*10**6 for i in EDep]
#print(EDep)
EventNo = df['EventNo'].tolist()

threshold = 1000

#print(EventNo)

OverThresholdScatters = []
ElasticTot = []

n=0
for i in EDep: #Creates a 2d list with event no. and EDep only if EDep of the scatter > 1keV
    if i > threshold:
        OverThresholdScatters.append([EventNo[n],i])
    n+=1

#for i in range(0, len(EDep)): #Creates a 2d list with event no. and EDep only if EDep of the scatter > 1keV
#    if EDep[i] > 1000:
#        OverThresholdScatters.append([EventNo[i],i])

print(OverThresholdScatters)
OverThresholdSingleScatters = [] 

#169, 192, 280, 626, 970, 1870, 1911, 1936, 2043, 2075, 2210, 2368, 2511, 2558, 
#2695!!!!!, 2744!!!!!!, 2753, 3131!!!!, 3225, 3599

for i in range(0, len(OverThresholdScatters)): #Counts the amount of single over threshold scatters
    if i == 0:
        if OverThresholdScatters[i][0] != OverThresholdScatters[i+1][0]:
            OverThresholdSingleScatters.append(OverThresholdScatters[i][0])
    elif i == len(OverThresholdScatters)-1:
        if OverThresholdScatters[i][0] != OverThresholdScatters[i-1][0]:
            OverThresholdSingleScatters.append(OverThresholdScatters[i][0])
    else:
        if (OverThresholdScatters[i][0] != OverThresholdScatters[i-1][0]) and (OverThresholdScatters[i][0] != OverThresholdScatters[i+1][0]):
            OverThresholdSingleScatters.append(OverThresholdScatters[i][0])
 

print(OverThresholdSingleScatters)
#print(EventNo)
print(len(EventNo))
print(len(EDep))
print(len(OverThresholdScatters))
#print(OverThresholdScatters)
#print(OverThresholdSingleScatters)
#print(EventNo)
#print("# of captures is", len(NCaptureTot))
print("# of scatterers over the 1keV threshold is", len(OverThresholdScatters))
print("# of events with only one 1keV scatter is", len(OverThresholdSingleScatters))



bottombin = 1e-4
binnumke = 100
bins = np.logspace(np.log10(bottombin),np.log10(max(EDep)), binnumke)
bins1 = np.linspace(0, 1000000, 1000)

fig1, ax1 = plt.subplots()
#ax1.hist(KEe, bins1, histtype = "step", label = "Escape")
ax1.hist(EDep, bins, histtype = "step", label = "Escape")
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('AmLi Neutron Energy (eV)')
ax1.set_ylabel('Number of Events')
ax1.set_title('Energy Depositions in LAr from Elastic Scatterers')
#ax1.xaxis.set_ticks(np.logspace(np.log10(bottombin), 1, num=1-int(np.log10(bottombin))+1))
ax1.xaxis.set_major_locator(ticker.LogLocator(numticks=999))
ax1.xaxis.set_minor_locator(ticker.LogLocator(numticks=999, subs="auto"))
plt.axvline(x = 1000, color = 'red', linestyle = '--', alpha = 0.5, label = "Elastic Max")