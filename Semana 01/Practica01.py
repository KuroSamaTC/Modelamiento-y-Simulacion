## Practica 1 - Introduccion al software de calculo
# Autor: Bruno Fernando Reyes Iglesias
print('PRACTICA 1 - INTRODUCCION AL SOFTWARE DE CALCULO')
## PROBLEMA 1
print('\nPROBLEMA 1\n')
# a. Condiciones normales (25 C, 1 atm)
print('a. Condiciones normales (25 C, 1 atm)')
P  = 1 # atm
T  = 25+273.15 # K
R  = 0.08205746 # atm.L/mol.K
Vm = R*T/P # L/mol
print('Presion = {:1.6g} atm'.format(P))
print('Temperatura = {:1.6g} K'.format(T))
print('Volumen Molar = {:1.6g} L/mol'.format(Vm))
# b. Condiciones estandar (0 C, 1 atm)
print('b. Condiciones estandar (0 C, 1 atm)')
P  = 1 # atm
T  = 273.15 # K
R  = 0.08205746 # atm.L/mol.K
Vm = R*T/P # L/mol
print('Presion = {:1.6g} atm'.format(P))
print('Temperatura = {:1.6g} K'.format(T))
print('Volumen Molar = {:1.6g} L/mol'.format(Vm))
# c. Condiciones (1000 C, 1 atm)
print('c. Condiciones (1000 C, 1 atm)')
P  = 1 # atm
T  = 1000+273.15 # K
R  = 0.08205746 # atm.L/mol.K
Vm = R*T/P # L/mol
print('Presion = {:1.6g} atm'.format(P))
print('Temperatura = {:1.6g} K'.format(T))
print('Volumen Molar = {:1.6g} L/mol'.format(Vm))
## PROBLEMA 2
print('\nPROBLEMA 2\n')
# Peso molecular del SO2
PM_S = 32 # g/mol
PM_O = 16 # g/mol
PM_SO2 = PM_S+2*PM_O # g/mol
print('Peso molecular del SO2 = {:1.6g} g/mol'.format(PM_SO2))
# Concentracion del SO2
Conc_SO2 = 480 # ug/m^3
Conc_SO2 = Conc_SO2*(10**-6)/(10**3) # g/L
print('Concentracion de SO2 = {:1.6g} g/L'.format(Conc_SO2))
# Moles de SO2
V_air = 1 # L
n_SO2 = Conc_SO2*V_air/PM_SO2 # mol
print('Moles de SO2 = {:1.6g} mol'.format(n_SO2))
# Volumen de SO2
P = 1 # atm
T = 30+273.15 # K
R = 0.08205746 # atm.L/mol.K
V_SO2 = n_SO2*R*T/P # L
print('Volumen de SO2 = {:1.6g} L'.format(V_SO2))
# ppm de SO2
ppm_SO2 = V_SO2/V_air*10**6
print('ppm de SO2 = {:1.6g}'.format(ppm_SO2))
## PROBLEMA 3
print('\nPROBLEMA 3\n')
# Peso molecular del NO
PM_N = 14 # g/mol
PM_O = 16 # g/mol
PM_NO = PM_N+PM_O # g/mol
print('Peso molecular del NO = {:1.6g} g/mol'.format(PM_NO))
# Concentracion del NO
Conc_NO = 40 # ug/m^3
Conc_NO = Conc_NO*(10**-6)/(10**3) # g/L
print('Concentracion de NO = {:1.6g} g/L'.format(Conc_NO))
# Moles de NO
V_air = 1 # L
n_NO = Conc_NO*V_air/PM_NO # mol
print('Moles de NO = {:1.6g} mol'.format(n_NO))
# Volumen de NO
P = 750 # mmHg
T = 25+273.15 # K
R = 62.36367 # L.mmHg/mol.K
V_NO = n_NO*R*T/P # L
print('Volumen de NO = {:1.6g} L'.format(V_NO))
# ppm de NO
ppm_NO = V_NO/V_air*10**6
print('ppm de NO = {:1.6g}'.format(ppm_NO))
## PROBLEMA 4
print('\nPROBLEMA 4\n')
# Volumen del aire en el laboratorio
A = 5 # m
L = 10 # m
H = 3 # m
V_N2_bot = 7*25 # L
V_lab = A*L*H # m^3
V_air = V_lab*(10**3)-V_N2_bot # L
print('Volumen del aire en el laboratorio = {:1.6g} L'.format(V_air))
# Composicion del aire en laboratorio
# Condiciones
P_lab = 1 # atm
P_bot = 200 # atm
T = 25+273.15 # K
R = 0.08205746 # atm.L/mol.K
V_O2 = 0.21*V_air # L
print('Volumen de O2 en laboratorio = {:1.6g} L'.format(V_O2))
V_N2_lab = 0.79*V_air # L
print('Volumen de N2 en laboratorio = {:1.6g} L'.format(V_N2_lab))
print('Volumen de N2 en botellas = {:1.6g} L'.format(V_N2_bot))
n_O2 = P_lab*V_O2/(R*T) # mol
print('Moles de O2 en laboratorio = {:1.6g} mol'.format(n_O2))
n_N2_lab = P_lab*V_N2_lab/(R*T) # mol
print('Moles de N2 en laboratorio = {:1.6g} mol'.format(n_N2_lab))
n_N2_bot = P_bot*V_N2_bot/(R*T) # mol
print('Moles de N2 en botellas = {:1.6g} mol'.format(n_N2_bot))
# Porcentaje de O2 luego de la fuga
n_tot = n_O2+n_N2_lab+n_N2_bot # mol
Conc_O2 = n_O2/n_tot*100 # #
print('Concentracion de O2 = {:1.6g} %'.format(Conc_O2))
if Conc_O2 < 18:
    print('///// ALERTA ///// NIVEL DE O2 BAJO - RIESGO PARA LA SALUD\n')
else:
    print('NIVEL DE O2 NORMAL\n')