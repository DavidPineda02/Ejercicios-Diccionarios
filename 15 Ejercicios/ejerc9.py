# Crear un programa en Python donde se le pregunte al usuario su nombre su edad y su número de  documento, todo esto deberá estar almacenado en un diccionario.

def infoPersonal():
    usuario = {}  # Diccionario para almacenar la información del usuario
    print("======== Informacion Personal ========")
    
    # Solicita el nombre del usuario y lo guarda en el diccionario
    usuario['nombre'] = input("\nDigite su Nombre: ").strip().capitalize()  # Nombre del usuario (formateado)
    
    # Solicita la edad del usuario y la convierte a entero
    usuario['edad'] = int(input("Digite su Edad: "))  # Edad del usuario (entero)
    
    # Solicita el número de documento del usuario
    usuario['documento'] = input("Digite su Numero de Documento: ").strip()  # Número de documento
    
    # Muestra la información almacenada en el diccionario
    print("\nInformacion Almacenada:\n")
    for clave, valor in usuario.items():  # Itera sobre los elementos del diccionario
        print(f"{clave.capitalize()}: {valor}")  # Muestra cada clave y su valor formateados
    
    print("\n======================================")

# Ejecuta la función principal
infoPersonal()