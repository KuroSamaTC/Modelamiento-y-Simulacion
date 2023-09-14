## Practica 3 - Modelizacion en base a datos experimentales
# Autor: Bruno Fernando Reyes Iglesias
print('PRACTICA 2 - MODELIZACION EN BASE A DATOS EXPERIMENTALES')
## Uso de scipy para ajuste de curva con datos experimentales
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
## PROBLEMA 3
print('Problema 3')
# Datos
time=np.array([0.5,1,2,3,4,5,6,7,8,9])
poblation=np.array([7,5.2,3.8,3.2,2.5,2.1,1.8,1.5,1.2,1.1])
# Definir la funcion
def modelo(t,A,B,C):
    return A*np.exp(-1.5*t)+B*np.exp(-0.3*t)+C*np.exp(-0.05*t)
# Ajuste de datos
optimvars,covarianza=curve_fit(modelo,time,poblation)
# Recuperacion de parametros
A,B,C=optimvars
print('Parametros de ajuste:')
print('   A = %.4f' % (A))
print('   B = %.4f' % (B))
print('   C = %.4f' % (C))
# Grafica de datos y curva de ajuste
plt.scatter(time,poblation,label='data')
plt.plot(time,modelo(time,A,B,C),'--r',label='Curva de ajuste')
plt.xlabel('Tiempo (hr)')
plt.ylabel('Poblacion (Nº)')
plt.legend()
plt.show()
