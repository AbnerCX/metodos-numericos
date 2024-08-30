# Funcion para encontrar el valor de epsilon de la maquina
def epsilon():
    eps = 0.1  # Inicializa la variable epsilon con un valor inicial de 0.1

    # Ciclo While para encontrar el valor mas pequeno de epsilon tal que 1.0 + eps sea distinto de 1.0
    while (1.0 + eps) != 1.0:
        eps /= 2  # Divide el valor de epsilon por 2 en cada iteracion
    # Cuando el ciclo termina, significa que eps es tan pequeno que 1.0 + eps ya no se distingue de 1.0
    print("El valor de epsilon de la maquina es:", eps)  # Imprime el valor final de epsilon

# Llamada a la funcion epsilon para ejecutar el programa
epsilon()
