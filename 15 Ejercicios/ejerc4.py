# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso  {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada  asignatura en el formato tiene créditos, donde es cada una de las asignaturas del curso, y son sus  créditos. Al final debe mostrar también el número total de créditos del curso.

# Definimos una función llamada DiccCredAsig() que permite ingresar asignaturas con sus créditos
def DiccCredAsig():
    print("======== Créditos Asignaturas ========")

    # Se solicita al usuario la cantidad de asignaturas a ingresar
    cantAsig = int(input("\n¿Cuántas asignaturas deseas ingresar?: "))

    # Se crea un diccionario vacío para almacenar asignaturas y sus créditos
    diccAsig = {}

    # Bucle para ingresar los datos de las asignaturas
    for i in range(cantAsig):
        # Se solicita el nombre de la asignatura
        nombAsig = input(f"\nDigite el Nombre de la Asignatura {i + 1}: ")
        # Se solicita el número de créditos de la asignatura y se convierte a entero
        credAsig = int(input(f"Digite los Créditos de la Asignatura {nombAsig}: "))

        # Se almacena la asignatura en el diccionario con la clave capitalizada y los créditos como valor
        diccAsig[nombAsig.capitalize()] = credAsig

    # Se imprime el diccionario con las asignaturas y sus respectivos créditos
    print("\nEl Diccionario de Asignaturas con sus Créditos es:\n")
    print(diccAsig)

    # Se calcula el total de créditos sumando los valores del diccionario
    ttlCred = sum(diccAsig.values())

    # Se imprime el total de créditos del curso
    print(f"\nEl Total de Créditos del Curso es: {ttlCred}")
    print("\n======================================")

# Se llama a la función para ejecutar el programa
DiccCredAsig()
