import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
pd.options.display.max_seq_items = None
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

with open('91_233_Protactinium_NC.txt', 'r') as file:
    head = [next(file) for _ in range(5)]
    print(head)
    data1 = ''
    for i in range(len(head)):
        data1=data1 + head[i]

    print(data1)    
    

df = pd.read_csv('91_233_Protactinium_NC.txt', sep="  ", skiprows=5, header=None)
#df = pd.read_csv('ee.csv')
df.rename( columns={0 :'x'}, inplace=True )
df.rename( columns={1 :'y'}, inplace=True )
df.rename( columns={2 :'x1'}, inplace=True )
df.rename( columns={3 :'y1'}, inplace=True )
df.rename( columns={4 :'x2'}, inplace=True )
df.rename( columns={5 :'y2'}, inplace=True )


print(df.iloc[0]['y1'])

for i in range(len(df['y'])):
    if (df.iloc[i]['x'] < 1):
        df.iloc[i]['y'] = 1
    if (df.iloc[i]['x'] >= 1):
        df.iloc[i]['y'] = 10000

for i in range(len(df['y1'])):
    if (df.iloc[i]['x1'] < 1):
        df.iloc[i]['y1'] = 1
    if (df.iloc[i]['x1'] >= 1):
        df.iloc[i]['y1'] = 10000
        
for i in range(len(df['y2'])):
    if (df.iloc[i]['x2'] < 1):
        df.iloc[i]['y2'] = 1
    if (df.iloc[i]['x2'] >= 1):
        df.iloc[i]['y2'] = 10000
        
empty_col = pd.DataFrame(['']*len(df))
df.insert(0, 'col1', empty_col)

print(df.head(175))

df.to_csv('91_233_Protactinium_NC_edit.txt', header=None, index=False, float_format='%.6e')

with open('91_233_Protactinium_NC_edit.txt', 'r') as file:
    data = file.read()
    data = data.replace(',', '  ')
    data = data1 + data
    
with open('91_233_Protactinium_NC_edit.txt', 'w') as file:
    file.write(data)
    