import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
pd.options.display.max_seq_items = None
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

df = pd.read_csv('28_58_Nickel_NC.txt', sep="  ", skiprows=5, header=None)
#df = pd.read_csv('ee.csv')
df.rename( columns={0 :'x'}, inplace=True )
df.rename( columns={1 :'y'}, inplace=True )
df.rename( columns={2 :'x1'}, inplace=True )
df.rename( columns={3 :'y1'}, inplace=True )
df.rename( columns={4 :'x2'}, inplace=True )
df.rename( columns={5 :'y2'}, inplace=True )

a = df['x'].append(df['x1'], ignore_index=True).append(df['x2'], ignore_index=True)
#a = sorted(a)
b = df['y'].append(df['y1'], ignore_index=True).append(df['y2'], ignore_index=True)
d2 = pd.concat([a,b], axis = 1)

print(d2.head())
#with pd.option_context('display.max_rows', 5, 'display.max_columns', None):display(d2)

fig,ax = plt.subplots()
ax.scatter(a,b,s=0.1)
plt.xlabel('Incident Energy (eV)')
plt.ylabel('Cross Section (b)')
plt.title('28-Ni-58 (n,gamma)')
ax.set_axisbelow(True)
plt.grid(linestyle='--')
ax.set_xscale('log')
ax.set_yscale('log')
#logfmt = plt.ticker.LogFormatterExponent(base=10.0, labelOnlyBase=True)
#ax.xaxis.set_major_formatter(logfmt)
#ax.yaxis.set_major_formatter(logfmt)


#hitx = df[df['z']==side]['x'].tolist()
#hity = df[df['z']==side]['y'].tolist()
#hitz = df[df['z']==side]['z'].tolist()

#print(hitx)
#fig, ax = plt.subplots()
#counts, xedges, yedges, im = plt.hist2d(hitx, hity, bins=(30, 30), cmap=plt.cm.jet)
#fig.colorbar(im, ax=ax)
#plt.show()