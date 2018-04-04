import pandas as pd 
import numpy as np
import csv

file = 'raw.csv'
labelled_file = 'Labelled.csv'
output_file = 'Eyescan.csv'


df_raw = pd.read_csv(file)
df_labelled = pd.read_csv(labelled_file)

first = df_raw ['Patient']
second = df_raw['FINDINGS']
a = df_labelled['OpticNerve']
b = df_labelled['Retina']
c = df_labelled['Macula']
d = df_labelled['Vitreous']
e = df_labelled['Cornea']
f = df_labelled['Lens']
g = df_labelled['Conjunctival']
h = df_labelled['Pupil']
i = df_labelled['Eyelids']

np_first = first.values
np_second = second.values
np_a = a.values
np_b = b.values
result = list(zip(np_first, np_second, a, b, c, d,e,f,g,h,i))

with open(output_file, 'w') as myfile:
    wr = csv.writer(myfile, delimiter=',')
    wr.writerow(('Patient', 'Findings', 'OpticNerve', 'Retina', 'Macula', 'Vitreous', 'Cornea',
			'Lens', 'Conjunctival', 'Pupil', 'Eyelids'))
    for r in result:
    	wr.writerow(r)