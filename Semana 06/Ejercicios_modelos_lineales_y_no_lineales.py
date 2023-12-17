## Modelos lineales y no lineales al estado estacionario
# Autor: Reyes Iglesias Bruno Fernando

## Librerias usadas:
import numpy as np
import sympy as sp
from scipy.optimize import root

## PROBLEMA 1
print('\nPROBLEMA 1\n')
def punto_fijo(g, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_next = g(x)
        if abs(x_next - x) < tol:
            return x_next, i
        x = x_next
def g1(x):
    return (10*x+5)**(1/3)
x0 = 1.0
sol = punto_fijo(g1, x0, tol=1e-6, max_iter=150)
if sol is not None:
    print(f'Solución aproximada: {sol[0]:.6f}\nIteraciones: {sol[1]}\n')
else:
    print('El método del punto fijo no convergió dentro del número máximo de iteraciones.\n')

## PROBLEMA 2
print('\nPROBLEMA 2\n')
def biseccion(f, ran, tol, max_iter):
    x0=ran[0]; xf=ran[1]
    for i in range(max_iter):
        xm = (x0+xf)/2
        f0=f(x0)
        fm=f(xm)
        ff=f(xf)
        if np.sign(f0)!=np.sign(fm):
            x0=x0; xf=xm
        elif np.sign(fm)!=np.sign(ff):
            x0=xm; xf=xf
        if abs(xm-(x0+xf)/2) < tol:
            return xm, i
def f(x):
    return np.exp(3*x)-4
sol = biseccion(f, ran=[0,1], tol=1e-6, max_iter=150)
if sol is not None:
    print(f'Solución aproximada: {sol[0]:.6f}\nIteraciones: {sol[1]}\n')
else:
    print('El método del punto fijo no convergió dentro del número máximo de iteraciones.\n')

## PROBLEMA 3
print('\nPROBLEMA 3\n')
def newton_rhapson(f, dfdx, x0, tol, max_iter):
    for i in range(max_iter):
        x_next = x0-f(x0)/dfdx(x0)
        if abs(x_next-x0) < tol:
            return x_next, i
        else:
            x0 = x_next
def dfdx(x):
    return 3*np.exp(3*x)
sol = newton_rhapson(f, dfdx, x0=0, tol=1e-6, max_iter=150)
if sol is not None:
    print(f'Solución aproximada: {sol[0]:.6f}\nIteraciones: {sol[1]}\n')
else:
    print('El método del punto fijo no convergió dentro del número máximo de iteraciones.\n')

## PROBLEMA 4
print('\nPROBLEMA 4\n')
x = sp.symbols('x')
eqn1 = x**3-10*x-5
raices = sp.solve(eqn1, x)
for raiz in raices:
    sol1 = raiz.evalf()
print(f'Solución simbólica pregunta 1:\n {sol1}\n')
x0 = 1
sol2 = root(f, x0)
print(f'Solución numérica pregunta 2:\n {sol2}\n')

## PROBLEMA 5
print('\nPROBLEMA 5\n')
# 1. CO2 + H2O -> C6H12O6 + O2
A = np.array([[1, 0, 0],
              [2, 1,-2],
              [0, 2, 0]])
B = np.array([6, 6, 12])
coef_solve = np.linalg.solve(A, B)
print(f'1. {coef_solve[0]:.2f} CO2 + {coef_solve[1]:.2f} H2O -> 1.00 C6H12O6 + {coef_solve[2]:.2f} O2')
# 2. AgNO3 + K2CrO4 -> Ag2CrO4 + KNO3
A = np.array([[0, 2],
              [1, -1]])
B = np.array([1, 0])
A_inv = np.linalg.inv(A)
coef_inv = np.dot(A_inv, B)
print(f'2. 1.00 AgNO3 + {coef_inv[0]:.2f} K2CrO4 -> {coef_inv[1]:.2f} Ag2CrO4 + 1.00 KNO3')
# 3. Mg + HCl -> MgCl2 + H2
A = np.array([[1, 0,-1],
              [0, 1, 0],
              [0, 1,-2]])
B = np.array([0, 2, 0])
coef_lstsq, residuals, rank, singular_values = np.linalg.lstsq(A, B,rcond=None)
print(f'3. {coef_lstsq[0]:.2f} Mg + {coef_lstsq[1]:.2f} HCl -> {coef_lstsq[2]:.2f} MgCl2 + 1.00 H2\n')

## PROBLEMA 6
print('\nPROBLEMA 6\n')
# 1. KMnO4 + HCl -> KCl + MnCl2 + H2O + Cl2
A = np.array([[0,-1, 0, 0, 0],
              [0, 0,-1, 0, 0],
              [0, 0, 0,-1, 0],
              [1, 0, 0,-1, 0],
              [1,-1,-2, 0,-2]])
B = np.array([-1,-1,-4, 0, 0])
coef1 = np.linalg.solve(A, B)
# 2. Cl2 + Ca(OH)2 -> Ca(ClO3)2 + CaCl2 + H2O
A = np.array([[0,-2,-2, 0],
              [1,-1,-1, 0],
              [2,-6, 0,-1],
              [2, 0, 0,-2]])
B = np.array([-2*coef1[4], 0, 0, 0])
coef2 = np.linalg.solve(A, B)
# 3. Ca(ClO3)2 + Na2SO4 -> CaSO4 + NaClO3
A = np.array([[0,-1],
              [4,-3]])
B = np.array([-2*coef2[1],-2*coef2[1]])
coef3 = np.linalg.solve(A, B)
print(f'1. 1.00 KMnO4 + {coef1[0]:.2f} HCl -> {coef1[1]:.2f} KCl + {coef1[2]:.2f} MnCl2 + {coef1[3]:.2f} H2O + {coef1[4]:.2f} Cl2')
print(f'2. {coef1[4]:.2f} Cl2 + {coef2[0]:.2f} Ca(OH)2 -> {coef2[1]:.2f} Ca(ClO3)2 + {coef2[2]:.2f} CaCl2 + {coef2[3]:.2f} H2O')
print(f'3. {coef2[1]:.2f} Ca(ClO3)2 + {coef3[0]:.2f} Na2SO4 -> {coef2[1]:.2f} CaSO4 + {coef3[1]:.2f} NaClO3\n')