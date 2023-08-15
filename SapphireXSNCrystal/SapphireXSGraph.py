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

x = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000]
xcap = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10]
xinel = [1000000]
ytotSapNC = [32.645789270429646, 10.348940933279293, 3.350676045804857, 1.2532162397389233, 2.9713567224862953, 11.777070314976335, 14.499960859744226, 14.52370621284483, 14.368332069342589, 13.666752213402514, 21.904298105103948, 29.023045542936977]
ycapSapNCtemp = [23.73283588381694, 7.531855721831337, 2.401630562591089, 0.7581707607172536, 0.23515317101756542, 0.07443108439065044, 0.018559949900472612, 0.009876120224734485, 0.002586299772481666, 0.0008200051328041508, 0.0010952149052551974, 0.0020322092230271546]
ycapSapNC = [23.73283588381694, 7.531855721831337, 2.401630562591089, 0.7581707607172536, 0.23515317101756542, 0.07443108439065044, 0.018559949900472612]
yinelSapNC = [0.09548581983626266]
yelSapNC = [ytotSapNC[i]-ycapSapNCtemp[i] for i in range(len(ytotSapNC))]
#yelSapNC = [yelSapNC[i+9]-yinelSapNC[i] for i in range(len(yinelSapNC))]
for i in range(len(yinelSapNC)):
    yelSapNC[i+11] = yelSapNC[i+11] - yinelSapNC[i]
print(yelSapNC[11])
ytotSap = [222.00680044156, 70.88565178834742, 26.248419248743783, 16.25780317930439, 14.82034180033668, 14.59632673661564, 14.410933960734637, 14.480001542050964, 14.336585912646337, 13.689371995315119, 22.005663336985943, 29.240909668250417]
ycapSaptemp = [23.921232747578088, 7.471347698491817, 2.372857100086438, 0.7748468995256471, 0.24661048755760231, 0.08086365012085064, 0.022481056978746035, 0.007819200832707521, 0.0022938537460234143, 0.0002737874399063024, 0.002420622967068454, 0.001754454580095025]
ycapSap = [23.921232747578088, 7.471347698491817, 2.372857100086438, 0.7748468995256471, 0.24661048755760231, 0.08086365012085064, 0.022481056978746035]
yinelSap = [0.09649500190522638]
yelSap = [ytotSap[i]-ycapSaptemp[i] for i in range(len(ytotSap))]
for i in range(len(yinelSap)):
    yelSap[i+11] = yelSap[i+11] - yinelSap[i]
print(yelSap[11])
xe = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
ycapExperiment = [23.58996370701591, 7.3359200079233915, 2.368893281157442, 0.7459801523487937, 0.23491419336717967, 0.07460624286177781]
ytotExperimentFA = [217.86218741746393, 70.35140397306299, 25.757821694683983, 16.184187791840614, 14.63708473743574, 14.273992181725847]
ytotExperiment = [31.822331080336927, 10.126612414452415, 3.222527223255722, 1.1926213903772718, 2.80599826823172, 11.777089876601366]
s = 6


fig1, ax1 = plt.subplots()
#ax1.plot(x, yelSap, 'o', markerfacecolor='none', ms=s, markeredgecolor='r', label = "Elastic")
ax1.plot(x, ytotSapNC, 'o', markerfacecolor='none', ms=s, markeredgecolor='b', label = "Total (NCrystal, Bragg=0)")
ax1.plot(xcap, ycapSapNC, 'o', markerfacecolor='none', ms=s, markeredgecolor='mediumorchid', label = "Capture (NCrystal)")
ax1.plot(xinel, yinelSapNC, 'o', markerfacecolor='none', ms=s, markeredgecolor='black', label = "Inelastic (NCrystal)")
#ax1.plot(x, yelSap, 'o', markerfacecolor='none', ms=s, markeredgecolor='r', label = "Elastic")
ax1.plot(x, ytotSap, '^', markerfacecolor='none', ms=s, markeredgecolor='r', label = "Total (Geant4)")
ax1.plot(xcap, ycapSap, '^', markerfacecolor='none', ms=s, markeredgecolor='orange', label = "Capture (Geant4)")
ax1.plot(xinel, yinelSap, '^', markerfacecolor='none', ms=s, markeredgecolor='silver', label = "Inelastic (Geant4)")
ax1.plot(xe, ycapExperiment, **{'color': 'lightsteelblue', 'marker': '.'}, label = "Capture Data")
ax1.plot(xe, ytotExperimentFA, **{'color': 'lawngreen', 'marker': '.'}, label = "Total (Free Atom) Data")
ax1.plot(xe, ytotExperiment, **{'color': 'khaki', 'marker': '.'}, label = "Total Data")
plt.xlabel('Incident Neutron Energy (eV)')
plt.ylabel('Cross Section (b)')
plt.title('Geant4 Sapphire Neutron Cross Section')
plt.legend(loc="lower left", fontsize = 8)
ax1.set_xscale('log')
ax1.set_yscale('log')
#ax1.legend(loc="upper right")