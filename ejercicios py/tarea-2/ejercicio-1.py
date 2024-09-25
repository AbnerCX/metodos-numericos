import math

def biseccion(f, a, b, aprox):
    
    if f(a) * f(b) >= 0:
        
        raise ValueError("ERROR: La funcion debe cambiar de signo en el intervalo dado.")

    iteracion = 1

    while (b - a) / 2 > aprox:
        
        mn = (a + b) / 2
        
        print(f"Iteración {iteracion}: a = {a} ---- b = {b} ----- mn = {mn} ----- f(mn) = {f(mn)}")
        
        if f(mn) == 0:
            return mn  # Encontramos la raiz exacta
        elif f(a) * f(mn) < 0:
            b = mn  # La raiz esta en [a, c]
        else:
            a = mn  # La raiz esta en [c, b]
        
        iteracion += 1  # Incrementa el contador

    return (a + b) / 2  # Raiz aproximada


def f1(x):
    return x - 2**(-x)

def f2(x):
    return math.exp(x) - x**2 + 3*x - 2

def f3(x):
    return 2 * x * math.cos(2 * x) - (x + 1)**2

def ejercicio_1():
    a = 0 
    b = 1
    
    aprox = 1e-5
    
    print("Evaluando ejercicio 1) x − 2^−x = 0 en [0, 1]:")
    
    raiz_1 = biseccion(f1, a, b, aprox)
    
    print(f"La raiz es aproximadamente: {raiz_1}\n")

def ejercicio_2():
    a= 0 
    b = 1
    
    aprox = 1e-5
    
    print("Evaluando ejercicio 2) e^x − x^2 + 3x − 2 = 0 en [0, 1]:")
    
    raiz_2 = biseccion(f2, a, b, aprox)
    
    print(f"La raiz es aproximadamente: {raiz_2}\n")

def ejercicio_3():
    aprox = 1e-5

    print("Evaluando ejercicio 3) 2x cos(2x) − (x + 1)^2 = 0 en [−3, −2]:")
    
    raiz_3_a = biseccion(f3, -3, -2, aprox)
    
    print(f"La raiz en el intervalo [-3, -2] es aproximadamente: {raiz_3_a}\n")

    print("Evaluando ejercicio 3) 2x cos(2x) − (x + 1)^2 = 0 en [−1, 0]:")
    
    raiz_3_b = biseccion(f3, -1, 0, aprox)
    
    print(f"La raiz en el intervalo [-1, 0] es aproximadamente: {raiz_3_b}\n")

if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()