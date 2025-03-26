# 4. Cuál es la función que permite devolver el número de elementos que tiene el diccionario

# Se crea un diccionario con información sobre un libro
libro = {
    "titulo": "Cien Años de Soledad",       # Clave "titulo" con el nombre del libro
    "autor": "Gabriel García Márquez",      # Clave "autor" con el nombre del escritor
    "año": 1967,                            # Clave "año" con el año de publicación
    "genero": "Realismo Mágico",            # Clave "genero" con el género literario
    "paginas": 417                          # Clave "paginas" con el número de páginas
}

# Se obtiene la cantidad de elementos en el diccionario
cantElemnt = len(libro)

# Se imprimen los resultados
print(f"Diccionario: {libro}")  
print(f"Cantidad de Elementos del Diccionario: {cantElemnt}")