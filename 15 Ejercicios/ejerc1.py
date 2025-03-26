# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en  un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en  <dirección> y su número de teléfono es <teléfono>. 

def infoPersonal():
    print("========== Informacion Personal ==========")

    nomb = input("\nDigite su Nombre: ")
    edad = int(input("Digite su Edad: "))
    direc = input("Digite su Direccion de Residencia: ")
    telf = int(input("Digite su Numero de Celular: "))

    # Crea un diccionario llamado 'persona' para almacenar los datos ingresados por el usuario
    persona = {"Nombre": nomb, "Edad": edad, "Direccion": direc, "Telefono": telf}

    # Las claves del diccionario se acceden con comillas simples para evitar errores de sintaxis
    print(f"\n{persona['Nombre']} tiene {persona['Edad']} años, Vive en {persona['Direccion']} y su Numero de Telefono es {persona['Telefono']}.")

    print("\n==========================================")

infoPersonal()