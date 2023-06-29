# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:33:35 2023

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd

df = pd.read_csv('NoWall.csv')
df1 = pd.read_csv('1Wall.csv')
df2 = pd.read_csv('2Wall.csv')
df3 = pd.read_csv('3Wall.csv')
df4 = pd.read_csv('4Wall.csv')
df5 = pd.read_csv('5Wall.csv')
df6 = pd.read_csv('6Wall.csv')
df7 = pd.read_csv('7Wall.csv')
df8 = pd.read_csv('8Wall.csv')

ek = 0.1

KE0 = df[df['KE']>=ek]['KE'].tolist()
KE1 = df1[df1['KE']>=ek]['KE'].tolist()
KE2 = df2[df2['KE']>=ek]['KE'].tolist()
KE3 = df3[df3['KE']>=ek]['KE'].tolist()
KE4 = df4[df4['KE']>=ek]['KE'].tolist()
KE5 = df5[df5['KE']>=ek]['KE'].tolist()
KE6 = df6[df6['KE']>=ek]['KE'].tolist()
KE7 = df7[df7['KE']>=ek]['KE'].tolist()
KE8 = df8[df8['KE']>=ek]['KE'].tolist()

norm = len(df['KE'].tolist())
print(norm)

x = [0,2.54,5.08,7.62,10.16,12.7,15.24,17.78,20.32]
xe = [0,2.54,5.08,7.62,10.16,15.24,17.78,20.32]
yt = [1,0.7669,0.5733,0.3892,0.2690,0.1924,0.1377,0.0908,0.0686]
ye = [1,0.62,0.472,0.326,0.267,0.136,0.126,0.11]
ye_err = [0,0.111,0.076,0.046,0.044,0.019,0.018,0.0016]

yt1 = []

yt1.append(1)
yt1.append(len(KE1)/norm)
yt1.append(len(KE2)/norm)
yt1.append(len(KE3)/norm)
yt1.append(len(KE4)/norm)
yt1.append(len(KE5)/norm)
yt1.append(len(KE6)/norm)
yt1.append(len(KE7)/norm)
yt1.append(len(KE8)/norm)

print(yt1)

#plt.plot(x,yt1,'bo', label='Geant4 Data')
#plt.plot(xe,ye,'ro')
#plt.errorbar(xe,ye,ye_err,ecolor='r',ls='none', label='Experimental Data')
#plt.xlabel('Wall Thickness (cm)')
#plt.ylabel('Transmission Probability')
#plt.legend(loc="upper right")

bins = np.linspace(0,10,50)

data = plt.hist(KE0, bins, alpha=0.5, label='No Wall', histtype = "step")
data1 = plt.hist(KE1, bins, alpha=0.5, label='1 Wall', histtype = "step")
data2 = plt.hist(KE2, bins, alpha=0.5, label='2 Wall', histtype = "step")
data3 = plt.hist(KE3, bins, alpha=0.5, label='3 Wall', histtype = "step")
data4 = plt.hist(KE4, bins, alpha=0.5, label='4 Wall', histtype = "step")
data5 = plt.hist(KE5, bins, alpha=0.5, label='5 Wall', histtype = "step")
data6 = plt.hist(KE6, bins, alpha=0.5, label='6 Wall', histtype = "step")
data7 = plt.hist(KE7, bins, alpha=0.5, label='7 Wall', histtype = "step")
data8 = plt.hist(KE8, bins, alpha=0.5, label='8 Wall', histtype = "step")

plt.legend(loc='upper right')
plt.xticks(np.arange(0, 10.5, 0.5))
plt.tick_params(axis='x', labelrotation=60)
plt.xlabel('Incident Neutron Energy on Detector (MeV)')
plt.ylabel('Number of Events')
plt.show()
