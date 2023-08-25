import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)

df = pd.read_csv('sapphire.csv')
#df = pd.read_csv('Informacion.csv')
df = df.fillna(0)
print(df.head())
#df['Tnsmi'].plot(kind='hist');

h=6.626*10**(-34)
nmass=1.676*10**(-27)

ek = df['Hit'].tolist()
tr = df['KE_i'].tolist()
ps = df[df['KE_i']==1]['Hit'].tolist()
print(ps[slice(100)])

print(max(ek))
print(np.array(ek).argmax())

wl = df['Hit'].apply(lambda x: (h/(np.sqrt(2*nmass*(x*1.60218*10**(-19)))))*10**(9)).tolist()
wps = df[df['KE_i']==1]['Hit'].apply(lambda x: (h/(np.sqrt(2*nmass*(x*1.60218*10**(-19)))))*10**(9)).tolist()

print(wl[0:5])
print(wps[0:5])
print((h/(np.sqrt(2*nmass*(100*1.60218*10**(-19)))))*10**(9))
#print("ps",ps[:5])
#print(ek[0:5])
#print(tr[0:5])

print(min(wl))

bins = 50
minwl = 0.028
#0.0028 (100eV max)
#0.028 (1eV max)
n = plt.hist(ek, bins,(0.001,1))
nw = plt.hist(wl, bins, (minwl,0.904))
m = plt.hist(ps, bins,(0.001,1))
mw = plt.hist(wps, bins, (minwl,0.904))
#print(np.isfinite(n).all())
print(nw)
print(mw)
#print(m[0])
#print(len(ek),len(wl))
#print(min(nw[1]),max(nw[1]))
#print(min(mw[1]),max(mw[1]))

prob = []
probw = []

plt.clf()

for i in range (len(n[0])):
     a = m[0][i]
     b = n[0][i]
     prob.append(np.divide(a,b))
     
for i in range (len(nw[0])):
     a = mw[0][i]
     b = nw[0][i]
     probw.append(np.divide(a,b))
     
#print(w)
#print(n[1])
#print(prob)
fig1, ax1 = plt.subplots()
ax1.set_ylim([0,1])
ax1.plot(nw[1][1:],probw)
ax1.set_xlabel("Wavelength (nm)");
ax1.set_ylabel("Transmission Probability")
ax1.set_title("Neutron Transmission through Sapphire Block")
#ax1.set_xscale('log')



plt.show()
