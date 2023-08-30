import matplotlib.pyplot as plt
import matplotlib.colors 
from matplotlib import colors
from matplotlib import ticker
import numpy as np
import os, pickle
import sys
import pandas as pd
from matplotlib.patches import Rectangle, PathPatch
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d
import uproot

filename = "Sap5cmx7.5cm10cmPad10cmAmLi.root"
file = uproot.open(filename)["tree"]
df = file.arrays(["Hit", "x", "y", "z", "KEinitial", "KEescape"], library="pd")
print(df.head())

S_l = 7.5*10
S_w = 5*10
V_l = 3*10
P_w = 50*10
P_l = 10*10
P_p = (S_l+P_l)+10*10
center = 0
center1 = 0.5*(P_p-P_w) #use to shift the center (Geant4 center is shifted for macro use)
print(center1)
xylength = P_w
zlengthface = 0.5*(P_w+V_l+P_p)+center
zlengthback = -0.5*(P_w+V_l+P_p)+center

side = 215

KEescapetemp = df['KEescape'].tolist()
Hittemp = df['Hit'].tolist()
#Hittemp1 = df[df['Hit']==1]['Hit'].tolist()
hitxtemp = df['x'].tolist()
hitytemp = df['y'].tolist()
hitztemp = df['z'].tolist()
KEescapetemp = [i*1000000 for i in KEescapetemp]

KEescape = []
hitx = []
hity = []
hitz = []
for i in range(len(Hittemp)):
    if Hittemp[i] == 1:
        KEescape.append(KEescapetemp[i])
        hitx.append(hitxtemp[i])
        hity.append(hitytemp[i])
        hitz.append(hitztemp[i])

hitz = [i-center1 for i in hitz] #Shifting z values for better alignment
print(max(hitz))

fig1, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
counts, xedges, yedges, im = ax1.hist2d(hitx, hity, bins=(35, 35), cmap=plt.cm.inferno)
cb1= fig1.colorbar(im, ax=ax1)
ax1.add_patch(Rectangle((-25, -25), 50, 50, facecolor="none", ec='blue', lw=2))
ax2.set_facecolor('gray')
sc = ax2.scatter(hitx, hity, s=6, c=KEescape, cmap=plt.cm.inferno, norm=matplotlib.colors.LogNorm())
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

#fig1 = plt.figure(figsize=(12, 12))
#ax2 = fig1.add_subplot(projection='3d')
#sc = ax2.scatter(hitx, hity, hitz, s=6, c=KEescape, cmap=plt.cm.inferno, norm=matplotlib.colors.LogNorm())
#cb2 = fig1.colorbar(sc, ax=ax2)
#cb2.set_ticks([1e-2,1e-1,1,10,100,1000,10000,100000,1000000])
#ax2.set_xlabel('x-pos (mm)')
#ax2.set_ylabel('y-pos (mm)')
#ax2.set_title('Energy of Neutrons Escaping (eV)')
#plt.show()

fig1 = plt.figure(figsize=(10, 10))
ax2 = fig1.add_subplot(projection='3d')
#ax2.set_facecolor('gray')
sc = ax2.scatter(hitx, hity, hitz, s=6, c=KEescape, cmap=plt.cm.inferno, norm=matplotlib.colors.LogNorm())
rectangleface= Rectangle((-P_w, -P_w), 2*P_w, 2*P_w, facecolor="none", ec='black', lw=1)
rectangletop = Rectangle((-P_w, center-0.5*(P_w+V_l+P_p)), 2*P_w, (P_w+V_l+P_p), facecolor="none", ec='black', lw=2)
rectanglebottom = Rectangle((-P_w, center-0.5*(P_w+V_l+P_p)), 2*P_w, (P_w+V_l+P_p), facecolor="none", ec='black', lw=2)
rectangleback = Rectangle((-P_w, -P_w), 2*P_w, 2*P_w, facecolor="none", ec='black', lw=2)
rectangleleft = Rectangle((-P_w, center-0.5*(P_w+V_l+P_p)), 2*P_w, (P_w+V_l+P_p), facecolor="none", ec='black', lw=2)
rectangleright = Rectangle((-P_w, center-0.5*(P_w+V_l+P_p)), 2*P_w, (P_w+V_l+P_p), facecolor="none", ec='black', lw=2)
rectanglesap = Rectangle((-25, -25), 50, 50, facecolor="none", ec='dodgerblue', lw=2)
rectanglelist = [rectangleface, rectangletop, rectanglebottom, rectangleback, rectangleleft, rectangleright, rectanglesap]
for (i, j, k) in zip(rectanglelist, ("z", "y", "y", "z", "x", "x", "z"), (zlengthface, xylength, -xylength, zlengthback, xylength, -xylength, zlengthface)):
    ax2.add_patch(i)
    art3d.pathpatch_2d_to_3d(i, z=k, zdir=j)
cb2 = fig1.colorbar(sc, ax=ax2)
cb2.set_ticks([1e-2,1e-1,1,10,100,1000,10000,100000,1000000])
ax2.set_xlabel('x-pos (mm)')
ax2.set_ylabel('y-pos (mm)')
ax2.set_zlabel('z-pos (mm)')
ax2.set_title('Energy of Neutrons Escaping (eV)')
ax2.grid(False)
#plt.axis('off')
ax2.axes.set_xlim3d(left=-P_w, right=P_w) 
ax2.axes.set_ylim3d(bottom=-P_w, top=P_w) 
ax2.axes.set_zlim3d(bottom=-P_w, top=P_w) 
ax2.w_xaxis.set_pane_color(colors.to_rgba('gray'))
ax2.w_yaxis.set_pane_color(colors.to_rgba('gray'))
ax2.w_zaxis.set_pane_color(colors.to_rgba('gray'))
plt.show()
