# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 09:30:24 2023

@author: Mahin
"""

import matplotlib.pyplot as plt
import numpy as np

sample_size = 32
binary_code = [1,0,1,0,1,0,1,0,1]
binary_code_arr = np.array(binary_code)
b_len = len(binary_code_arr)
plt.stem(binary_code_arr)

#generating signal
signal = np.zeros(sample_size*b_len)

id_n = np.where(binary_code_arr == 1)

for i in id_n[0]:
    temp = int(i*sample_size)
    signal[temp:temp+sample_size] = 1
plt.figure()
plt.plot(signal)