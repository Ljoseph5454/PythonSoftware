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

threshold = 300

file = uproot.open(filename)["tree"] #From NCaptureCount
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

#-------------------------------------------------------------------------------------------

filename1 = "Data1.root" #EdepSap5cmx7.5cm3cmPad10cm25cmAmLi
file1 = uproot.open(filename1)["tree1"] #From SBCEdepTest
print(file1.keys())
df1 = file1.arrays(["EDep", "EventNo"], library="pd")

EDep = df1['EDep'].tolist()
EDep = [i*10**6 for i in EDep]
#print(EDep)
EventNo = df1['EventNo'].tolist()
EventNo = [int(i) for i in EventNo]

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

TotalCompt = [] # Creates a 2D array with eventNo and # of Compt events in the LAr

for i in range(0, len(ComptCount)):
    if ComptCount[i] > 0:
        TotalCompt.append([ComptCount[i],i])
        
print(len(TotalCompt))

#-------------------------------------------------------------------------------------------

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
indexlisttemp = []
HasScattered = False
for i in TotalCompt: #Counts the number of capture events in LAr which lead to a Compt in the LAr
    index = i[1]
    #indexlisttemp.append(index)
    for j in OverThresholdScatters: # Want to subtract capture events with one or more >1keV scatter and capture
        if j[0] == index:
            HasScattered = True   
    if HasScattered == False:
        if ElCapLocation[index] == 1: # and ElCap[index] == 0
            LArNCapandCompt += 1
    HasScattered = False
        
indexlisttemp1 = []
for j in OverThresholdScatters:
    indexlisttemp1.append(j[0])
        
LArScatterandCompt = 0
LArScatterandComptEventNo = []

for i in TotalCompt: # Counts scatter in LAr to caps not in LAr to compt. in LAr (and event number)
    index = i[1]
    if ElCap[index] > 0 and ElCapLocation[index] > 1: 
        LArScatterandCompt += 1
        LArScatterandComptEventNo.append(index)
        
#print(LArScatterandComptEventNo)
print(CapVolume)
print(len(Elastic))
print("# of captures after a scatter in LAr", ElCapTot)
print("# of LAr captures which lead to compton scattering in LAr is", LArNCapandCompt)
print("# of compton scatterers is", len(TotalCompt))
print("# of scatters in LAr, to captures not in LAr, to compton scattering in LAr", LArScatterandCompt)
print("# of captures is", len(LArCaptureTot))
print("# of scatterers is", len(ElasticTot))
print("# of scatterers is", sum(ElasticTot))
print("# of scatterers over the", threshold/1000, "keV threshold is", len(OverThresholdScatters))
print("# of events with only one >", threshold/1000, "keV scatter is", len(OverThresholdSingleScatters))

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
print("# of single scatters >", threshold/1000, "keV which capture elewhere and produce a compt in LAr is", len(intersection(LArScatterandComptEventNo, OverThresholdSingleScatters)))

#print(OverThresholdScatters)
#print(indexlisttemp)
#print(len(indexlisttemp))
#print(len(TotalCompt))
#for i in indexlisttemp:
#    if i == True:
#        print('1')

# of captures after a scatter in LAr 434
# of LAr captures which lead to compton scattering in LAr is 193
# of compton scatterers is 7277
# of scatters in LAr, to captures not in LAr, to compton scattering in LAr 118
# of captures is 204
# of scatterers is 520
# of scatterers is 940.0
# of scatterers over the 1keV threshold is 172
# of events with only one 1keV scatter is 54




