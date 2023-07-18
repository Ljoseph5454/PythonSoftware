import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
pd.options.display.max_seq_items = None
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

file_name = 'EXYZ.txt'
file_name_edit = file_name[0:-4] + '_edit.txt'
skip = 0
Data = 0
avo = 6.0221408e+23
amu = 0 
KE = 0
IonData = ''
file_lines = []

with open(file_name, 'r') as file: # Searches for the row in which data starts and
    done = 0                       # looks for ion data in the file (we want the atomic mass)
    for num, line in enumerate(file, 1):
        if '0000001' in line and done == 0:
            #print('found at line:', num)
            skip = num - 1
            done = 1
        if 'Ion Data' in line:
            Data = num
            
            
with open(file_name, 'r') as file:  # Adds a space after first column to allow
    n = 0                           # pandas to use double-space as separator    
    for line in file:
        if n >= skip:
            file_lines.append(''.join([line.strip()[:7], ' ', line.strip()[7:], '\n'])) 
        else:
            #file_lines.append(''.join([line.strip(), '\n']))
            file_lines.append(''.join([line]))
        n += 1
        
with open(file_name, 'r') as file: # Adds the ion data string to a variable
    n = 0
    for line in file:
        if n == Data:
            IonData = line.rstrip()
            IonData = (' '.join(IonData.split())).split()
        n += 1

amu = float(IonData[1]) # Set the atomic mass variable
mass = amu/avo * 0.001 # calculate mass of 1 atom in kg
print(mass)
    
#with open(file_name_edit, 'w') as file: # Write the editied file for pandas to open
 #   file.writelines(file_lines)
    

df = pd.read_csv(file_name, sep='  | ', skiprows=skip, header=None, engine=('python'))
#print(df.head(5))
df.rename( columns={0 :'Ion Number'}, inplace=True )
df.rename( columns={1 :'Energy (keV)'}, inplace=True )
df.rename( columns={2 :'x (A)'}, inplace=True )
df.rename( columns={3 :'y (A)'}, inplace=True )
df.rename( columns={4 :'z (A)'}, inplace=True )
df.rename( columns={5 :'Electronic Stop (eV/A)'}, inplace=True )
df.rename( columns={6 :'Energy Lost to Last Recoil (eV)'}, inplace=True )

Posx = df['x (A)'].tolist()
Posy = df['y (A)'].tolist()
Posz = df['z (A)'].tolist()
Energy = df['Energy (keV)'].tolist()
Energy = [1.60218e-16*x for x in Energy] # Writing all energy in Joules
print(Energy[1])
IonNum = df['Ion Number'].tolist()
Events = max(IonNum)
KEInitial = 1.60218e-16*(df.iloc[0][1]) # Set kinetic energy variable (in J)
print(KE)

displacement = [] # Want to record the displacement in each step (in meters)
  
for i in range(Events): # Calculate displacement and record it in a 2D array which is
    temp = []           # indexed by the event number
    for j in range(len(Posx)):
        if (IonNum[j] == i + 1):
            #if Posx[j] == 0:
            #    temp.append(0)
            if Posx[j] !=0:
                temp.append(((Posx[j]-Posx[j-1])**2+(Posy[j]-Posy[j-1])**2+(Posz[j]-Posz[j-1])**2)**0.5)
    displacement.append(temp)
    
print(displacement[slice(3)])
print(len(displacement[1]))

velocity_temp = [(2*x/mass)**0.5 for x in Energy] # Want velocity from mass and energy for each step 
#print(velocity_temp)
velocity = []

for i in range(Events): # Write velocity in a nicer 2D list indexed by the event number
    temp = []           
    for j in range(len(Posx)):
        if (IonNum[j] == i + 1):
            if velocity_temp[j] != 0: 
                temp.append(velocity_temp[j])
    velocity.append(temp)

time = [[displacement[j][i]/velocity[j][i] for i in range(len(velocity[j]))] for j in range(len(velocity))] # Want to calculate total time for each event 
print(time[0])

timetot = [sum(time[i]) for i in range(len(time))] # Sums the times at each step for each event
print(timetot)

timeaverage = 0 
for i in range(len(timetot)): # Calculate average time over all events
    timeaverage += timetot[i]
timeaverage = timeaverage/Events
print(timeaverage)






