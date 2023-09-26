%% Practica 3 - Modelizacion de datos experimentales
% Autor: Reyes Iglesias Bruno Fernando
clear, clc, close all
fprintf('PRACTICA 3 - MODELIZACION DE DATOS EXPERIMENTALES \n\n')
%% PROBLEMA 1
fprintf('\nPROBLEMA 1 \n')
% Datos: Precipitación cm (Pre), Flujo m^3/s (Flw)
Pre=[88.9;101.6;104.1;139.7;132.1;94.0;116.8;121.9;99.1];
Flw=[114.7;172.0;152.9;269.0;206.4;161.4;175.8;239.0;130.0];
Tab=table(Pre,Flw,VariableNames={'Precipitacion, cm','Flujo, m^3/s'});
disp(Tab)
% a. Graficar los datos
Fig1=figure('Name','Problema 1','NumberTitle','off');
plot(Pre,Flw,'ob')
hold on
% b. Ajuste a una linea recta. Sobreponga la linea de su grafica
[F,gof]=fit(Pre,Flw,'poly1');
disp(F); disp(gof);
plot(F,Pre,Flw)
title('Datos y Curva de ajuste')
xlabel('Precipitacion, cm')
ylabel('Flujo, m^3/s')
grid on
hold off
% c. Predecir el flujo de agua anual si la precipitacion es de 120 cm
optimpar=coeffvalues(F);
Flw120=polyval(optimpar,120);
fprintf('El flujo cuando la precipitacion es 120 cm sera: %1.4g m^3/s \n', Flw120)
%% Problema 2
fprintf('\nPROBLEMA 2 \n')
% Datos:
p=[4.5;8.0;5.5;39.0;19.5;17.5;21.0];
c=[0.8;2.0;1.2;11.0;4.4;3.8;5.5];
Tab=table(p,c,VariableNames={'Fosforo (p)','Clorofila (c)'});
disp(Tab)
% Encontrar una curva de ajuste y graficar los datos
[F,gof]=fit(p,c,'poly1');
disp(F); disp(gof);
Fig2=figure('Name','Problema 2','NumberTitle','off');
plot(F,p,c)
title('Datos y Curva de ajuste')
xlabel('p')
ylabel('c')
grid on
% Predecir lel nivel de clorofila cuando p = 15 mg/cm^3
optimpar=coeffvalues(F);
c15=polyval(optimpar,120); % Flujo a 120 cm
fprintf('El nivel de clorofila cuando p = 15 mg/cm^3 es: %1.4g \n', c15)
%% Problema 3
fprintf('\nPROBLEMA 3 \n')
% Datos:
t=[0.5;1;2;3;4;5;6;7;8;9];
P=[7;5.2;3.8;3.2;2.5;2.1;1.8;1.5;1.2;1.1];
Tab=table(t,P,VariableNames={'Tiempo (hrs)','Poblacion'});
disp(Tab)
% Encontrar una curva de ajuste de acuerdo al modelo dado y graficar los datos
model=fittype('A.*exp(-1.5.*t)+B.*exp(-0.3.*t)+C.*exp(-0.05.*t)','dependent','P','independent','t','coefficients',{'A','B','C'});
[F,gof]=fit(t,P,model,'StartPoint',[1,1,1]); % StartPoint para indicar un valor incial de calculo (no es necesario)
disp(F); disp(gof);
Fig3=figure('Name','Problema 3','NumberTitle','off');
plot(F,t,P)
title('Datos y Curva de ajuste')
xlabel('Tiempo, hrs')
ylabel('Poblacion')
grid on
% Poblacion incial A,B,C
optimpar=coeffvalues(F);
A=optimpar(1);
B=optimpar(2);
C=optimpar(3);
fprintf('La poblacion incial de A es: %1.5g \n', A)
fprintf('La poblacion incial de B es: %1.5g \n', B)
fprintf('La poblacion incial de C es: %1.5g \n', C)
