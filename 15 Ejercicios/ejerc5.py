# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe  preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.  Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato.

# Definimos una función llamada CestaCompra() que permite al usuario ingresar artículos y sus precios
def CestaCompra():
    print("======== Cesta de Compra ========")

    # Se crea un diccionario vacío para almacenar los artículos y sus precios
    diccArtcl = {}

    # Bucle infinito para ingresar artículos hasta que el usuario decida salir
    while True:
        # Se solicita el nombre del artículo
        artcl = input("\nDigite el Artículo que Desea Comprar (Digita 0 para Salir): ")

        # Si el usuario ingresa "0", se rompe el ciclo y se finaliza la entrada de datos
        if artcl == "0":
            break

        # Se solicita el precio del artículo y se convierte a entero
        valArtcl = int(input("Digite el Precio del Artículo: "))

        # Se almacena el artículo en el diccionario con la clave capitalizada y el precio como valor
        diccArtcl[artcl.capitalize()] = valArtcl

    # Se calcula el total de la compra sumando los valores del diccionario
    totlComp = sum(diccArtcl.values())

    # Se imprime la lista de compra en un formato tabular
    print("\n+----------------------+---------+")
    print("| Lista de la compra   | Precio  |")
    print("+----------------------+---------+")

    for art, precio in diccArtcl.items():
        print(f"| {art:<20} | {precio:>7} |")  # Se alinean los valores para mejor visualización

    # Se imprime el total de la compra
    print("+----------------------+---------+")
    print(f"| Total                | {totlComp:>7} |")
    print("+----------------------+---------+")

# Se llama a la función para ejecutar el programa
CestaCompra()