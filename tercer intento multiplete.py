# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:58:33 2020

@author: Liat Colmenares V
Referencia: http://www.fimee.ugto.mx/profesores/ljavier/documentos/Lec01%20-%20Teorema%20de%20Muestreo.pdf
"""


from pylab import *
from scipy.fftpack import fft, fftfreq

print("ingresa las variables") #Pide todas las variables desde consola para evitar moverle al codigo
A = 1 # float(input("Amplitud: "))
T2  = float(input("Tiempo de Relajación: "))
w = float(input("Desplazamiento Quimico: "))
J = float(input("Constante de Acoplamiento: "))
tmin = 0 #los tiempos negativos no nos sirven de nada
tmax = float(input("Máximo Valor de x: ")) #si le pones menos de 100 sale con poca resolucion la transformada
Np = 2 ** 13 #numero de puntos para la simulacion


#Multiplete en el tiempo/ me quise lucir poniendo una función 
def multiplete(t):
    doblete = A * exp(-t*T2) * cos( 2* pi * w * t) * cos(2 * pi * J * t)
    return doblete 


t = arange(tmin, tmax, (tmax - tmin)/Np) #variable independiente de la función abajo cuando uso el return
multiplete(t) #llamo a la funcion para usar sus valores mas abajo y no marque error

#Grafica multiplete/ una simple grafica 
figure(1)
plot(t, multiplete(t))
xlabel("tiempo")
ylabel("multiplete (t)")

#Transformada de Fourier/ me quise lucir x2 con la función
def transformada():
    x = fft(multiplete(t)) / Np #aplico la transformada al multiplete en el tiempo y normalizo entre el no. de puntos
    x1 = fftshift(x) #ajusto la transformada al cero 
    return x1

transformada() #vuelvo a llamar a la funcion para que no me marque error y usar sus valores

Ts = t[2] - t[1] #Tasa de muestreo: intervalo de tiempo entre 2 muestras
Fs = 1 / Ts #Frecuencia de muestreo: muestras tomadas por segundo
frecuencia = arange(-Fs / 2, Fs / 2, Fs / Np) #variable x de frecuencias para la transformada
print("Para Corroborar: ", len(transformada()), len(frecuencia), Fs/2) #ver comentario de abajo

"""
1) para la variable de frecuencia se puede hacer tambien con el comando fftfreq 
2) en la linea 48 imprimo el largo del array de transformada y de freccuencia
    para ver que tengan el mismo no. de puntos por que si no no encajan y no sale la grafica
3) imrpimir Fs/2 nos dice cuanto esmamos viendo en x (corroborar que el numero coincida con los limites de la grafica de fft)
    y el teorema de muestreo dice que solo se puede ver la mitad de la frecuencia de muestreo 
"""
    
#Grafica Transformada de Fourier/ una simple grafica x2
figure(2)
plot(frecuencia, transformada())
title("tercer intento")
xlabel("Frecuencia")

print("Gracias por Utilizar el Simulador de Liat n.n/")
print()