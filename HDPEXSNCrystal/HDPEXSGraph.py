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
ytotHDPENC = [735.3052816123421, 346.8547241996009, 224.17732134812957, 150.0080364844656, 72.86804395403887, 47.786791235532675]
ycapHDPENC = [34.17698948934166, 10.63803439120176, 3.3940446452106823, 1.1025590681608222, 0.3308209195513364, 0.11277682731585711]
yelHDPENC = [ytotHDPENC[i]-ycapHDPENC[i] for i in range(len(ytotHDPENC))]
ytotHDPE = [2416.756674933928, 767.9990092358609, 245.92002075932845, 89.02793423524363, 51.206287015017004, 46.373457222529474]
ycapHDPE = [33.4720799478349, 10.544626396808368, 3.351889882949647, 1.0629935347688089, 0.3466665630916651, 0.10619521703959248]
yelHDPE = [ytotHDPE[i]-ycapHDPE[i] for i in range(len(ytotHDPE))]
#ytotHDPEL = [2412.621066048362, 767.7877471595186]
#ycapHDPEL = [32.618636812973854, 10.157831894920431]
#yelHDPEL = [ytotHDPEL[i]-ycapHDPEL[i] for i in range(len(ytotHDPEL))]
xe = [0.001, 0.01, 0.1, 1]
#ytotExperimentFA = [219.272766012402, 144.50911705837137, 71.78183424264171, 47.92729435692446]
ytotExperiment = [219.272766012402, 144.50911705837137, 71.78183424264171, 47.92729435692446]
#ycapExperiment = [23.58996370701591, 7.3359200079233915, 2.368893281157442, 0.7459801523487937, 0.23491419336717967, 0.07460624286177781]
print(yelHDPE)
s = 6

fig1, ax1 = plt.subplots()
ax1.plot(x, ycapHDPENC, 'o', markerfacecolor='none', ms=s, markeredgecolor='mediumorchid', label = "Capture (NCrystal)")
#ax1.plot(x, yelHDPE, 'o', markerfacecolor='none', ms=s, markeredgecolor='r', label = "Elastic")
ax1.plot(x, ytotHDPENC, 'o', markerfacecolor='none', ms=s, markeredgecolor='b', label = "Total (NCrystal)")
ax1.plot(x, ycapHDPE, '^', markerfacecolor='none', ms=s, markeredgecolor='orange', label = "Capture (Geant4)")
#ax1.plot(x, yelHDPE, 'o', markerfacecolor='none', ms=s, markeredgecolor='r', label = "Elastic")
ax1.plot(x, ytotHDPE, '^', markerfacecolor='none', ms=s, markeredgecolor='r', label = "Total (Geant4)")
#ax1.plot(xe, ycapExperiment, **{'color': 'lightsteelblue', 'marker': '.'}, label = "Capture Experiment")
#ax1.plot(xe, ytotExperimentFA, **{'color': 'lawngreen', 'marker': '.'}, label = "Total (Free Atom) Experiment")
ax1.plot(xe, ytotExperiment, **{'color': 'limegreen', 'marker': '.'}, label = "Total Experiment")
plt.xlabel('Incident Neutron Energy (eV)')
plt.ylabel('Cross Section (b)')
plt.title('Geant4 HDPE Neutron Cross Section')
plt.legend(loc="upper right", fontsize = 8)
ax1.set_xscale('log')
ax1.set_yscale('log')
#ax1.legend(loc="upper right")