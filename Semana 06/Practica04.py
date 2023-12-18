## Práctica 4 - Análisis de un CSTR
# Autor: Bruno Fernando Reyes Iglesias

## Librerías usadas
import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt

print('PRÁCTICA 4 - ANÁLISIS DE UN CSTR')
CA0 = 1  # lbmol/ft^3  Concentración en la alimentación
F = 7.67/60  # lbmol/s  Flujo molar
k = 0.311  # ft^3/lbmol*s  Constante cinética
R = 5  # ft  Radio del tanque
Ro = 0.625  # ft  Radio del orificio
V0 = F/CA0  # ft^3/s  Flujo volumétrico
g = 32.174  # ft/s^2  Aceleración por gravedad

# 1. A volumen constante de 250 ft^3
VR = 250  # ft^3  Volumen del reactor en estado estacionario
tau = VR/V0  # s  Tiempo de residencia
def modelo1(x, t):
    dCAdt = (CA0-x-k*(x**2)*tau)/tau
    return dCAdt
t1 = np.linspace(0,50,101)  # Intervalo de tiempo
x0 = CA0  # Valor incial (CA incial)
sol1 = odeint(modelo1, x0, t1)

# 2. A volumen variable
As = np.pi*Ro**2  # Area del orificio
def modelo2(X, t):
    dCAdt = (CA0*(V0/X[1])-X[1]*(((As/R)*np.sqrt(2*g*X[1]/np.pi))/X[1])-k*(X[0]**2)-(X[0]/X[1])*(V0-(As/R)*np.sqrt(2*g*X[1]/np.pi)))
    dVRdt = V0-(As/R)*np.sqrt(2*g*X[1]/np.pi)
    return [dCAdt, dVRdt]
t2 = np.linspace(0,250,101)
X0 = [CA0, 500]  # Valores inciales (CA incial, volumen incial)
#sol2 = odeint(modelo2, X0, t2, atol=1e-6, rtol=1e-6)
solucion = solve_ivp(modelo2, [t2[0], t2[-1]], X0, t_eval=t2)
print(solucion)

# Grafica de las respuestas
plt.figure(1)
plt.plot(t1,sol1,'-r',label='Concentración de A')
plt.xlabel('Tiempo (s)')
plt.ylabel('CA (lbmol/ft^3)')
plt.title('Problema 1')
plt.legend()
plt.grid()
plt.figure(2)
plt.plot(t2,sol2[:,0],'-b',label='Concentración de A')
plt.xlabel('Tiempo (s)')
plt.ylabel('CA (lbmol/ft^3)')
plt.title('Problema 2')
plt.legend()
plt.grid()
plt.figure(3)
plt.plot(t2,sol2[:,1],'-m',label='Volumen del reactor')
plt.xlabel('Tiempo (s)')
plt.ylabel('VR (ft^3)')
plt.title('Problema 2')
plt.legend()
plt.grid()
plt.show()