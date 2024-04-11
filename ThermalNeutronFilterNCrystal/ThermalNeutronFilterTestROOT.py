import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
import uproot
import math
#from matplotlib.ticker import (LogLocator, MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

S_l = 10*10
S_w = 5*10
V_l = 3*10
P_w = 25*10
P_l = 10*10
Pad = 10*10
P_p = (S_l+P_l)+Pad
center = 0
center1 = 0.5*(P_p-P_w) #use to shift the center (Geant4 center is shifted for macro use)
print(center1)
xylength = P_w
zlengthface = 0.5*(P_w+V_l+P_p)+center
zlengthback = -0.5*(P_w+V_l+P_p)+center

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
filename = "Sap5cmx10cm10cmPad5cm25cm2.4MeVSource.root"
faceonly = True # Only check data points that leave the face of the filter
printdat = False # Set to true if you want text file output for histograms
file = uproot.open(filename)["tree"]
print(file.keys())
#print(file.keys())
thickness = filename[0:-5]
print(thickness)
df = file.arrays(["Hit", "x", "y", "z", "KEinitial", "KEescape", "px", "py", "pz"], library="pd")
#df = pd.read_csv(file)

KEi = df['KEinitial'].tolist()
Hit = df['Hit'].tolist()

boundary = xylength

if faceonly == True:
    KEe = df[df['z'].between(zlengthface+center1-Pad, zlengthface+center1) & df['x'].between(-boundary, boundary, inclusive='neither') & df['y'].between(-boundary, boundary, inclusive='neither')]['KEescape'].tolist()
    px = df[df['z'].between(zlengthface+center1-Pad, zlengthface+center1) & df['x'].between(-boundary, boundary, inclusive='neither') & df['y'].between(-boundary, boundary, inclusive='neither')]['px'].tolist()
    py = df[df['z'].between(zlengthface+center1-Pad, zlengthface+center1) & df['x'].between(-boundary, boundary, inclusive='neither') & df['y'].between(-boundary, boundary, inclusive='neither')]['py'].tolist()
    pz = df[df['z'].between(zlengthface+center1-Pad, zlengthface+center1) & df['x'].between(-boundary, boundary, inclusive='neither') & df['y'].between(-boundary, boundary, inclusive='neither')]['pz'].tolist()
    momdir = list(zip(px,py,pz))
    theta = [np.arccos(i[2]/np.sqrt(i[0]**2 + i[1]**2 + i[2]**2)) for i in momdir]
    phi = [np.arctan2(i[1],i[0]) for i in momdir]
else:
    KEetemp = df['KEescape'].tolist()
    
#print(phi)



print(df.head())


if faceonly == False:
    KEe = []        
    for i in range(len(KEetemp)):
        if KEetemp[i] > 0:
            KEe.append(KEetemp[i])

print(len(Hit))
print(len(KEe))
print(len(KEi))

ratio = len(KEe)/len(Hit)

bottombin = 1e-9

binnumke = 100
binnumtheta = 50
bins = np.linspace(0,10.2,52)
if faceonly == True:
    thetabins = np.linspace(0,np.pi/2+0.05,binnumtheta)
    phibins = np.linspace(-np.pi,np.pi,50)
bins1=np.logspace(np.log10(bottombin),np.log10(10), binnumke)
#print(bins1)
print(max(KEi))
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
print('So the ratio of thermal to fast is', round(my_div(len(KEthermal),len(KEfast)),3), 'and the ratio of thermal to non thermal is', round(my_div(len(KEthermal),(len(KEfast)+len(KEmedium))),3))
print('If neutrons <1keV will not produce events, then we get a good/bad neutron ratio of:', round(my_div(len(KEunderthreshold),len(KEoverthreshold)),3))

xlabels = ['$<10^{-9}$', '$10^{-8}$', '$<10^{-7}$', '$10^{-6}$', '$10^{-5}$', '$10^{-4}$', '$10^{-3}$', '$10^{-2}$', '$10^{-1}$', '$1$', '$10$']

fig1, ax1 = plt.subplots(figsize=(16,10))
#ax1.hist(KEe, bins1, histtype = "step", label = "Escape")
#ax1.xaxis.set_major_locator(LogLocator(base=10))
a = ax1.hist(np.clip(KEe, bottombin, 10), bins1, histtype = "step", label = "Escape")
ax1.hist(np.clip(KEi, bottombin, 10), bins1, histtype = "step", label = "Initial")
ax1.legend(loc="upper left", fontsize = 8)
ax1.set_xlabel('AmLi Neutron Energy (MeV)')
ax1.set_ylabel('Number of Events')
plt.axvline(x = 0.001, color = 'red', linestyle = '--', alpha = 0.5, label = "Elastic Max")
ax1.set_title('Neutron Energy Spectrum of AmLi Neutrons')
ax1.set_xscale('log')
ax1.set_yscale('log')
#ax1.set_title('Neutron Energy Spectrum of AMBE neutrons in a ' + thickness + ' HDPE box')
fig1.canvas.draw()
#start, end = ax1.get_xlim()
#print(start, end)
ax1.set_xlim(bottombin/2, 10)
ax1.xaxis.set_ticks(np.logspace(np.log10(bottombin), 1, num=1-int(np.log10(bottombin))+1))
labels = [item.get_text() for item in ax1.get_xticklabels()]
#print(labels)
#labels[2] = '$<10^{-7}$'
#ax1.set_xticklabels(labels)
#ax1.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=8))
#ax1.xaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=(0.2,0.4,0.6,0.8), numticks=5))
#ax1.xaxis.set_minor_formatter(ticker.FormatStrFormatter('%.2f'))
#plt.grid(True, which="both",ls="--")
ax1.xaxis.set_major_locator(ticker.LogLocator(numticks=999))
ax1.xaxis.set_minor_locator(ticker.LogLocator(numticks=999, subs="auto"))
ax1.legend(title='Escape Ratio = ' + str(round(ratio,3)) + '\n' + 'Good/Bad Ratio = ' + str(round(my_div(len(KEunderthreshold),len(KEoverthreshold)),3)), loc='upper left')
plt.show()

savepath = r'C:\Users\User\Documents\GitHub\PythonStuff\ThermalNeutronFilterNCrystal\TextOutputsMacro'

if printdat == True:
    gpspointke = ['/gps/hist/point' for i in range(binnumke-1)]
    gpspointtheta = ['/gps/hist/point' for i in range(binnumtheta-1)]
    #print(gpspoint)

    dfsaveke = pd.DataFrame({'gpspoint':gpspointke, 'x_upper':a[1][1:], 'y': a[0]})
    print(dfsaveke.head())
    dfsaveke.to_csv(savepath + '/' + filename[0:-5]+'ke.txt', index = False, sep=' ')
    #print('r'+filename[0:-5]+'.txt')
    #np.savetxt(filename[0:-5]+'ke.txt', dfsaveke.values) #fmt='%1.11f %d'


            
if faceonly == True:
    fig1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    b = ax1.hist(theta, thetabins, histtype = "step", label = "Theta")
    ax1.set_xlim([0, np.pi/2])
    ax1.set_xlabel('theta (rad)')
    ax2.hist(phi, phibins, histtype = "step", label = "Phi")
    ax2.set_xlim([-np.pi, np.pi])
    ax2.set_xlabel('phi (rad)')
    fig1.suptitle('Angular Distribution of Escaping Neutrons')
    if printdat == True:
        dfsavetheta = pd.DataFrame({'gpspoint':gpspointtheta, 'x_lower':[i for i in b[1][1:]], 'y': b[0]}) #Invert theta cuz Geant4 GPS is backwards
        # dfsavetheta = pd.DataFrame({'gpspoint':gpspointtheta, 'x_lower':[np.pi-i for i in b[1][1:]], 'y': b[0]}) #Invert theta cuz Geant4 GPS is backwards
        print(dfsavetheta.head())
        dfsavetheta.to_csv(savepath + '/' + filename[0:-5]+'theta.txt', index = False, sep=' ')