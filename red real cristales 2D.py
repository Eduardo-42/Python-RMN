# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:28:20 2020

@author: Admin
"""


from pylab import *
 
a  = 1.0
a1 = array( [1,-1] )*a #para que sea vector y no lista hay que escribirlo con un array como ahi se ve
a2 = array( [1,1] )*a

"""
no le hagas caso a esto
A = array([a1,a2])
B = 2*pi*linalg.inv(A)
  
b1 = B.T[0]
b2 = B.T[1]

dot(a2,b2)
"""
num_a1 = 4 # cuantos valores queremos en n
num_a2 = 3 #cuantos valores queremos en m

n = linspace(-num_a1, num_a1, 2 * num_a1+1)
m = linspace(-num_a2, num_a2, 2 * num_a2+1)
 
N,M = meshgrid(n,m) #meshgrid hace todas las combinaciones posibles de n con m, al hacer eso lo deja en forma de matriz

N = N.reshape((2 * num_a1 + 1)*(2 * num_a2 + 1)) # lo pasa a lista (horizontal), no queremos matriz
M = M.reshape((2* num_a1 + 1) * (2 * num_a2 + 1)) 


parejas = column_stack((N, M)) #pasa la combinacion de todas las posobilidades a columnas(pares ordenados de N y M) 1 con 1 y asi

a = array([a1, a2]) #hace la matriz del vector a1 y a2
R = dot(parejas, a) #hace el producto punto entre los pares ordenados N,M y los vectores a1 y a2
x = R.T[0] #vuelve a pasar de columnas a filas los primeros del arreglo
y = R.T[1] #vuelve a pasar de columnas a filas los segundos del arreglo
scatter(x,y) #scatter sirve para graficar puntos 
