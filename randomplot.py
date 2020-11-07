# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:15:29 2020

@author: jaimes
"""

import numpy as np
import matplotlib.pyplot as plt

v1 = [2*1, 2*0]#Aqui se supone que cree los vectores
v2 = [-2*(3**(-0.5)), 2*2*(3**(-0.5))]
ejex=[]
ejey=[]

vrandomv1 = np.random.randint(low=-100, high=100, size=150)#Se generan valores random de -100 a 100 150 valores

vrandomv2 = np.random.randint(low=-100, high=100, size=150)

print(vrandomv1)
i=0
for value in vrandomv1:
    '''Por cada valor en vrandomv1 tomamos el primer valor de la lista y lo multiplicamos por el primer valor de v1 posteriormente tomamos otro 
    valor aleatorio vrandomv2 en este caso y lo multiplicamos por v2 en x para y hacemos lo mismo con los valores random pero para Y de v1 y v2'''
    valor = vrandomv1[i]*v1[0] + vrandomv2[i]*v2[0]
    valor2 = vrandomv1[i]*v1[1] + vrandomv2[i]*v2[1]
    print(valor, valor2)
    #Subo los daots en dos listas vacias
    ejex.append(valor)
    ejey.append(valor2)
    i+=1

#valores random
plt.scatter(ejex, ejey)
#los dos puntos que me diste
plt.scatter(v1[0], v1[1])
plt.scatter(v2[0], v2[1])
plt.show()

    
