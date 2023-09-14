%% Practica 02 - Columna de destilacion
% Autor: Reyes Iglesias Bruno Fernando
%% Metodo de McCabe-Thiele
F = 100; % Flujo molar total de la alimentacion
xf =0.55; % Fraccion molar de la alimentacion
q =0.4; % La fraccion de líquido en la alimentacion
xd =0.9; % Fraccion molar del destilado 
xb =0.1; % Fraccion molar del fondo
ratio = 1.1; % Relacion de reflujo
a = 2.45; % La volatilidad relativa
%% Balance alrededor de la columna
D = F.*(xf-xb)./(xd-xb); % Flujo molar del destilado
B = F-D; % Flujo molar del fondo
fprintf('Flujo molar del destilado: %1.6g\n',D);
fprintf('Flujo molar del fondo: %1.6g\n',B);
%% Grafica ELV
x = linspace(0,1); % Fraccion mol del componente ligero en la fase líquida
plot(x,x,'--c','DisplayName','Linea de 45 grados');
title('Diagrama de McCabe-Thiele')
xlabel('Composicion del liquido')
ylabel('Composicion del vapor')
grid on
hold on
y = a.*x./(1+x.*(a-1)); % Fraccion mol del componente ligero en la fase vapor
plot(x,y,'r','DisplayName','Curva de equilibrio'); % Grafica y en funcion de x en ELV
%% Ecuacion linea q (y=m*x+n)
m = q./(q-1);
n = xf-m.*xf;
Zf = -n.*(q-1);
%% Interseccion linea-q con ELV
syms x0
f = a*x0/(1+x0*(a-1))==m*x0+n;
[x0] = solve(f);
x0 = eval(x0);
x0 = x0( x0>=0 );
y0 = m*x0+n;
%% Linea Operacion Enriquecimiento (LOE)
% [y=(R/(R+1))X+Xd/(R+1)]
syms m1 n1
f1 = m1*x0+n1*xd==y0;
f2 = m1*xd+n1*xd==xd;
[m1,n1] = solve(f1,f2);
m1 = eval(m1);
n1 = eval(n1);
% m=R/(R+1)
r = m1/(1-m1); % Reflujo minimo
R = ratio*r; % Reflujo real
m2 = R/(R+1);
n2 = xd-m2*xd;
%% interseccion linea q y LOE 
syms xz yz
a1 = m*xz+n==yz;
a2 = m2*xz+n2==yz;
[xz, yz]=solve(a1,a2);
xz = eval(xz);
%% Graficamos linea q
x2 = linspace(xz,xf);
y2 = x2.*m+n;
plot(x2,y2,'g','DisplayName','Linea q');
%% Grafica LOE
x3 = linspace(xz,xd);
y3 = m2.*x3+n2;
plot(x3,y3,'b','DisplayName','LOE');
%% Linea Operacion Agotamiento (LOA) 
syms m3 n3
f3 = m3*xb+n3==xb;
f4 = m3*xz+n3==yz;
[m3,n3] = solve(f3,f4);
m3 = eval(m3);
n3 = eval(n3);
% Grafica LOA
x4 = linspace(xb,xz);
y4 = m3.*x4+n3;
plot(x4,y4,'b','DisplayName','LOA');
legend("Position", [0.60952,0.14883,0.275,0.21892])
legend AutoUpdate off
t = xd; t1 = xd; p = xd;
%% Graficamos etapas
i = 0;
syms x y
while t>xb
    h = solve(y==a*x/(1+x*(a-1)), y==t1+0*x);
    plot([h.x,t],[p,p],'m') % Horizontal
    t = h.x;
    if t>xz
        p = subs(R*x/(R+1)+xd/(R+1),h.x);
        plot([h.x,h.x],[p,h.y],'m') 
        t1 = p;
        i = i+1;
    elseif t<xz
        p = subs(x.*(yz-xb)/(xz-xb)-xb*(yz-xb)/(xz-xb)+xb,h.x);
        plot([h.x,h.x],[p,h.y],'m') 
        t1 = p;
        i = i+1;
    end
end
fprintf('El N°. de las etapas requeridas es: %d.\n',i);
fprintf('El N°. de bandejas requeridas es: %d.\n',i-1);