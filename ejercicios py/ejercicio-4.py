import numpy as np
import sys

def raiz_de_ecuacion_cuadratica():
    while True:
        try:
            a = float(input("Introduce el valor de a: "))
            if not a:
                print("No se puede dividir entre 0.")
                sys.exit(0)
            
            b = float(input("Introduce el valor de b: "))
            c = float(input("Introduce el valor de c: "))

            agrupacion = b**2 - 4 * a * c
            if agrupacion < 0:
                print("La ecuacion no tiene raices reales.")
                sys.exit(0)

            x1 = (-b + np.sqrt(agrupacion)) / (2 * a)
            x2 = (-b - np.sqrt(agrupacion)) / (2 * a)
            
            print(f"Valor de x1: {x1}")
            print(f"Valor de x2: {x2}")
        
        except ValueError:
            print("Error de valor, porfavor vuelve a intentarlo.")
            
        repetir = int(input("¿Deseas volver al inicio? \n 1- Si \n 2- No \n"))
        
        if repetir == 1:
            continue
        else:
            break

raiz_de_ecuacion_cuadratica()