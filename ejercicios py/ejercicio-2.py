def registro():
    registro = []

    while len(registro) < 8:
        nombres = input("Introduce el nombre de la persona: ")
        registro.append(nombres)
        altura =  float(input("Introduce la altura de la persona: "))
        registro.append(altura)
        
    return registro


def altura_maxima(registro):
    indice_max = 0
    max_altura = registro[1]

    for indice in range(3, len(registro), 2):
        altura = registro[indice]
        if altura > max_altura:
            max_altura = altura
            indice_max = indice
    
    return indice_max

def main():
    
    datos = registro()

    indice_max = altura_maxima(datos)

    nombre_max = datos[indice_max - 1]
    altura_max = datos[indice_max]

    print(f"Nombre con la altura maxima: {nombre_max} y su altura maxima es de: {altura_max}")


main()