# Función de registro
def registro():
    registros = []  # Inicializa nuestra lista donde se guardaran los registros de personas y altura.

    while len(registros) < 4:  # Ciclo While para que solo se almacenen 4 personas con su respectiva altura.

        nombre = input("Introduce el nombre que deseas agregar: ")  # Captura del nombre.
        altura = float(input("Introduce la altura que deseas agregar: "))  # Captura de la altura.

        registros.append({'nombre': nombre, 'altura': altura})  # Los registros se almacenan dentro de un diccionario que se almacena en nuestra lista.

    return registros  # Se retorna el valor de nuestra lista.


def max_altura(registros):  # Se crea una nueva funcion que recibe como parametro nuestra lista.
    altura_maxima = 0  # Inicializa la variable para almacenar la altura maxima.

    for persona in registros:  # Recorre cada persona en la lista de registros.
        height = persona['altura']  # Captura la altura de la persona actual.
        if height > altura_maxima:  # Compara si la altura actual es mayor que la altura maxima registrada.
            altura_maxima = height  # Si es mayor, actualiza la altura maxima.

    return altura_maxima  # Retorna la altura maxima encontrada.


def mostrar_maximo(altura_maxima, registros):  # Define una funcion que recibe la altura máxima y la lista de registros.
    for persona in registros:  # Recorre cada persona en la lista de registros.
        if persona['altura'] == altura_maxima:  # Verifica si la altura de la persona es igual a la altura maxima.
            print(f"La persona más alta es {persona['nombre']} con una altura de {persona['altura']} metros.")  # Imprime el nombre y la altura de la persona mas alta.


reg = registro()  # Llama a la funcion de registro para obtener la lista de personas y sus alturas.
altura = max_altura(reg)  # Llama a la funcion para encontrar la altura maxima.
mostrar_maximo(altura, reg)  # Llama a la funcion para mostrar a la persona con la altura maxima.
