import numpy as np
import matplotlib.pyplot as plt


# Definir la función
def f(x):
    return 3 * x + 1


# Crear el rango de valores de x
x = np.linspace(-1, 1, 100)
y = f(x)

# Crear la gráfica
plt.figure(figsize=(6, 6))
plt.plot(x, y, color="blue", label=r"$f(x) = 3x + 1$")

# Dibujar puntos y anotaciones
plt.plot(0, f(0), "ko")  # Punto en el intercepto con y
plt.plot(-1 / 3, 0, "ko")  # Punto en el intercepto con x

# Añadir líneas de referencia
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# Anotaciones
plt.text(0.1, 1, "1", fontsize=12, verticalalignment="center")
plt.text(-1 / 3, -0.1, r"$-\frac{1}{3}$", fontsize=12, horizontalalignment="center")
plt.text(0.05, 1.2, r"$f(x) = 3x + 1$", fontsize=15)

# Etiquetas y límites
plt.xlim(-1, 1)
plt.ylim(-1, 4)
plt.xlabel(r"$x$", fontsize=12)
plt.ylabel(r"$y$", fontsize=12)

plt.show()
