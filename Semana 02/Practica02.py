## Practica 2 - Columna de destilacion
# Autor: Bruno Fernando Reyes Iglesias
print('PRACTICA 2 - PROCESOS DE SEPARACION: COLUMNA DE DESTILACION')
## Metodo de McCabe-Thiele
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
F = 100 # Flujo molar total de la alimentacion
xf = 0.55 # Fraccion molar de la alimentacion
q = 0.4 # La fraccion de líquido en la alimentacion
xd = 0.9 # Fraccion molar del destilado 
xb = 0.1 # Fraccion molar del fondo
ratio = 1.1 # Relacion de reflujo
a = 2.45 # La volatilidad relativa
## Balance alrededor de la columna
D = F*(xf-xb)/(xd-xb) # Flujo molar del destilado
B = F-D # Flujo molar del fondo
print('Flujo molar del destilado: %1.6g' % (D))
print('Flujo molar del fondo: %1.6g' % (B))
## Grafica ELV
plt.figure(figsize=(8, 6))
x = np.linspace(0,1) # Fraccion mol del componente ligero en la fase líquida
plt.plot(x, x, label='Linea de 45 grados', linestyle='--', color='cyan')
y = a*x/(1+x*(a-1)) # Fraccion mol del componente ligero en la fase vapor
plt.plot(x, y, label='Curva de Equilibrio', color='red') # Grafica y en funcion de x en ELV
## Ecuacion linea q (y=m*x+n)
m = q/(q-1)
n = xf-m*xf
Zf = -n*(q-1)
## Interseccion linea-q con ELV
x0 = sp.symbols('x0')
f = sp.Eq(a*x0/(1+x0*(a-1)),m*x0+n)
sys_sol = sp.solve(f,x0)
x0 = [x for x in sys_sol if x>=0]
x0 = x0[0]
x0 = float(x0)
y0 = m*x0+n
## Linea Operacion Enriquecimiento (LOE)
# [y=(R/(R+1))X+Xd/(R+1)]
m1,n1 = sp.symbols('m1 n1')
f1 = sp.Eq(m1*x0+n1*xd,y0)
f2 = sp.Eq(m1*xd+n1*xd,xd)
sys_sol = sp.solve((f1,f2),(m1,n1))
m1 = sys_sol[m1]
m1 = float(m1)
n1 = sys_sol[n1]
n1 = float(n1)
# m=R/(R+1)
r = m1/(1-m1) # Reflujo minimo
R = ratio*r # Reflujo real
m2 = R/(R+1)
n2 = xd-m2*xd
## interseccion linea q y LOE
xz,yz = sp.symbols('xz yz')
a1 = sp.Eq(m*xz+n,yz)
a2 = sp.Eq(m2*xz+n2,yz)
sys_sol = sp.solve((a1,a2),(xz,yz))
xz = sys_sol[xz]
xz = float(xz)
yz = sys_sol[yz]
yz = float(yz)
## Graficamos linea q
x2 = np.linspace(xz,xf)
y2 = x2*m+n
plt.plot(x2, y2, label='Linea q', color='green')
## Grafica LOE
x3 = np.linspace(xz,xd)
y3 = m2*x3+n2
plt.plot(x3, y3, label='LOE', color='blue')
## Linea Operacion Agotamiento (LOA) 
m3,n3 = sp.symbols('m3 n3')
f3 = sp.Eq(m3*xb+n3,xb)
f4 = sp.Eq(m3*xz+n3,yz)
sys_sol = sp.solve((f3,f4),(m3,n3))
m3 = sys_sol[m3]
m3 = float(m3)
n3 = sys_sol[n3]
n3 = float(n3)
# Grafica LOA
x4 = np.linspace(xb,xz)
y4 = m3*x4+n3
plt.plot(x4, y4, label='LOA', color='blue')
t = xd
t1 = xd
p = xd
## Graficamos etapas
i = 0
x,y = sp.symbols('x y')
while t>xb:
    f1 = sp.Eq(y,a*x/(1+x*(a-1)))
    f2 = sp.Eq(y,t1+0*x)
    h = sp.solve((f1,f2),(x,y))
    x_sol = h[0][0]
    y_sol = h[0][1]
    plt.plot([x_sol,t],[p,p], color='magenta') # horizontal
    t = x_sol
    if t>xz:
        p = R*x/(R+1)+xd/(R+1)
        p = float(p.subs(x,x_sol))
        plt.plot([x_sol,x_sol],[p,y_sol], color='magenta')
        t1 = p
        i = i+1
    elif t<xz:
        p = x*(yz-xb)/(xz-xb)-xb*(yz-xb)/(xz-xb)+xb
        p = float(p.subs(x,x_sol))
        plt.plot([x_sol,x_sol],[p,y_sol], color='magenta')
        t1 = p
        i = i+1
plt.xlabel('x (Composicion del liquido)')
plt.ylabel('y (Composicion del vapor)')
plt.title('Diagrama McCabe-Thiele')
plt.legend()
plt.grid(True)
print('El N°. de las etapas requeridas es: %i' % (i))
print('El N°. de bandejas requeridas es: %i' % (i-1))
plt.show()
