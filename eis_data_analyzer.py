# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:17:07 2020

@author: shatt
"""
import pandas as pd

import numpy as np

eis_data = pd.read_csv("EIS_data.csv")##load data

###grab different columns of eis data
real_part=eis_data.iloc[:,1]
imaginary_part=eis_data.iloc[:,2]
frequency=eis_data.iloc[:,0]

##Make a new list of data
my_data=[real_part,imaginary_part,frequency]

#concatanate
cleaned_data=pd.concat(my_data,axis=1)

##save as text file, only values, note the .values
np.savetxt('cleaned_data.txt', cleaned_data.values)