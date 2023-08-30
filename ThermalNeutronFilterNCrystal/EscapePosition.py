import matplotlib.pyplot as plt
import matplotlib.colors 
from matplotlib import ticker
import numpy as np
import os, pickle
import sys
import pandas as pd
from matplotlib.patches import Rectangle

df = pd.read_csv('Sap5cmx10cm10cmAmLiPos.csv')
print(df.head())

side = 215

Tot = df['Event'].tolist()
KE = df[df['z']==side]['KE_e'].tolist()
hitx = df[df['z']==side]['x'].tolist()
hity = df[df['z']==side]['y'].tolist()
hitz = df[df['z']==side]['z'].tolist()
KE = [i*1000000 for i in KE]
print(len(Tot))
print(len(hitx))
#print(hitx)


fig1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
counts, xedges, yedges, im = ax1.hist2d(hitx, hity, bins=(35, 35), cmap=plt.cm.inferno)
cb1= fig1.colorbar(im, ax=ax1)
ax1.add_patch(Rectangle((-25, -25), 50, 50, facecolor="none", ec='blue', lw=2))
ax2.set_facecolor('gray')
sc = ax2.scatter(hitx, hity, s=6, c=KE, cmap=plt.cm.inferno, norm=matplotlib.colors.LogNorm())
ax2.add_patch(Rectangle((-25, -25), 50, 50, facecolor="none", ec='blue', lw=2))
cb2 = fig1.colorbar(sc, ax=ax2)
cb2.set_ticks([1e-2,1e-1,1,10,100,1000,10000,100000,1000000])
ax1.set_xlabel('x-pos (mm)')
ax1.set_ylabel('y-pos (mm)')
ax1.set_title('# of Neutrons Escaping')
ax2.set_xlabel('x-pos (mm)')
ax2.set_ylabel('y-pos (mm)')
ax2.set_title('Energy of Neutrons Escaping (eV)')
plt.show()
