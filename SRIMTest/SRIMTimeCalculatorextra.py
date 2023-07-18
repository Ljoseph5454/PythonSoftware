import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
pd.options.display.max_seq_items = None
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

file_name = 'EXYZ.txt'
file_name_edit = file_name[0:-4] + '_edit1.txt'
skip = 0
Data = 0
avo = 6.0221408e+23
amu = 0 
KE = 0
IonData = ''
file_lines = []

with open(file_name, 'r') as file: # Searches for the row in which data starts and
    done = 0                       # looks for the ion data in the file (we want the mass)
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

mass = float(IonData[1]) # Set the mass variable
    
with open(file_name_edit, 'w') as file: # Write the editied file for pandas to open
    file.writelines(file_lines)
    

df = pd.read_csv(file_name_edit, sep="  ", skiprows=skip, header=None)
#print(df.head(5))
df.rename( columns={0 :'Ion Number'}, inplace=True )
df.rename( columns={1 :'Energy (keV)'}, inplace=True )
df.rename( columns={2 :'x (A)'}, inplace=True )
df.rename( columns={3 :'y (A)'}, inplace=True )
df.rename( columns={4 :'z (A)'}, inplace=True )
df.rename( columns={5 :'Electronic Stop (eV/A)'}, inplace=True )
df.rename( columns={6 :'Energy Lost to Last Recoil (eV)'}, inplace=True )

Num = df['Ion Number'].tolist()
Time = []
KE = df.iloc[0][1] # Set kinetic energy variable
print(KE)

