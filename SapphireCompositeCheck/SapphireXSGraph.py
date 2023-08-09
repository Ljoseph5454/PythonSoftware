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
ytotSap = [222.00680044156, 70.88565178834742, 26.248419248743783, 16.25780317930439, 14.82034180033668, 14.59632673661564,]
ycapSap = [23.921232747578088, 7.471347698491817, 2.372857100086438, 0.7748468995256471, 0.24661048755760231, 0.08086365012085064]
yelSap = [ytotSap[i]-ycapSap[i] for i in range(len(ytotSap))]
ycapExperiment = [23.58996370701591, 7.3359200079233915, 2.368893281157442, 0.7459801523487937, 0.23491419336717967, 0.07460624286177781]
ytotExperiment = [217.86218741746393, 70.35140397306299, 25.757821694683983, 16.184187791840614, 14.63708473743574, 14.273992181725847]
print(yelSap)
s = 6

fig1, ax1 = plt.subplots()
ax1.plot(x, ycapSap, 'o', markerfacecolor='none', ms=s, markeredgecolor='g', label = "Capture")
ax1.plot(x, yelSap, 'o', markerfacecolor='none', ms=s, markeredgecolor='r', label = "Elastic")
ax1.plot(x, ytotSap, 'o', markerfacecolor='none', ms=s, markeredgecolor='b', label = "Total")
ax1.plot(x, ycapExperiment, **{'color': 'lightsteelblue', 'marker': '.'}, label = "Capture Experiment")
ax1.plot(x, ytotExperiment, **{'color': 'darkorchid', 'marker': '.'}, label = "Total Experiment")
plt.xlabel('Incident Neutron Energy (eV)')
plt.ylabel('Cross Section (b)')
plt.title('Geant4 Sapphire Neutron Cross Section')
plt.legend(loc="upper right", fontsize = 8)
ax1.set_xscale('log')
ax1.set_yscale('log')
plt.rcParams['figure.dpi'] = 300
#ax1.legend(loc="upper right")