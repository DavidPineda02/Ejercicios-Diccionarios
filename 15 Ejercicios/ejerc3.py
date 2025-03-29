#  Escribe un programa Python que pida un número por teclado y que cree un diccionario cuyas claves  sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves. 

# Definimos una función llamada DiccNumCuadr() que genera un diccionario con números y sus cuadrados
def DiccNumCuadr():
    print("======= Diccionario de Numeros Cuadrados =======")

    # Se solicita al usuario un número entero
    num = int(input("\nDigite un Numero Entero: "))

    # Se verifica si el número ingresado es positivo
    if num > 0:
        # Se genera un diccionario donde las claves son los números del 1 al num y los valores son sus cuadrados
        diccNumCuad = {i: i**2 for i in range(1, num + 1)}

        # Se imprime el diccionario generado
        print("\nEl Diccionario Generado es:\n")
        print(diccNumCuad)
        print("\n================================================")
    else:
        # Mensaje de error si el número no es válido
        print("\nNumero no Valido.")
        print("\n================================================")

# Se llama a la función para ejecutar el programa
DiccNumCuadr()