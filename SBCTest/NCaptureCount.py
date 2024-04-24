import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
import uproot
import math
#from matplotlib.ticker import (LogLocator, MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

filename = "Data.root" #Sap5cmx7.5cm3cmPad10cm25cmAmLi

file = uproot.open(filename)["tree"]
print(file.keys())
df = file.arrays(["CaptureCount", "ElasticCount", "ElCap", "ElCapLocation", "ComptCount", "EventNo"], library="pd")
#df = file.arrays(["Hit", "x"], library="pd")

LArCapture = df['CaptureCount'].tolist()
Elastic = df['ElasticCount'].tolist()
ElCap = df['ElCap'].tolist()
ElCap = [int(i) for i in ElCap]
ComptCount = df['ComptCount'].tolist()
ComptCount = [int(i) for i in ComptCount]
ElCapLocation = df['ElCapLocation'].tolist()
ElCapLocation = [int(i) for i in ElCapLocation]

#print(ComptCount)

TotalCompt = [] # Creates a 2D array with eventNo and # of Compt events in the LAr

for i in range(0, len(ComptCount)):
    if ComptCount[i] > 0:
        TotalCompt.append([ComptCount[i],i])
        
print(len(TotalCompt))

ElCapTot = 0

for i in ElCap: #Counts the number of captures which happened after a scatter in LAr
    if i != 0:
        ElCapTot += 1
        
#print(ElCap)

#1 = LAr, 2 = Pressure Vessel, 3 = Vacuum Vessel, 4 = Cu Reflectors, 5 = Top Flange, 6 = HDPE

CapVolume = [0,0,0,0,0,0,0] #Creates an array which counts number of captures in above volumes
LArCaptureTot = []
ElasticTot = []
Hit1 = [1,0,0,1]

for i in ElCapLocation: #Adds 1 for each volume there is a capture in
    CapVolume[i] += 1

    
for i in range(0, len(LArCapture)): #Counts total number of captures in LAr
    if LArCapture[i] != 0: # and ElCap[i] == 0
        LArCaptureTot.append(i)
        
for i in Elastic: #Counts total number of scatters in LAr
    if i != 0:
        ElasticTot.append(i)
        
LArNCapandCompt = 0 

for i in TotalCompt: #Counts the number of capture events in LAr which lead to a Compt in the LAr
    index = i[1]
    if ElCapLocation[index] == 1: # and ElCap[index] == 0
        LArNCapandCompt += 1
        
LArScatterandCompt = 0
LArScatterandComptEventNo = []

for i in TotalCompt:
    index = i[1]
    if ElCap[index] > 0 and ElCapLocation[index] > 1:
        LArScatterandCompt += 1
        LArScatterandComptEventNo.append(index)
        
print(LArScatterandComptEventNo)
print(CapVolume)
print(len(Elastic))
print("# of captures after a scatter in LAr", ElCapTot)
print("# of LAr captures which lead to compton scattering in LAr is", LArNCapandCompt)
print("# of compton scatterers is", len(TotalCompt))
print("# of scatters in LAr, to captures not in LAr, to compton scattering in LAr", LArScatterandCompt)
print("# of captures is", len(LArCaptureTot))
print("# of scatterers is", len(ElasticTot))
print("# of scatterers is", sum(ElasticTot))

