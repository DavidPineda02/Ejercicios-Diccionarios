# Función reversed()

# Se crea un diccionario con los nombres de los aprendices y sus respectivas notas
notasAprend = {
    "Michelle": 8,  
    "Ximena": 57,   
    "David": 87,    
    "Jensen": 90,   
    "Nicolas": 32,  
    "Edwar": 94     
}

# Se crea un diccionario vacío para almacenar los elementos en orden inverso
dictInvert = {}

# Se recorre el diccionario en orden inverso usando reversed() y list()
for clave, valor in reversed(list(notasAprend.items())):
    dictInvert[clave] = valor  # Se agregan los elementos al nuevo diccionario en orden inverso

# Se imprime el diccionario en su orden original
print("====== Orden Normal ======\n")
for clave in notasAprend.keys():
    print(f"Clave: {clave} - Valor: {notasAprend[clave]}")  # Se imprime clave y valor en orden original

# Se imprime el diccionario en orden inverso
print("\n====== Orden Inverso ======\n")
for clave in dictInvert.keys():
    print(f"Clave: {clave} - Valor: {dictInvert[clave]}")  # Se imprime clave y valor en orden inverso
print("\n===========================")