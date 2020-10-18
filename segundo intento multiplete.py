# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:03:22 2020

@author: Admin
"""

from pylab import *
from scipy.fftpack import fft, fftfreq

print("ingresa las variables")
A = float(input("Amplitud: "))
T2  = float(input("Tiempo de Relajación: "))
w = float(input("Periodo: "))
J = float(input("Constande de Acoplamiento: "))
tmin = 0
tmax = float(input("Máximo Valor de x: "))
Np = 2 ** 16

#Multiplete en el tiempo 
def multiplete(t):
    doblete = A * exp(-t/T2) * cos( w * t) * cos(2 * pi * J * t)
    doblete1 = doblete * blackman(Np)
    return doblete1 

t = arange(tmin, tmax, (tmax - tmin)/Np)
multiplete(t)

#Grafica multiplete
figure(1)
plot(t, multiplete(t))
xlabel("tiempo")
ylabel("multiplete (t)")

#Transformada de Fourier 
Ts = t[2] - t[1]
Fs = 1 / Ts
n = multiplete(t).size 
x = fft(multiplete(t)) / Np
frecuencia = fftfreq(n, d= t[2] - t[1])
    
#Grafica Transformada de Fourier
figure(2)
plot(frecuencia, abs(x))
xlim(-2, 2)
#ylim(0, )






