import math


# Definir la funcion f(x) = tan(pi * x) - 6
def f(x):
    return math.tan(math.pi * x) - 6


# Metodo de la regla falsa
def regla_falsa(f, x0, x1, iteraciones):
    tabla = []

    for i in range(1, iteraciones + 1):
        # Calcular el punto de interseccion
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        # Calcular el error relativo
        error_relativo = abs((x2 - x1) / x2)

        # Guardar la iteracion en la tabla
        tabla.append([i, x0, x1, x2, f(x2), error_relativo])

        # Imprimir los resultados de la iteracion
        print(
            f"Iteracion {i}: x0 = {x0:.5f}, x1 = {x1:.5f}, x2 = {x2:.5f}, f(x2) = {f(x2):.5f}, error relativo = {error_relativo:.5f}")

        # Determinar el siguiente intervalo
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

    return tabla


# Valores iniciales y numero de iteraciones
x0 = 0
x1 = 0.48
iteraciones = 10

# Ejecutar el metodo de la regla falsa
resultados = regla_falsa(f, x0, x1, iteraciones)
