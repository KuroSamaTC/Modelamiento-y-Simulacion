## Práctica 5 - Tanque calentado por resistencia
# Autor: Bruno Fernando Reyes Iglesias

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sympy as sp

# Parámetros
R = 10  # Resistencia
DV = 220  # Voltios
Ce = 4.187e3  # J.Kg-1.K-1 calor específico
T0 = 25  # °C Temperatura inicial del tanque
Te = 17  # °C Temperatura del agua entrante
V = 0.1  # m3 Volumen
p = 1000  # kg/m3 Densidad
Q = 1.667e-5  # m3/s Caudal de agua entrante
q = DV**2/R  # W Calor producido por la resistencia

# Definición de la variable simbólica
t = sp.symbols('t')
T = sp.Function('T')

# Ecuación diferencial y condición inicial
eqn = sp.Eq(T(t).diff(t), (Q/V)*(Te+q/(p*Q*Ce)-T(t)))
cond = {T(0): T0}
Tsol = sp.dsolve(eqn, T(t), ics=cond)
Tsol1 = Tsol.args[1].subs(t, 36000)
Tsol1 = Tsol1.evalf() # Temperatura a las 10 horas
print(f'Temperatura en 10 horas (solución analítica): {Tsol1:.4f} °C\n')

# Resolución numérica usando odeint
def model(x, t):
    return (Q/V)*(Te+q/(p*Q*Ce)-x)
x0 = T0 #  Condición inicial
tspan = np.linspace(0, 36000, 1000) #  Tiempo 10 horas
x = odeint(model, x0, tspan)

# Temperatura al estado estacionario
T = sp.symbols('T')
T_steady = sp.solve((Q/V)*(Te+q/(p*Q*Ce)-T))[0]
T_steady = T_steady.evalf()
print(f'Temperatura al estado estacionario: {T_steady:.4f} °C')

# Tiempo en el que alcanza el 99% del valor estacionario
T_steady_99 = sp.Eq(Tsol.args[1] - T_steady*0.99, 0)
t_99 = sp.nsolve(T_steady_99, t, 1)/3600 # Tiempo en el que alcanza el 99% estacionario
print(f'Tiempo en el que alcanza 0.99 de la Temp. en estacionario: {t_99:.4f} h')

# Gráfico
time = tspan/3600 #  Vector con tiempo en horas
plt.plot(time, x, '-r', label='Temperatura °C')
plt.ylabel('T(t) (°C)')
plt.xlabel('t/3600 (h)')
plt.axis([0, 10, 20, 100])
plt.title('Cambio de la temperatura en el tanque')
plt.legend()
plt.grid()
plt.show()