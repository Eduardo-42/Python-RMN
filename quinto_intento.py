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

grafica.get_xdata()
grafica.get_ydata()
grafica.get_xydata()