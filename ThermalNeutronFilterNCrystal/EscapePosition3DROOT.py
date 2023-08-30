import matplotlib.pyplot as plt
import matplotlib.colors 
from matplotlib import ticker
import numpy as np
import os, pickle
import sys
import pandas as pd
from matplotlib.patches import Rectangle, PathPatch
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d
import uproot

df = pd.read_csv('Sap5cmx10cm10cmAmLiPos.csv')
print(df.head())

side = 215

S_l = 10*10
S_w = 5*10
V_l = 3*10
P_w = 50*10
P_l = 10*10
P_p = (S_l+P_l)+0*10
center = 0
center1 = 0.5*(P_p-P_w) #use to shift the center (Geant4 center is shifted for macro use)
xylength = P_w
zlengthface = 0.5*(P_w+V_l+P_p)+center
zlengthback = -0.5*(P_w+V_l+P_p)+center
print(zlengthback)

Tot = df['Event'].tolist()
KE = df['KE_e'].tolist()
hitx = df['x'].tolist()
hity = df['y'].tolist()
hitz = df['z'].tolist()
KE = [i*1000000 for i in KE]
hitz = [i-center1 for i in hitz]
print(len(Tot))
print(len(hitx))
#print(hitx)

fig1 = plt.figure(figsize=(10, 10))
ax2 = fig1.add_subplot(projection='3d')
#ax2.set_facecolor('gray')
sc = ax2.scatter(hitx, hity, hitz, s=6, c=KE, cmap=plt.cm.inferno, norm=matplotlib.colors.LogNorm())
rectangleface= Rectangle((-P_w, -P_w), 2*P_w, 2*P_w, facecolor="none", ec='black', lw=1)
rectangletop = Rectangle((-P_w, center-0.5*(P_w+V_l+P_p)), 2*P_w, (P_w+V_l+P_p), facecolor="none", ec='green', lw=2)
#rectangletop = Rectangle((-P_w, 50), 100, 2*P_w, facecolor="none", ec='blue', lw=2)
rectanglebottom = Rectangle((-P_w, center-0.5*(P_w+V_l+P_p)), 2*P_w, (P_w+V_l+P_p), facecolor="none", ec='blue', lw=2)
rectangleback = Rectangle((-P_w, -P_w), 2*P_w, 2*P_w, facecolor="none", ec='blue', lw=2)
rectangleleft = Rectangle((-P_w, center-0.5*(P_w+V_l+P_p)), 2*P_w, (P_w+V_l+P_p), facecolor="none", ec='blue', lw=2)
rectangleright = Rectangle((-P_w, center-0.5*(P_w+V_l+P_p)), 2*P_w, (P_w+V_l+P_p), facecolor="none", ec='blue', lw=2)
rectanglelist = [rectangleface, rectangletop, rectanglebottom, rectangleback, rectangleleft, rectangleright]
for (i, j, k) in zip(rectanglelist, ("z", "y", "y", "z", "x", "x"), (zlengthface, xylength, -xylength, zlengthback, xylength, -xylength)):
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
plt.show()
