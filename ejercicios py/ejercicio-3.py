import numpy as np
import time
import matplotlib.pyplot as plt


# Funcion para la multiplicacion de matrices en Python puro
def multiplicar_matrices_python(A, B):
    n = len(A)
    resultado = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            suma = 0.0
            for k in range(n):
                suma += A[i, k] * B[k, j]
            resultado[i, j] = suma
    return resultado

# Funcion para medir el tiempo de ejecucion de la multiplicacion de matrices
def medir_tiempo(longitud_matriz):
    A = np.random.rand(longitud_matriz, longitud_matriz)
    B = np.random.rand(longitud_matriz, longitud_matriz)
    inicio = time.time()
    multiplicar_matrices_python(A, B)
    tiempo_python = time.time() - inicio
    inicio = time.time()
    np.dot(A, B)
    tiempo_numpy = time.time() - inicio
    return tiempo_python, tiempo_numpy

# Funcion principal para probar diferentes longitudes de matrices
def principal():
    longitudes = [100, 500, 1000, 1500, 2000, 2500]
    tiempos_python = []
    tiempos_numpy = []
    
    for longitud in longitudes:
        print(f"Probando longitud {longitud}...")
        tiempo_python, tiempo_numpy = medir_tiempo(longitud)
        tiempos_python.append(tiempo_python)
        tiempos_numpy.append(tiempo_numpy)
    
    # Mostrar resultados en grafico
    plt.figure(figsize=(10, 6))
    plt.plot(longitudes, tiempos_python, label='Python', marker='o')
    plt.plot(longitudes, tiempos_numpy, label='Numpy', marker='o')
    plt.xlabel('Longitud de la Matriz (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparacion de Tiempo de Multiplicacion de Matrices')
    plt.legend()
    plt.grid(True)
    plt.show()


principal()
