# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso  {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada  asignatura en el formato tiene créditos, donde es cada una de las asignaturas del curso, y son sus  créditos. Al final debe mostrar también el número total de créditos del curso.

def DiccCredAsig():
    print("======== Creditos Asignaturas ========")
    cantAsig = int(input("\nCuantas asignaturas deseas ingresar?: "))

    diccAsig = {}

    for i in range(cantAsig):
        nombAsig = input(f"\nDigite el Nombre de la Asignatura {i + 1}: ")
        credAsig = int(input(f"Digite los Creditos de la Asignatura {nombAsig}: "))

        diccAsig[nombAsig.capitalize()] = credAsig

    print("\nEl Diccionario de Asignaturas con sus Creditos es:\n")
    print(diccAsig)

    ttlCred = sum(diccAsig.values())

    print(f"\nEl Total de Creditos del Curso es: {ttlCred}")
    print("\n======================================")

DiccCredAsig()