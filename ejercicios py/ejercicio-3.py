import numpy as np
import time
import matplotlib.pyplot as plt

# Función para multiplicar dos matrices usando la multiplicación manual
def multiplicacion_matrices_manual(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C

# Función para medir el tiempo de ejecución de la multiplicación manual y numpy
def medir_tiempos(tamaños):
    tiempos_manual = []
    tiempos_numpy = []

    for n in tamaños:
        print(f"Probando tamaño: {n}x{n}")
        
        # Crear matrices aleatorias
        A = np.random.rand(n, n)
        B = np.random.rand(n, n)

        # Medir tiempo para la multiplicación manual
        start = time.time()
        C_manual = multiplicacion_matrices_manual(A.tolist(), B.tolist())
        end = time.time()
        tiempos_manual.append(end - start)

        # Medir tiempo para la multiplicación usando numpy
        start = time.time()
        C_numpy = np.dot(A, B)
        end = time.time()
        tiempos_numpy.append(end - start)

    return tiempos_manual, tiempos_numpy

# Tamaños de las matrices
tamaños = [100, 1000, 2500, 5000, 7500, 10000]

# Medir tiempos
tiempos_manual, tiempos_numpy = medir_tiempos(tamaños)

# Graficar los resultados
plt.figure(figsize=(12, 6))
plt.plot(tamaños, tiempos_manual, label='Multiplicación Manual', marker='o')
plt.plot(tamaños, tiempos_numpy, label='Multiplicación NumPy', marker='o')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Tamaño de la matriz (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempos de ejecución de multiplicación de matrices')
plt.legend()
plt.grid(True)
plt.show()
