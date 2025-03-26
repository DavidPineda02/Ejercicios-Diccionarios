# Función zip ()

# Se crean dos diccionarios con los nombres de los aprendices y sus respectivas notas en dos evaluaciones diferentes
notasAprend1 = {
    "Michelle": 8,  
    "Ximena": 57,   
    "David": 87,    
    "Jensen": 90,   
    "Nicolas": 32,  
    "Edwar": 94     
}
notasAprend2 = {
    "Michelle": 70,  
    "Ximena": 45,   
    "David": 36,    
    "Jensen": 76,   
    "Nicolas": 27,  
    "Edwar": 74     
}

# Se crea un diccionario vacío para almacenar la combinación de notas de cada aprendiz
diccCombinado = {}

# Se recorre ambos diccionarios simultáneamente usando zip() para emparejar las claves
for key1, key2 in zip(notasAprend1.keys(), notasAprend2.keys()):
    diccCombinado[key1] = (notasAprend1[key1], notasAprend2[key2])  
    # Se almacena una tupla con las notas del aprendiz en ambas evaluaciones

print("====== Combinando Diccionarios ======\n")
print(f"Diccionario 1: {notasAprend1}")  # Se muestra el primer diccionario de notas
print(f"Diccionario 2: {notasAprend2}")  # Se muestra el segundo diccionario de notas
print(f"\nDiccionario Combinado: {diccCombinado}")  # Se muestra el diccionario combinado con las notas en tuplas
print("\n=====================================")