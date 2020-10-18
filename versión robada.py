# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:01:39 2020

@author: Admin
"""
from pylab import * 
from scipy.fftpack import fft, fftfreq


#Fourier
A = 1
T2  = 1
w = 1
J = 1

Np = 2 ** 12
Fo =1000 / 2 * pi 
tmin = -100
tmax = 100
t = arange(tmin, tmax, (tmax - tmin)/Np)
Ts = t[2]-t[1] #Periodo de muestreo
Fs = 1 / Ts #Frecuencia de muestreo 
x = A * exp(-t/T2) * cos(w * t) * cos(2 * pi * J * t)
X = fft(x) #Ts es factor de escalamiento para señales aperiodicas 
X1 = fftshift(X)
frq = arange (-Fs/2, Fs/2, Fs/Np)
print(len(X1), len(frq), Fs/2)

print(t)
plot(frq, abs(X1))