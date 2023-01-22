import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd

df = pd.read_csv('Pos1.csv')
print(df.head())

side = 375.4

hitx = df[df['z']==side]['x'].tolist()
hity = df[df['z']==side]['y'].tolist()
hitz = df[df['z']==side]['z'].tolist()

#print(hitx)
fig, ax = plt.subplots()
counts, xedges, yedges, im = plt.hist2d(hitx, hity, bins=(30, 30), cmap=plt.cm.jet)
fig.colorbar(im, ax=ax)
plt.show()