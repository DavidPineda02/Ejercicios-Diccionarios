# `Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes  se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro  diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde  preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al  usuario por una opción del siguiente menú:  

# ✓ Añadir cliente,  
# ✓ Eliminar cliente,  
# ✓ Mostrar cliente,  
# ✓ Listar todos los clientes,  
# ✓ Listar clientes preferentes,  
# ✓ Terminar.

#  En función de la opción elegida el programa tendrá que hacer lo siguiente: • Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de  datos. 

# • Preguntar por el NIF del cliente y eliminar sus datos de la base de datos. 
# • Preguntar por el NIF del cliente y mostrar sus datos. 
# • Mostrar lista de todos los clientes de la base datos con su NIF y nombre. 
# • Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre. `

# Diccionario principal para almacenar los datos de los clientes
clientesEmpresa = {}

def AñadirCliente():
    # Solicita los datos de un cliente y lo añade al diccionario si no existe previamente
    nifCliente = int(input("\nDigite el NIF Del Cliente: "))  # NIF del cliente
    
    if nifCliente in clientesEmpresa:  # Verifica si el cliente ya está registrado
        print("\nEl Cliente ya esta Registrado.")
        return
    else:
        nombCliente = input("Digite el Nombre del Cliente: ").strip().capitalize()  # Nombre del cliente
        direccCliente = input("Digite la Direccion del Cliente: ").strip()  # Dirección del cliente
        telefCliente = int(input("Digite el Telefono del Cliente: "))  # Teléfono del cliente
        correoCliente = input("Digite el Correo del Cliente: ").strip()  # Correo del cliente
        prefer = input(f"{nombCliente} es un Cliente Preferente? (Si - No): ").lower().strip()  # Cliente preferente

        if prefer == "si":  # Si el cliente es preferente
            clientePreferente = True
        elif prefer == "no":  # Si el cliente no es preferente
            clientePreferente = False
        else:
            print("\nOpcion no Valida.")  # Mensaje si la opción no es válida
            return

        # Añade el cliente al diccionario
        clientesEmpresa[nifCliente] = {
            "nombre": nombCliente, 
            "direccion": direccCliente, 
            "telefono": telefCliente, 
            "correo": correoCliente, 
            "preferente": clientePreferente
        }
        
        print("\nEl Cliente fue Añadido Correctamente.")

def EliminarCliente():
    # Elimina un cliente del diccionario si existe
    nifCliente = int(input("\nDigite el NIF del Cliente que desea Eliminar: "))  # NIF del cliente a eliminar
    
    if nifCliente not in clientesEmpresa:  # Verifica si el cliente no está registrado
        print("\nEl Cliente no se Encuentra Registrado.")
        return
    else:
        clientesEmpresa.pop(nifCliente)  # Elimina el cliente del diccionario
        print("\nEl Cliente fue Eliminado Correctamente.")

def MostrarCliente():
    # Muestra los datos de un cliente específico si existe
    nifCliente = int(input("\nDigite el NIF del Cliente que desea Mostrar: "))  # NIF del cliente a mostrar
    
    if nifCliente not in clientesEmpresa:  # Verifica si el cliente no está registrado
        print("\nEl Cliente no se Encuentra Registrado.")
        return
    else:
        datosCliente = clientesEmpresa.get(nifCliente, "Cliente no Encontrado")  # Obtiene los datos del cliente
        
        print("\n------- Datos Personales -------\n")
        for clave, valor in datosCliente.items():  # Itera sobre los datos del cliente
            print(f"{clave.capitalize()}: {valor}")
        print("\n--------------------------------")

def ListarTodosClientes():
    # Lista todos los clientes registrados
    if not clientesEmpresa:  # Verifica si no hay clientes registrados
        print("\nNo hay clientes registrados.")
        return
    else:
        print("\n======= Todos los Clientes =======\n")
        for nifCliente, datosCliente in clientesEmpresa.items():  # Itera sobre todos los clientes
            print(f"NIF: {nifCliente}, Nombre: {datosCliente['nombre']}")
        print("\n==================================")

def ListarClientesPreferentes():
    # Lista solo los clientes preferentes
    if not clientesEmpresa:  # Verifica si no hay clientes registrados
        print("\nNo hay clientes registrados.")
        return

    # clientesPreferentes = {
    #     nif: datos for nif, datos in clientesEmpresa.items() if datos["preferente"]
    # }

    clientesPreferentes = {}  # Diccionario temporal para almacenar clientes preferentes
    for nif, datos in clientesEmpresa.items():  # Filtra los clientes preferentes
        if datos["preferente"]:
            clientesPreferentes[nif] = datos
    
    if not clientesPreferentes:  # Verifica si no hay clientes preferentes
        print("\nNo hay clientes preferentes registrados.")
        return
    
    print("\n======= Clientes Preferentes =======\n")
    for nifCliente, datosCliente in clientesPreferentes.items():  # Itera sobre los clientes preferentes
        print(f"NIF: {nifCliente}, Nombre: {datosCliente['nombre']}")
    print("\n====================================")

# Menú principal del programa
print("======= Clientes Empresariales =======")

while True:
    # Opciones del menú
    print("\n1. Añadir Cliente. \n2. Eliminar Cliente. \n3. Mostrar Cliente. \n4. Listar todos los Clientes. \n5. Listar Clientes Preferentes. \n0. Terminar.")
    opc = int(input("\nDigita la opcion que deseas: "))  # Lee la opción seleccionada por el usuario

    if opc == 1:  # Opción para añadir un cliente
        AñadirCliente()
    elif opc == 2:  # Opción para eliminar un cliente
        EliminarCliente()
    elif opc == 3:  # Opción para mostrar un cliente
        MostrarCliente()
    elif opc == 4:  # Opción para listar todos los clientes
        ListarTodosClientes()
    elif opc == 5:  # Opción para listar clientes preferentes
        ListarClientesPreferentes()
    elif opc == 0:  # Opción para finalizar el programa
        print("\nGracias por Visitarnos, Vuelva Pronto.")
        print("\n======================================")
        break
    else:  # Manejo de opción inválida
        print("\nOpcion Incorrecta. Intente Nuevamente.")