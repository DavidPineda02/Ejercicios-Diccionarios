# Función sorted()

# Se crea un diccionario con los nombres de los aprendices y sus respectivas notas
notasAprend = {
    "Edwar": 94,    
    "Ximena": 57,   
    "David": 87,    
    "Jensen": 90,   
    "Nicolas": 32,  
    "Michelle": 8    
}

# Se imprime el diccionario en su orden original
print("====== Diccionario Original ======\n")
for clave in notasAprend:
    print(f"Aprendiz: {clave} - Nota: {notasAprend[clave]}")  # Se muestra cada aprendiz con su nota original

# Se imprime el diccionario ordenado por valores (notas)
print("\n====== Diccionario Ordenado por Valores ======\n")
for clave, valor in sorted(notasAprend.items(), key=lambda item: item[1]):  
    # sorted() ordena la lista de tuplas (clave, valor) en función del segundo elemento (nota)
    print(f"Aprendiz: {clave} - Nota: {valor}")  
print("\n==============================================")


#Sintaxis General de la Funcion lambda: (lambda argumentos: expresión)
# argumentos: Los valores que recibe la función.
# expresión: La operación que se realiza con los argumentos y que devuelve un resultado.