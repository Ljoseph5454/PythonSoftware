import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
import uproot
import math
#from matplotlib.ticker import (LogLocator, MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

filename = "Sap5cmx7.5cm3cmPad10cm25cmAmLi.root"
file = uproot.open(filename)["tree"]
print(file.keys())
df = file.arrays(["Hit", "x"], library="pd")

Capture = df['Hit'].tolist()
Elastic = df['x'].tolist()

NCaptureTot = []
ElasticTot = []

Hit1 = [1,0,0,1]

for i in Capture:
    if i != 0:
        NCaptureTot.append(i)
        
for i in Elastic:
    if i != 0:
        ElasticTot.append(i)
        

print("# of captures is", len(NCaptureTot))
print("# of scatterers is", len(ElasticTot))
print("# of captures is", sum(ElasticTot))