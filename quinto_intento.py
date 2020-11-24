from nmrsim import Multiplet
from nmrsim.plt import mplplot
import matplotlib.pyplot as plt

# 1200 Hz, 2H, td, J= 7.1, 1.1 Hz
td = Multiplet(1200.0, 2, [(7.1, 2), (1.1, 1)])
print(td.v)
print(td.I)
print(td.J)

# print(td.peaklist())

grafica = mplplot(td.peaklist())

print(type(grafica)) #imprime el tipo de grafica 

print(grafica[1]) #imprime el segundo valor de la tupla grafica que son las intensidades en forma de lista

print(f'la longitud de los valores de X en grafica 1 son: {len(grafica[1])}')
print(f'la longitud de los valores de Y en grafica 1 son: {len(grafica[0])}')

#DEBIDO A QUE SON DIMENSIONES IGUALES EL ORDENAMIENTO DE TUPLAS ES 1 a 1 por lo que

axe_x = grafica[0]
axe_y = grafica[1]

x=grafica[1] #Muestra de que el array Y muestra las intensidades sin se rnormalizados

plt.plot(x) #La grafica muestra el mismo valor que [grafica]
plt.show()

print(td.peaklist()) #Te imprime la lista de los valores correspondientes a la RMN en forma de lista que guarda tuplas de pares

print(type(td.peaklist()))

axes = plt.gca()

line = axes.lines[0]

line.get_xdata()
#grafica.get_ydata()
grafica.get_xydata() 