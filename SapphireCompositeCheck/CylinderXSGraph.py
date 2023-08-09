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
ytotAl = [27.79443822496165, 8.951183077767258, 3.2852875674597795, 1.8727303807049032, 1.5586631009455798, 1.467241534882788]
ycapAl = [11.87989878611311, 3.772565619955789, 1.1931835916257172, 0.37419025736864664, 0.1215445486117363, 0.03722391773997633]
ycapAl = [2*i for i in ycapAl]
print(ycapAl)
ytotSap = [222.00680044156, 70.88565178834742, 26.248419248743783, 16.25780317930439, 14.82034180033668, 14.59632673661564,]
ycapSap = [23.921232747578088, 7.471347698491817, 2.372857100086438, 0.7748468995256471, 0.24661048755760231, 0.08086365012085064]



fig1, ax1 = plt.subplots()
ax1.plot(x, ycapSap, 'bo', label = "Sapphire")
ax1.plot(x, ycapAl, 'ro', label = "(Al)*2+(O)*3")
#ax1.plot(x, ytotSap, 'go')
plt.xlabel('Incident Neutron Energy (eV)')
plt.ylabel('Cross Section (b)')
plt.title('Geant4 Capture Cross Section for Sapphire and (Al)*2+(O)*3')
plt.legend(loc="upper right")
ax1.set_xscale('log')
ax1.set_yscale('log')
#ax1.legend(loc="upper right")