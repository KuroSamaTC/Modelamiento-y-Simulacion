# practica 03
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# datos
t=np.array([0,1,2,3,4,5])
v=np.array([1.2,3.4,6.5,9.1,11.8,14.7])
# funcion
def fcn_lineal (x, m, b):
    return x * m + b
# ajuste
optimvars, covarianza = curve_fit(fcn_lineal, t, v)
# parametros de ajuste
m, b = optimvars
# grafica de datos
plt.scatter(t,v,label='data')
plt.plot(t,fcn_lineal(t,m,b),'r-',label='Ajuste lineal')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.show()
