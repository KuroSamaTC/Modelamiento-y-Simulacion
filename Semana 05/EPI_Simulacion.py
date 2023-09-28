## Examen Parcial I - Diseño de un CSTR Isotermico
# Autores: - Bruno Fernando Reyes Iglesias
#          - Alfredo Manuel Blanco Villacorta
import sympy as sp
print('EXAMEN PARCIAL I - DISEÑO DE UN CSTR ISOTERMICO\n')
## DATOS
# Reaccion: A + B <=> C + D
# A : CH3COOC2H5 , B : C4H9OH , C : CH3COOC4H9 , D : C2H5OH
T = 300 # K
v = 0.04 # dm^3/s
Kc = 1.08
kA = 9*10**-5 # dm^3/mol.s
CA0 = 7.72 # mol/dm^3
## SOLUCION
X = sp.symbols('X')
# Estequiometria
CA = CA0*(1-X)
CB = CA0*(1-X)
CC = CA0*(X)
CD = CA0*(X)
FA0 = CA0*v
# Cinetica
rA = -kA*(CA*CB-CC*CD/Kc)
# Balance molar
V = FA0*X/(-rA)
# Conversion
xeq = sp.solve(-rA, X)
xeq = float(xeq[0])
x = 0.70*xeq
# Volumen CSTR
V = V.subs(X,x)
# Reporte
print('Condiciones de operacion:')
print(f'   T = {T:.2f} °C')
print(f'   v = {v:.2f} dm^3/s')
print(f' CA0 = {CA0:.2f} mol/dm^3')
print('Conversion de equilibrio:')
print(f' Xeq = {xeq:.2f}')
print(f'El volumen del CSTR sera:')
print(f'   V = {V:.4g} dm^3')