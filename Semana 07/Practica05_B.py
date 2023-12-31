## Práctica 5 - Etapa de absorción no estacionaria
# Autor: Bruno Fernando Reyes Iglesias

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sympy as sp

meq = 0.5 # Pendiente de la línea de equilibrio
Ls = 1.3 # kmol/min Flujo molar de líquido inerte
Gs = 1.7 # kmol/min Flujo molar de gas inerte
ML = 1 # kmol Moles de líquido en el volumen
xe = 0 # Fracción molar de A en el líquido entrante
ye = 0.0909 # Fracción molar de A en el gas entrante

# Calculamos las razones molares
Xe = xe/(1-xe)
Ye = ye/(1-ye)

# Solución de la EDO con odeint
def model(X,t):
    dXdt = (Ls*(Xe-X)+Gs*(Ye-0.5*(X/(1+X))/(1-0.5*(X/(1+X)))))/ML
    return dXdt
X0 = 0 # Razón molar inicial
tspan = np.linspace(0,10,100) # Intervalo de tiempo
tsol = odeint(model,X0,tspan) # Resolvemos la EDO

# Calculamos la razón molar del gas en equilibrio como función de X.
Yeq = 0.5*(tsol/(1+tsol))/(1-0.5*(tsol/(1+tsol)))

# Graficamos X y Yeq versus tiempo
plt.figure(1)
plt.plot(tspan,tsol,'b') # Graficamos t vs valores de X
plt.title('Composición del líquido saliente')
plt.xlabel('t')
plt.ylabel('X')
plt.figure(2)
plt.plot(tspan,Yeq,'g') #Graficamos t vs valores de Yeq
plt.title('Composición del gas saliente')
plt.xlabel('t')
plt.ylabel('Yeq(X)')

# Calcular el estado estacionario
X = sp.symbols('X')
f1 = sp.Eq((Ls*(Xe-X)+Gs*(Ye-0.5*(X/(1+X))/(1-0.5*(X/(1+X)))))/ML, 0)
Xsol = sp.solve(f1)
Xest = [sol for sol in Xsol if sol >= 0]
Xest = Xest[0].evalf()
print(f'X en al estado estacionario: {Xest:.4e}\n')

