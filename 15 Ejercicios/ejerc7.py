# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se  almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor  el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura,  pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de  factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el  número de factura y se eliminará del diccionario. Después de cada operación el programa debe  mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro. 

# Diccionarios para almacenar facturas pendientes y cobradas
FactPendiet = {}  # Almacena las facturas pendientes {número_factura: valor}
FactCobrad = {}  # Almacena las facturas cobradas {número_factura: valor}

def NuevFact():
    # Solicita los datos de una nueva factura y la agrega a las facturas pendientes
    numFact = int(input("\nDigite el Numero de la Factura: "))  # Número de la factura
    valFact = float(input("Digite el Valor de la Factura: "))  # Valor de la factura

    if numFact in FactPendiet:  # Verifica si la factura ya existe
        print(f"\nLa Factura {numFact} ya Existe.")
    else:
        FactPendiet[numFact] = valFact  # Agrega la factura al diccionario de pendientes
        print(f"\nLa Factura {numFact} fue Agregada con Exito.")

def PagrFact():
    # Permite pagar una factura pendiente y moverla al diccionario de facturas cobradas
    numFact = int(input("\nDigite el Numero de la Factura que Deseas Pagar: "))  # Número de la factura a pagar

    if numFact in FactPendiet:  # Verifica si la factura está pendiente
        valorPago = FactPendiet.pop(numFact)  # Elimina la factura de pendientes y obtiene su valor
        FactCobrad[numFact] = valorPago  # Agrega la factura a las cobradas
        print(f"\nFactura {numFact} Pagada con Exito.")
    else:
        print(f"\nLa Factura {numFact} No Existe en las Facturas Pendientes.")  # Mensaje si no existe

def MostrFact():
    # Muestra el total de facturas pendientes y cobradas
    totlFactPendin = sum(FactPendiet.values())  # Calcula el total de facturas pendientes
    totlFactCobrad = sum(FactCobrad.values())  # Calcula el total de facturas cobradas

    if not FactPendiet and not FactCobrad:  # Verifica si no hay facturas registradas
        print("\nNo hay Facturas Disponibles")
    else:
        print(f"\nCantidad Pendiente de Cobro: ${totlFactPendin:.2f}")  # Muestra total pendiente
        print(f"Cantidad Cobrada hasta el Momento: ${totlFactCobrad:.2f}")  # Muestra total cobrado

# Menú principal del programa
print("========== Facturas Empresariales ==========")
while True:
    # Opciones del menú
    print("\n1. Nueva Factura. \n2. Pagar Factura. \n3. Mostrar Valores Pendientes y Cobrados. \n0. Terminar.")
    opc = int(input("\nDigite la Opcion que Deseas: "))  # Lee la opción seleccionada por el usuario

    if opc == 1:  # Opción para agregar una nueva factura
        NuevFact()
    elif opc == 2:  # Opción para pagar una factura pendiente
        PagrFact()
    elif opc == 3:  # Opción para mostrar los totales de facturas
        MostrFact()
    elif opc == 0:  # Opción para finalizar el programa
        print("\nPrograma Finalizado. Hasta luego")
        print("\n============================================")
        break
    else:  # Manejo de opción inválida
        print("\nOpcion Incorrecta. Intente Nuevamente.")