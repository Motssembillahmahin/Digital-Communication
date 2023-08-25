# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:02:10 2023

@author: Mahin
"""

import matplotlib .pyplot as plt
import numpy as np
from  math import pi
import generate_signal as gs
plt.close('all')
fs = 1000;#sampling frequency
fc = 100; #carrier frequency
T = 1
t = np.arange(0, T, 1/fs)

#carrier frequency

x = np.sin(2*pi*fc*t)

given_binary_signal = gs.signal
plt.subplot(2,1,1)
plt.plot(given_binary_signal)

#ask 

ask = x * given_binary_signal;

plt.subplot(2,1,2)
plt.plot(ask)
