# Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase  y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la  información en un diccionario cuyas claves serán los nombres de los alumnos y los valores serán  listas con las notas de cada alumno. 

# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo  sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista  de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un  alumno que ya existe el programa nos dará un error.

def registroAlumnos(cantAlumnos):
    alumnos = {}  # Diccionario para almacenar los datos de los alumnos

    for i in range(cantAlumnos):  # Itera según la cantidad de alumnos a registrar
        while True:  # Bucle para validar nombres duplicados
            print(f"\nRegistro del Alumno {i + 1}:")
            nombre = input("Digite el nombre del Alumno: ").strip().capitalize()  # Nombre del alumno

            if nombre in alumnos:  # Verifica si el alumno ya está registrado
                print("\nEl Alumno ya esta Registrado. Intente con otro Nombre.")
            else:
                break  # Sale del bucle si el nombre no está duplicado

        notas = []  # Lista para almacenar las notas del alumno
        while True:  # Bucle para ingresar notas hasta que se introduzca un número negativo
            nota = float(input(f"Digite la Nota de {nombre} (Número Negativo para Terminar): "))
            if nota < 0:  # Termina la entrada de notas si se introduce un número negativo
                break
            notas.append(nota)  # Agrega la nota a la lista

        alumnos[nombre] = notas  # Guarda el nombre y las notas en el diccionario

    return alumnos  # Retorna el diccionario con los datos de los alumnos


def calculoPromedios(alumnos):
    promedios = {}  # Diccionario para almacenar los promedios

    for nombre, notas in alumnos.items():  # Itera sobre los alumnos y sus notas
        if notas:  # Verifica que haya notas para calcular el promedio
            promedio = sum(notas) / len(notas)  # Calcula el promedio
        else:
            promedio = 0  # Si no hay notas, el promedio es 0
        promedios[nombre] = promedio  # Guarda el promedio en el diccionario

    return promedios  # Retorna el diccionario con los promedios


def listarResultados(promedios):
    print("\n----- Resultados Finales -----")  # Encabezado de los resultados
    for nombre, promedio in promedios.items():  # Itera sobre los promedios
        print(f"{nombre}: Promedio = {promedio:.2f}")  # Muestra el nombre y el promedio formateado
    print("--------------------------------")  # Línea divisoria


# Programa principal
print("========== Registro de Alumnos y Notas ==========")
cantAlumnos = int(input("\nDigite la Cantidad de Alumnos a Registrar: "))  # Solicita la cantidad de alumnos

alumnos = registroAlumnos(cantAlumnos)  # Registra los alumnos y sus notas
promedios = calculoPromedios(alumnos)  # Calcula los promedios de notas

listarResultados(promedios)  # Muestra los resultados finales