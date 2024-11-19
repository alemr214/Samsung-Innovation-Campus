import numpy as np


# Crear una matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Acceder a un elemento de la matriz
print("Elemento en la fila 1, columna 1:", matriz[0, 0])
print("Elemento en la fila 2, columna 3:", matriz[1, 2])

# Elemento en la fila completa
print("Primera fila: ", matriz[0, :])


# Acceder a una columna completa
print("Segunda columna: ", matriz[:, 1])

# Acceder a un subconjunto de la matriz
print("Submatriz:\n (fila 1 y 2, columnas 1 y 2)\n", matriz[0:-1, 0:-1])
