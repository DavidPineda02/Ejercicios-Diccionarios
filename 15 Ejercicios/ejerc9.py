# Crear un programa en Python donde se le pregunte al usuario su nombre su edad y su número de  documento, todo esto deberá estar almacenado en un diccionario.

def infoPersonal():
    usuario = {}
    print("======== Informacion Personal ========")
    usuario['nombre'] = input("\nDigite su Nombre: ")
    usuario['edad'] = int(input("Digite su Edad: "))
    usuario['documento'] = input("Digite su Numero de Documento: ")

    print("\nInformacion Almacenada:\n")
    for clave, valor in usuario.items():
        print(f"{clave.capitalize()}: {valor}")
    print("\n======================================")

infoPersonal()