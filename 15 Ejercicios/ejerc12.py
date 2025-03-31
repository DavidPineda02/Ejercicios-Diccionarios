# Realizar un algoritmo el cual pregunte el nombre de la persona y la edad, tener en cuenta que al  momento de mostrar la edad en pantalla debe mostrar la fecha de nacimiento de dicha persona. 

from datetime import date

def calculoFechaNacimiento():
    print("======== Fecha Nacimiento ========")
    
    # Solicita el nombre del usuario
    nombre = input("\nDigita tu Nombre: ").strip().capitalize()  # Nombre del usuario (formateado)

    # Solicita la edad del usuario
    edad = int(input("Digita tu Edad: "))  # Edad del usuario (entero)

    # Obtiene el año actual usando la biblioteca `datetime`
    añoActual = date.today().year  # Año actual según el sistema

    # Validación de la edad ingresada
    if edad < 0 or edad > añoActual:  # Verifica si la edad es negativa o mayor al año actual
        print("\nLa Edad Ingresada no es Valida.")  # Mensaje de error si la edad no es válida
        return  # Termina la función si la edad no es válida

    # Calcula el año de nacimiento restando la edad al año actual
    añoNacimiento = añoActual - edad

    # Muestra el resultado
    print(f"\n{nombre}, Naciste en el año {añoNacimiento}")
    print("\n==================================")

# Ejecuta la función principal
calculoFechaNacimiento()