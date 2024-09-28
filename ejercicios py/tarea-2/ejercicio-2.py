import math
def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    iteracion = 0
    while iteracion < max_iter:
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ValueError("La derivada se ha hecho cero, no se puede continuar con el metodo.")

        x1 = x0 - fx / dfx

        print(f"Iteracion {iteracion + 1}: x0 = {x0} ---- f(x0) = {fx} ---- f'(x0) = {dfx} ---- x1 = {x1}")

        if abs(x1 - x0) < tol:
            return x1

        x0 = x1
        iteracion += 1

    raise ValueError("El metodo no ha convergido despues de las iteraciones maximas.")


# Funcion dada: 4x^2 - e^x - e^(-x) = 0
def f(x):
    return 4 * x ** 2 - math.exp(x) - math.exp(-x)


# Derivada de la funcion
def df(x):
    return 8 * x - math.exp(x) + math.exp(-x)


def resolver_newton_raphson():
    valores_iniciales = [-10, -1, 3, 0, 10]
    tol = 1e-5

    for x0 in valores_iniciales:
        print(f"Aproximando con valor inicial x0 = {x0}:")
        try:
            raiz = newton_raphson(f, df, x0, tol)
            print(f"La raiz aproximada con x0 = {x0} es: {raiz}\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    resolver_newton_raphson()
