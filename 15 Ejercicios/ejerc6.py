# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las  palabras español e inglés separadas por dos puntos, y cada par: separados por comas. El programa  debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español  y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario  debe dejarla sin traducir.

# Definimos una función llamada TradcEsplIngl() que traduce palabras de español a inglés
def TradcEsplIngl():
    print("==== Traductor Español-Inglés ====")

    # Se solicita al usuario ingresar palabras en formato "Español:Inglés", separadas por comas
    palbrs = input("\nDigite las Palabras 'Español:Inglés' Separadas por Comas: ")

    # Se crea un diccionario vacío para almacenar las traducciones
    diccPalbrs = {}

    # Se divide la entrada del usuario en pares de palabras (Español:Inglés)
    pares = palbrs.split(",")

    # Se recorre la lista de pares para almacenarlos en el diccionario
    for par in pares:
        if ":" in par:
            # Se separa cada par en palabras individuales y se eliminan espacios extra
            espanol, ingles = par.split(":")
            diccPalbrs[espanol.strip().capitalize()] = ingles.strip().capitalize()
    
    # Se imprime el diccionario de traducción generado
    print("\nDiccionario de traducción:")
    for clave, valor in diccPalbrs.items():
        print(f"{clave} - {valor}")

    # Se solicita una frase en español para traducirla
    frase = input("\nDigite una Frase en Español para Traducirla: ")
    
    # Se separa la frase en palabras individuales
    palabras = frase.split()

    # Se crea una lista donde se almacenará la traducción
    traduccion = []
    
    # Se recorre cada palabra de la frase
    for palabra in palabras:
        # Se busca la palabra en el diccionario y se agrega la traducción (o la palabra original si no está)
        traduccion.append(diccPalbrs.get(palabra.capitalize(), palabra))
    
    # Se imprime la frase traducida
    print("\nFrase traducida:")
    print(" ".join(traduccion))

# Se llama a la función para ejecutar el traductor
TradcEsplIngl()