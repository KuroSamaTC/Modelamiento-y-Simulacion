## Practica 3 - Modelizacion en base a datos experimentales
# Autor: Bruno Fernando Reyes Iglesias
print('PRACTICA 3 - MODELIZACION EN BASE A DATOS EXPERIMENTALES')
## Uso de scipy para ajuste de curva con datos experimentales
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pandas import DataFrame
## PROBLEMA 1
print('\nProblema 1\n')
# Datos
Pre=np.array([88.9,101.6,104.1,139.7,132.1,94.0,116.8,121.9,99.1])
Flw=np.array([114.7,172.0,152.9,269.0,206.4,161.4,175.8,239.0,130.0])
Table=DataFrame({'Precipitacion (cm)':Pre,'Flujo (m^3/s)':Flw})
print(Table)
# Definir el modelo de ajuste
def modelo(x,a,b):
    return a+b*x
# Ajuste de datos
popt,pcov=curve_fit(modelo,Pre,Flw)
# Recuperacion de parametros
a,b=popt
# Calculo de R^2
pvals=modelo(Pre,*popt)
meany=np.mean(Flw)
TSS=np.sum((Flw-meany)**2)
RSS=np.sum((Flw-pvals)**2)
r_sqr=1-(RSS/TSS)
# Resultados
print('\nModelo de ajuste:')
print('   f(x) = a + b * x')
print('\nParametros de ajuste:')
print('   a = %.4f' % (a))
print('   b = %.4f' % (b))
print('   R^2 = %.4f' % (r_sqr))
# Grafica de datos y curva de ajuste
plt.figure(1)
plt.scatter(Pre,Flw,label='Data')
plt.plot(Pre,modelo(Pre,*popt),'-r',label='Curva de ajuste')
plt.xlabel('Precipitacion (cm)')
plt.ylabel('Flujo (m^3/s)')
plt.title('Problema 1')
plt.legend()
plt.grid()
# Nivel de clorofila cuando p = 15
Flw120=modelo(120,*popt)
print('\nEl flujo cuando la precipitacion es 120 cm es: %.4g m^3/s\n' % (Flw120))
## PROBLEMA 2
print('\nProblema 2\n')
# Datos
p=np.array([4.5,8.0,5.5,39.0,19.5,17.5,21.0])
c=np.array([0.8,2.0,1.2,11.0,4.4,3.8,5.5])
Table=DataFrame({'Fosforo, p (mg/m^3)':p,'Clorofila, c (mg/m^3)':c})
print(Table)
# Definir el modelo de ajuste
def modelo(x,a,b):
    return a+b*x
# Ajuste de datos
popt,pcov=curve_fit(modelo,p,c)
# Recuperacion de parametros
a,b=popt
# Calculo de R^2
pvals=modelo(p,*popt)
meany=np.mean(c)
TSS=np.sum((c-meany)**2)
RSS=np.sum((c-pvals)**2)
r_sqr=1-(RSS/TSS)
# Resultados
print('\nModelo de ajuste:')
print('   f(x) = a + b * x')
print('\nParametros de ajuste:')
print('   a = %.4f' % (a))
print('   b = %.4f' % (b))
print('   R^2 = %.4f' % (r_sqr))
# Grafica de datos y curva de ajuste
plt.figure(2)
plt.scatter(p,c,label='Data')
plt.plot(p,modelo(p,*popt),'-r',label='Curva de ajuste')
plt.xlabel('Fosforo mg/cm^3')
plt.ylabel('Clorofila mg/cm^3')
plt.title('Problema 2')
plt.legend()
plt.grid()
# Nivel de clorofila cuando p = 15
c15=modelo(15,*popt)
print('\nEl nivel de clorofila cuando p = 15 mg/m^3 es: %.4g\n' % (c15))
## PROBLEMA 3
print('\nProblema 3\n')
# Datos
t=np.array([0.5,1,2,3,4,5,6,7,8,9])
P=np.array([7,5.2,3.8,3.2,2.5,2.1,1.8,1.5,1.2,1.1])
Table=DataFrame({'Tiempo , hrs':t,'Poblacion':P})
print(Table)
# Definir la funcion
def modelo(t,A,B,C):
    return A*np.exp(-1.5*t)+B*np.exp(-0.3*t)+C*np.exp(-0.05*t)
# Ajuste de datos
popt,pcov=curve_fit(modelo,t,P)
# Recuperacion de parametros
A,B,C=popt
# Calculo de R^2
pvals=modelo(t,*popt)
meany=np.mean(P)
TSS=np.sum((P-meany)**2)
RSS=np.sum((P-pvals)**2)
r_sqr=1-(RSS/TSS)
# Resultados
print('\nModelo de ajuste:')
print('   P(t) = A*exp(-1.5*t)+B*exp(-0.3*t)+C*exp(-0.05*t)')
print('\nParametros de ajuste:')
print('   A = %.4f' % (A))
print('   B = %.4f' % (B))
print('   C = %.4f' % (C))
print('   R^2 = %.4f' % (r_sqr))
# Grafica de datos y curva de ajuste
plt.figure(3)
plt.scatter(t,P,label='Data')
plt.plot(t,modelo(t,*popt),'-r',label='Curva de ajuste')
plt.xlabel('Tiempo (hrs)')
plt.ylabel('Poblacion')
plt.title('Problema 3')
plt.legend()
plt.grid()
# Poblacion incial
print('\nPoblacion incial de cada microorganismo, t = 0:')
print('   A = %.4g' % (A))
print('   B = %.4g' % (B))
print('   C = %.4g' % (C))
## Mantener los graficos abiertos
plt.show()
