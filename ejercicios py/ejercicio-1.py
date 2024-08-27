
def epsilon():
    eps = 0.1

    while (1.0 + eps) != 1.0:
        eps /= 2

    print("El valor de epsilon de la maquina es:", eps)

epsilon()
