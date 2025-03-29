# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al  usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos  de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. 

# Definimos una función llamada Frutas() que maneja la venta de frutas
def Frutas():
    # Se crea un diccionario con frutas y sus respectivos precios por unidad
    frutas = {
        "manzana": 0.80,   
        "banana": 1.35,
        "naranja": 0.70,
        "pera": 0.85,
    }

    # Se muestra el listado de frutas y sus precios
    print("========== Venta de Fruta ==========\n")
    for fruta, precio in frutas.items():
        print(f"Fruta: {fruta.capitalize()} - Precio: ${precio}")  # Se imprimen las frutas y sus precios

    print("\n====================================")

    # Se solicita al usuario que ingrese la fruta que desea comprar
    fruts = input("\n¿Cuál fruta desea llevar?: ")

    # Se verifica si la fruta ingresada está en el diccionario
    if fruts.lower() in frutas:
        # Se solicita la cantidad de frutas a comprar
        cantFruts = int(input(f"¿Cuántas {fruts.capitalize()} deseas llevar?: "))

        # Se calcula el total a pagar multiplicando la cantidad por el precio unitario
        pago = cantFruts * frutas.get(fruts)

        # Se muestra el total a pagar con dos decimales
        print(f"\nTotal a pagar: ${pago:.2f}")
        print("\n====================================")
    else:
        # Mensaje si la fruta no está disponible en el diccionario
        print("\nFruta NO Disponible.")
        print("\n====================================")

# Se llama a la función para ejecutar el programa
Frutas()
