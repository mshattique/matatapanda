# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:29:28 2020

@author: shatt
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt


i_V_data = pd.read_csv("IV_data.csv")##load data

###grab different columns of I_V data
Grab_Voltage_vals=i_V_data.iloc[:,0]
Grab_Current_vals=i_V_data.iloc[:,1]

Ohmic_loss = Grab_Current_vals * 0.3288
Activation_and_Conc_loss= Grab_Voltage_vals - Ohmic_loss


fig, ax = plt.subplots()
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 14,
        }


plt.plot(Grab_Current_vals, Grab_Voltage_vals, label='Voltage',Linewidth='3')
plt.plot(Grab_Current_vals, Ohmic_loss, label = 'Ohmic Loss',Linewidth='3')
plt.plot(Grab_Current_vals, Activation_and_Conc_loss, 
         label = 'Activation + Concentration Loss',Linewidth='3')


plt.title('I-V Curves of the Fuel Cell',fontdict=font)
plt.xlabel('Current(I)',fontdict=font)
plt.ylabel('Voltage(V)',fontdict=font)


ax.tick_params(axis="y",direction="in")
ax.tick_params(axis="x",direction="in")


plt.xlim(0,1.4)
plt.ylim(0,1.2)
plt.legend()
plt.savefig('I_V_curve.png')
plt.show()
