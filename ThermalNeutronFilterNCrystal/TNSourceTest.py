import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
import uproot
import math
#from matplotlib.ticker import (LogLocator, MultipleLocator, AutoMinorLocator)
import matplotlib.ticker as ticker

filename = "TNsourcetest3.root"
file = uproot.open(filename)["tree"]
print(file.keys())
df = file.arrays(["Hit", "KEinitial", "pxi", "pyi", "pzi", ], library="pd")

KEi = df['KEinitial'].tolist()
pxi = df['pxi'].tolist()
pyi = df['pyi'].tolist()
pzi = df['pzi'].tolist()
momdir = list(zip(pxi,pyi,pzi))
theta = [np.arccos(i[2]/np.sqrt(i[0]**2 + i[1]**2 + i[2]**2)) for i in momdir]
phi = [np.arctan2(i[1],i[0]) for i in momdir]

binnumke = 100
binnumtheta = 50
bottombin = 1e-9
thetabins = np.linspace(0,np.pi/2+0.05,50)
phibins = np.linspace(-np.pi,np.pi,binnumtheta)
bins1=np.logspace(np.log10(bottombin),np.log10(10), binnumke)

fig1, ax1 = plt.subplots(figsize=(16,10))
ax1.hist(np.clip(KEi, bottombin, 10), bins1, histtype = "step", label = "Initial")
ax1.legend(loc="upper left", fontsize = 8)
ax1.set_xlabel('AmLi Neutron Energy (MeV)')
ax1.set_ylabel('Number of Events')
ax1.set_title('Neutron Energy Spectrum of AmLi Neutrons')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.xaxis.set_major_locator(ticker.LogLocator(numticks=999))
ax1.xaxis.set_minor_locator(ticker.LogLocator(numticks=999, subs="auto"))
plt.show()

fig1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
b = ax1.hist(theta, thetabins, histtype = "step", label = "Theta")
ax1.set_xlim([0, np.pi/2])
ax1.set_xlabel('theta (rad)')
ax2.hist(phi, phibins, histtype = "step", label = "Phi")
ax2.set_xlim([-np.pi, np.pi])
ax2.set_xlabel('phi (rad)')
fig1.suptitle('Angular Distribution of Escaping Neutrons')
plt.show()
