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

x = [0.00001, 0.0001, 0.001, 0.01, 0.1]
y = [1546, 590, 380, 406, 401]
y_err = []
for i in range(len(y)):
    y_err.append(np.sqrt(y[i]))

fig1, ax1 = plt.subplots()
ax1.plot(x,y,'bo', label='Geant4 Data')
ax1.errorbar(x,y,y_err,ecolor='r', ls='none')
plt.xlabel('Incident Neutron Energy (eV)')
plt.ylabel('Number of Neutron Captures')
plt.axhline(y = 397, color = 'black', linestyle = '-')
ax1.set_xscale('log')
#ax1.legend(loc="upper right")