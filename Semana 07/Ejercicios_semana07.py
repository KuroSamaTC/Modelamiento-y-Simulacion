## Ejercicio sobre calentamiento de una placa
# Autor: Bruno Fernando Reyes Iglesias

import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# Parámetros
p = 7600 # densidad kg/m3
vod = 47 # conductividad W/m/K
Cp = 480 # Capacidad calorífica J/kg
T0 = 400 # Temperatura inicial K
TH = 800 # Temperatura arriba K
TD = 300 # Temperatura abajo K
TR = 500 # Temperatura derecha
TL = 800 # Temperatura izquierda
L = 1 # Largo del borde m
dt = 0.99 * 8.0816 # Variación tiempo
N = 50 # Número de segmentos
tkon = 1000 # Tiempo final

# Cálculos
a = vod / (p * Cp)
dz = L / (N - 1) # tamaño del paso
M = (dz**2) / (dt * a) # Valor de M
t = dt

# Inicialización de temperaturas
Tpoc = np.full((N, N), T0)

# Cálculos para cada t
while t < tkon:
    # T en los límites (esquinas)
    Tpoc[0, 0] = (Tpoc[1, 0] + TL + TH + Tpoc[0, 1] + (M - 4) * Tpoc[0, 0]) / M # Esquina superior izquierda (1,1)
    Tpoc[0, -1] = (Tpoc[1, -1] + TH + Tpoc[0, -2] + TR + (M - 4) * Tpoc[0, -1]) / M # Esquina superior derecha (1,N)
    Tpoc[-1, 0] = (TD + Tpoc[-2, 0] + TL + Tpoc[-1, 1] + (M - 4) * Tpoc[-1, 0]) / M # Esquina inferior izquierda (N,1)
    Tpoc[-1, -1] = (TD + Tpoc[-2, -1] + Tpoc[-1, -2] + TR + (M - 4) * Tpoc[-1, -1]) / M # Esquina inferior derecha (N,N)

    # Cálculos de T (laterales)
    Tpoc[0, 1:-1] = (Tpoc[1, 1:-1] + TH + Tpoc[0, :-2] + Tpoc[0, 2:] + (M - 4) * Tpoc[0, 1:-1]) / M # Frontera superior
    Tpoc[-1, 1:-1] = (TD + Tpoc[-2, 1:-1] + Tpoc[-1, :-2] + Tpoc[-1, 2:] + (M - 4) * Tpoc[-1, 1:-1]) / M # Frontera inferior
    Tpoc[1:-1, 0] = (Tpoc[2:, 0] + Tpoc[:-2, 0] + TL + Tpoc[1:-1, 1] + (M - 4) * Tpoc[1:-1, 0]) / M # Frontera izquierda
    Tpoc[1:-1, -1] = (Tpoc[2:, -1] + Tpoc[:-2, -1] + Tpoc[1:-1, -2] + TR + (M - 4) * Tpoc[1:-1, -1]) / M # Frontera derecha

    # Cálculo de todos los nodos
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            Tpoc[i, j] = (Tpoc[i + 1, j] + Tpoc[i - 1, j] + Tpoc[i, j - 1] + Tpoc[i, j + 1] + (M - 4) * Tpoc[i, j]) / M
    
    # Gráfica
    plt.clf()
    plt.pcolor(np.flipud(Tpoc), cmap='jet')
    titulo = 'Tiempo = {} s'.format(t)
    plt.title(titulo)
    plt.colorbar()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(0.02)
    t += dt # tiempo

plt.show()