# En una escuela se necesita un programa el cual gestione la cantidad de personas que entran a cuyo  salón, teniendo en cuenta que se debe que tener la información personal de cada estudiante y de  los profesores, así mismo, se debe tener un registro del número del salón al cual se le valla a hacer  la gestión y que al final se muestre en pantalla.

def registroPersona(tipoRegistro):
    # Solicita los datos de una persona (estudiante o profesor) y los devuelve como un diccionario
    print(f"\nRegistro de {tipoRegistro}:")
    nombre = input(f"Digite el Nombre del {tipoRegistro}: ")  # Nombre de la persona
    edad = int(input(f"Digite la Edad del {tipoRegistro}: "))  # Edad de la persona
    documento = input(f"Digite el Numero de Documento del {tipoRegistro}: ")  # Número de documento
    return {"nombre": nombre, "edad": edad, "documento": documento}

def mostrar_datos(persona, tipoRegistro):
    # Muestra los datos de una persona (estudiante o profesor) en formato legible
    print(f"\nDatos del {tipoRegistro}:")
    for clave, valor in persona.items():  # Itera sobre los datos de la persona
        print(f"{clave.capitalize()}: {valor}")

def gestionar_salon():
    # Gestiona el registro de estudiantes y profesores en un salón escolar
    print("========== Gestion Escolar =========")
    numSalon = input("\nDigite el Numero del Salon: ")  # Número del salón
    cantEstudiantes = int(input("\nCuantos Estudiantes hay en el Salon?: "))  # Cantidad de estudiantes
    estudiantes = []  # Lista para almacenar los datos de los estudiantes

    # Registro de estudiantes
    for i in range(cantEstudiantes):  # Itera según la cantidad de estudiantes
        print(f"\nRegistro del estudiante {i + 1}:")
        estudiante = registroPersona("Estudiante")  # Llama a la función para registrar un estudiante
        estudiantes.append(estudiante)  # Agrega el estudiante a la lista

    cantProfesores = int(input("\nCuantos Profesores hay en el Salon?: "))  # Cantidad de profesores
    profesores = []  # Lista para almacenar los datos de los profesores

    # Registro de profesores
    for i in range(cantProfesores):  # Itera según la cantidad de profesores
        print(f"\nRegistro del Profesor {i + 1}:")
        profesor = registroPersona("Profesor")  # Llama a la función para registrar un profesor
        profesores.append(profesor)  # Agrega el profesor a la lista

    # Mostrar información del salón
    print("\n----- Informacion del Salon -----")
    print(f"Numero del Salon: {numSalon}")  # Muestra el número del salón

    print("\n----- Estudiantes Registrados -----")
    for i, estudiante in enumerate(estudiantes, start=1):  # Itera sobre los estudiantes registrados
        print(f"\nEstudiante {i}:")
        mostrar_datos(estudiante, "Estudiante")  # Muestra los datos del estudiante
    print("\n-----------------------------------")

    print("\n----- Profesores Registrados -----")
    for i, profesor in enumerate(profesores, start=1):  # Itera sobre los profesores registrados
        print(f"\nProfesor {i}:")
        mostrar_datos(profesor, "Profesor")  # Muestra los datos del profesor
    print("\n----------------------------------")

# Ejecuta la función principal para gestionar el salón
gestionar_salon()