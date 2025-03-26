#Función enumerate().

# Se crea un diccionario con los nombres de los aprendices y sus respectivas notas
notasAprend = {
    "Michelle": 8,  
    "Ximena": 57,   
    "David": 87,    
    "Jensen": 90,   
    "Nicolas": 32,  
    "Edwar": 94     
}

print("====== Índice, Aprendiz y Nota ======\n")

# Se recorre el diccionario con la función enumerate(), obteniendo el índice y los pares (clave, valor)
for indice, (aprendiz, nota) in enumerate(notasAprend.items()):
    print(f"Índice {indice}: Aprendiz '{aprendiz}', Nota: {nota}")  # Se imprime el índice, el nombre y la nota

print("\n=====================================")
