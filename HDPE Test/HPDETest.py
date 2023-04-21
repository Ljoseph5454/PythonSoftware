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

x = [0,2.54,5.08,7.62,10.16,12.7,15.24,17.78,20.32]
xe = [0,2.54,5.08,7.62,10.16,15.24,17.78,20.32]
yt = [1,0.89608,0.73165,0.56339,0.41355,0.29619,0.20281,0.14056,0.09567]
ye = [1,0.62,0.472,0.326,0.267,0.136,0.126,0.11]
ye_err = [0,0.111,0.076,0.046,0.044,0.019,0.018,0.0016]

plt.plot(x,yt,'bo', label='Geant4 Data')
plt.plot(xe,ye,'ro')
plt.errorbar(xe,ye,ye_err,ecolor='r',ls='none', label='Experimental Data')
plt.xlabel('Wall Thickness (cm)')
plt.ylabel('Transmission Probability')
plt.legend(loc="upper right")