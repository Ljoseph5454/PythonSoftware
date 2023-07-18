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

x = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
ytots = [2353.591, 750.093, 240.667, 78.929, 26.226, 33.258]
ycaps = [2321.699, 736.734, 231.893, 70.633, 17.976, 26.578]
ytote = [2463.4, 781.69, 252.88, 85.158, 30.090, 36.972]
ycape = [2411.1, 761.70, 239.70, 72.564, 17.750, 26.143]



fig1, ax1 = plt.subplots()
ax1.plot(x, ytots, 'bo', label = "Geant4 Data")
ax1.plot(x, ytote, 'ro', label = "ENDF Data")
plt.xlabel('Incident Neutron Energy (eV)')
plt.ylabel('Cross Section (b)')
plt.title('Pa-233 (n, gamma)')
plt.legend(loc="upper right")
ax1.set_xscale('log')
ax1.set_yscale('log')
#ax1.legend(loc="upper right")