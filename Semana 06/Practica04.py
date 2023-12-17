## Práctica 4 - Análisis de un CSTR
# Autor: Bruno Fernando Reyes Iglesias

## Librerías usadas
import numpy as np
import sympy as sp
from scipy.integrate import ode, odeint
import matplotlib.pyplot as plt

print('PRÁCTICA 4 - ANÁLISIS DE UN CSTR')
CA0 = 1  # lbmol/ft^3  Concentración en la alimentación
F = 7.67  # lbmol/s  Flujo molar
k = 0.311  # ft^3/lbmol*s  Constante cinética
R = 5  # ft  Radio del tanque
Ro = 0.5  # ft  Radio del orificio
V0 = F/CA0  # ft^3/s  Flujo volumétrico
g = 32  # ft/s^2  Aceleración por gravedad
# 1. A volumen constante de 250 ft^3
VR = 250  # ft^3  Volumen del reactor en estado estacionario
tau = VR/V0  # s  Tiempo de residencia
def modelo1(t,CA,k,tau,CA0):
    dCAdt = (CA0-CA-k*(CA**2)*tau)/tau
    return dCAdt
tspan = np.linspace(0,50,101)  # Intervalo de tiempo
x0 = CA0  # Concentración inicial de A
sol = odeint(modelo1,x0,tspan,args=(k,tau,CA0))
print(sol)
plt.plot(tspan,sol[:,0])
plt.show()