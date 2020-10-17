# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:05:31 2020

@author: jaime
"""

import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
class Graficador:
    def __init__(self, titulo):
        self.titulo=titulo
         
    def corte(self):
        with open(f'{self.titulo}.txt') as f: #Abre el archivo con los datos del archivo .txt
            signal_stock=(np.loadtxt(f, dtype=str, delimiter='\n')) # Elimina toos los cambios de linea de la matriz
            #print(signal_stock)
            value2=[]
            self.MHZ=[]
            self.ppm=[]
            self.inten=[]      
            x=0
            #y=0
            for i in signal_stock: #Por cada valor en signal_stock
                
                value=signal_stock[x] #transferimos el string a una matriz IDONTKNOWFORWHAT BUT I DID IT
                value=value.split(' ') #cortamos la matriz delimitandola por espacios
                for valor in value:
                    if valor != '':
                        value2.append(valor) #Si el valor de la matriz es diferente a espaciovacio añadelo a value2
                    
                #value = value.replace(' ', '')
                
                x+=1
            
            while len(value2) != 0: #Mientras la longitud de value2 sea diferente de cero
               self.MHZ.append(value2[0]) #añade el primer valor a MHZ
               value2.pop(0) #Borra el primer valor
               self.ppm.append(value2[0]) 
               value2.pop(0)
               self.inten.append(value2[0])
               value2.pop(0)
               
        #print(f'value2: {value2}')                 
        #print(self.MHZ)
        #print(self.ppm)
        #print(self.inten)
        
    
    def graficar(self):
        output_file(f'{self.titulo}.html') #Crea un archivo de salida
        fig = figure() #Donde exista una figura
        x_vals=self.ppm 
        y_vals=self.inten
        y_vals=list(map(float, y_vals)) #convierte la matriz a float
        x_vals=list(map(float, x_vals))
        x_axes = np.arange(0, 14, 0.001).tolist() #crea una matriz de 0 a 14 con valores de 0.001
        #y_vals =y_vals[::-1]
        
        x_axes = [round(num, 3) for num in x_axes] #redondea los valores de x_axes a 3 decimales
        y_axes=[]
        position=0
        for i in x_axes: #por cada valor en x_axes
            y_axes.append(0) #añade un cero a y_axes
            if x_axes[position] in x_vals: #Si algun valor en x_axes existe en x_vals
                #print(x_axes[position])
                lugar = x_vals.index(x_axes[position]) #encuentra la posicion de ese valor en x_vals
                #print(lugar)#Modificar esta parte 
                y_axes[position] = y_vals[lugar] #Esa posicion será el mismo lugar que el y_vals que al mismo tiempo sera el valor de y_axes
            position+=1
        #print(x_vals)
        #print(x_axes)
        #print(y_vals)
        
        fig.y_range = Range1d(start=0,end=1500) #modificacion de valores del eje y en grafica
        fig.x_range = Range1d(start=14, end=0) #loanterior pero en x
        fig.line(x_axes, y_axes, line_width=2) #crea grafica
        show(fig) #mostrar grafica
#print(value2)
if __name__ == "__main__":
    pregunta1 = input('escribe el nombre del archivo a graficar: ')
    s = Graficador(pregunta1)
    s.corte()
    s.graficar()
    
       
    
        