# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:33:35 2023

@author: User
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd

df = pd.read_csv('10e-4eVLocal.csv')

Hit = df['HasHit'].tolist()
Pos = df['Pos'].tolist()

mfp = sum(Pos) / len(Pos) * 0.1
stdev = np.std(Pos)*0.1
mfp_error = stdev*(1/(100000**0.5))

print(mfp_error)

print("The mean free path is:", round(mfp,6), "cm")

noc = 0

for i in range(len(Hit)):
    if (Hit[i] == 1):
        noc = noc + 1
        
print("The number of captures is:", noc, "which gives a ratio of:", round(noc/100000, 6))

nd_HDPE = 4.1216e+22
nd_HDPENCrystal = 3.9499e+22
nd = nd_HDPE
sigma_error = (1/(nd*(mfp**2)))*mfp_error*(1e24)

print(sigma_error)

print("The total cross section is:", 1/(mfp*nd), "cm^2, or, in barns it is:", (1/(mfp*nd))*1e+24, "b")
print("The capture cross section is:", (noc/100000)*(1/(mfp*nd)), "cm^2, or, in barns it is:", (noc/100000)*(1/(mfp*nd))*1e+24, "b")