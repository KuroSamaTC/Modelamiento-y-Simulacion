import sympy as sp
h=sp.symbols('h')
hs=sp.symbols('hs')
k=sp.symbols('k')
f1=k*sp.sqrt(h)
f1_lin=sp.series(f1,h,hs,2)
print(f1_lin)