# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:15:29 2020

@author: jaime
"""

import numpy as np
import matplotlib.pyplot as plt

v1 = [2*1, 2*0]
v2 = [-2*(3**(-0.5)), 2*2*(3**(-0.5))]
ejex=[]
ejey=[]

vrandomv1 = np.random.randint(low=-100, high=100, size=150)

vrandomv2 = np.random.randint(low=-100, high=100, size=150)

print(vrandomv1)
i=0
for value in vrandomv1:
    valor = vrandomv1[i]*v1[0] + vrandomv2[i]*v2[0]
    valor2 = vrandomv1[i]*v1[1] + vrandomv2[i]*v2[1]
    print(valor, valor2)
    ejex.append(valor)
    ejey.append(valor2)
    i+=1


plt.scatter(ejex, ejey)
plt.scatter(v1[0], v1[1])
plt.scatter(v2[0], v2[1])
plt.show()

    