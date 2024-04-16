
import csv
import pandas as pd
import numpy as np

input_file = 'CONFIG/ISE/juice_0.0.4_EXTENDED.brf'


import codecs

# doc = codecs.open(input_file,'rU','UTF-16')

df = pd.read_csv(input_file, names=['dt', '1', '2', '3'], header=None, comment='#', engine='python', sep='\s+')

print(df['dt'].iloc[0])
#
df['HgaX'] = df['1']*1000
df['Hgak'] = df['2']*1000
df['HgaB'] = df['3']*1000
df['MgaX'] = df['1']*0
df['Mgak'] = df['2']*0
df['Mgak'] = df['3']*0

df['HgaX'] =df['HgaX'].astype(int)
df['Hgak'] =df['Hgak'].astype(int)
df['HgaB'] =df['HgaB'].astype(int)
df['MgaX'] =df['MgaX'].astype(int)
df['Mgak'] =df['Mgak'].astype(int)
df['Mgak'] =df['Mgak'].astype(int)


del df['1']
del df['2']
del df['3']

df.to_csv('BRF_GEN_0_0_4_290102_370525_V02.asc', index=False, header=True, sep="\t", quoting=csv.QUOTE_NONE)