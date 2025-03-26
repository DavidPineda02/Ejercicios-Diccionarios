# 2. Función que permite comparar el número de elementos de diferentes entre dos diccionarios.

# Función para comparar la cantidad de elementos en dos diccionarios
def compararDicc(dic1, dic2):
    # Se obtiene la cantidad de elementos en cada diccionario
    cantDicc1 = len(dic1)
    cantDicc2 = len(dic2)
    
    # Se comparan las cantidades y se devuelve un mensaje acorde
    if cantDicc1 > cantDicc2:
        return f"El Diccionario 1 tiene más Elementos: ({cantDicc1} vs {cantDicc2})"
    elif cantDicc1 < cantDicc2:
        return f"El Diccionario 2 tiene más Elementos: ({cantDicc2} vs {cantDicc1})"
    else:
        return "Ambos Diccionarios tienen la misma Cantidad de Elementos."

# Definimos el primer diccionario con tres elementos
dicc1 = {
    "nombre": "Ximena",
    "edad": 22,
    "ciudad": "Piedecuesta"
}

# Definimos el segundo diccionario con dos elementos
dicc2 = {
    "nombre": "Michelle",
    "edad": 17
}

# Se llama a la función y se almacena el resultado en la variable 'resultado'
resultado = compararDicc(dicc1, dicc2)

# Se imprime el resultado de la comparación
print(resultado)
