def calcular_calificacion():
    # Paso 1: Introducir clave y nombre del curso
    clave_curso = input("Introduce la clave del curso: ")
    nombre_curso = input("Introduce el nombre del curso: ")

    # Paso 2: Introducir factores de ponderacion
    cuestionarios = float(input("Introduce el factor de ponderacion para los cuestionarios (C): "))
    tareas = float(input("Introduce el factor de ponderacion para las tareas (T): "))
    examen = float(input("Introduce el factor de ponderacion para el examen final (E): "))

    # Paso 3: Introducir calificaciones de los cuestionarios y calcular el promedio
    num_cuestionarios = int(input("Introduce el numero de cuestionarios: "))
    suma_cuestionarios = 0
    
    for x in range(num_cuestionarios):
        nota = float(input(f"Introduce la calificacion del cuestionario {x + 1}: "))
        suma_cuestionarios += nota
    promedio_cuestionarios = suma_cuestionarios / num_cuestionarios

    # Paso 4: Introducir calificaciones de las tareas y calcular el promedio
    num_tareas = int(input("Introduce el numero de tareas: "))
    suma_tareas = 0
    
    for x in range(num_tareas):
        nota = float(input(f"Introduce la calificacion de la tarea {x + 1}: "))
        suma_tareas += nota
    promedio_tareas = suma_tareas / num_tareas

    # Paso 5: Verificar si el curso tiene examen final
    tiene_examen_final = input("¿El curso tiene examen final? (si/no): ").strip().lower()

    if tiene_examen_final == "si":
        # Paso 6: Introducir la calificacion del examen final
        calificacion_examen_final = float(input("Introduce la calificacion del examen final: "))

        # Paso 7: Calcular CP con el examen final
        promedio_final = (cuestionarios * promedio_cuestionarios + tareas * promedio_tareas + examen * calificacion_examen_final) / (cuestionarios + tareas + examen)
    else:
        # Paso 9: Calcular CP sin el examen final
        promedio_final = (cuestionarios * promedio_cuestionarios + tareas * promedio_tareas) / (cuestionarios + tareas)

    # Paso 10: Imprimir resultados
    print(f"\nClave del curso: {clave_curso}")
    print(f"Nombre del curso: {nombre_curso}")
    print(f"Calificacion promedio (CP): {promedio_final:.2f}")

# Datos de prueba
calcular_calificacion()
