# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:57:06 2023

@author: Mahin
"""

import matplotlib.pyplot as plt
import numpy as np
a = [1,0,1,0,1,1,0,0,1,1,0,1]
sample_size = 32
random_sample = 16
random_number = np.random.rand(random_sample)
random_number[np.where( random_number >= .50)] = 1
random_number[np.where( random_number <= .50)] = 0



#generate the signal 

signal = np.zeros(sample_size*random_sample)

id_n = np.where(random_number == 1)

for i in id_n[0]:
    temp = int(i*sample_size)
    signal[temp:temp+sample_size] = 1

plt.figure()
plt.plot(signal)