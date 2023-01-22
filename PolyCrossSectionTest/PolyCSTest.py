import matplotlib.pyplot as plt
import numpy as np
import os, pickle
import sys
import pandas as pd
df = pd.read_csv('Hit8.csv')
print(df.head())

side = -100

hitx = df[df['Hit']==1]['Hit'].tolist()

print(len(hitx))