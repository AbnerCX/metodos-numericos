import math
def newton_raphson(f, df, x0, tol=1e-5, delta=0.001, max_iter=100):
    iteracion = 0
    while iteracion < max_iter:
        fx = f(x0)
        dfx = df(x0)

        if abs(dfx) < delta:
            print("Derivada pequena")
            return None  # Detiene el programa si la derivada es muy pequeña

        x1 = x0 - fx / dfx

        print(f"Iteracion {iteracion + 1}: x0 = {x0} ---- f(x0) = {fx} ---- f'(x0) = {dfx} ---- x1 = {x1}")

        if abs(x1 - x0) < tol:
            return x1

        x0 = x1
        iteracion += 1

    raise ValueError("El metodo no ha convergido despues de las iteraciones maximas.")


# Funcion f(x) = (x − 2)(x − 7)(x − 2)
def f(x):
    return (x - 2) * (x - 7) * (x - 2)


# Derivada de la funcion f'(x)
def df(x):
    return 3 * x ** 2 - 18 * x + 29


def resolver_newton_raphson():
    x0 = 5.33333333333  # Valor inicial
    tol = 1e-5
    delta = 0.001

    print(f"Aproximando con valor inicial x0 = {x0}:")
    raiz = newton_raphson(f, df, x0, tol, delta)

    if raiz is not None:
        print(f"La raiz aproximada con x0 = {x0} es: {raiz}\n")


if __name__ == "__main__":
    resolver_newton_raphson()
