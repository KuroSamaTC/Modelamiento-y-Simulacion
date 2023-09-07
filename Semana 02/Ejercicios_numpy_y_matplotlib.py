## Introduccion a la libreria NumPy
# Autor: Reyes Iglesias Bruno Fernando
## Problema 1
print('\nProblema 1\n')
# Importar la biblioteca NumPy
import numpy as np
# Generar una matriz de 4x5 con ceros y unos
matriz_ceros = np.zeros((2, 5), dtype=int)
matriz_unos = np.ones((2, 5), dtype=int)
matriz = np.vstack((matriz_ceros, matriz_unos))
# Imprimir la matriz
print(matriz)
## Problema 2
print('\nProblema 2\n')
# Importar la biblioteca NumPy
import numpy as np
# Generar vector con diferentes numeros
vector=[32,4,81,np.exp(2.5),np.cos(np.pi/3),14]
print(vector)
## Problema 3
print('\nProblema 3\n')
# Importar la biblioteca NumPy
import numpy as np
# Crear un vector de 33 elementos con números impares
vector=[]
for i in range(1, 35):
    if i % 2 != 0:
        vector.append(i)
# Convertir el vector en vector columna
vector=np.reshape(vector,[len(vector),1])
# Imprimir el vector
print(vector)
print('\nProblema 4\n')
# Importar la biblioteca NumPy
import numpy as np
# Crear el vector A
A=np.random.uniform(0,101,(4, 6))
# Imprimir la matriz
print(A)

