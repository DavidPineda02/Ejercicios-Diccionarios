# 2. Función que permite comparar el número de elementos de diferentes entre dos diccionarios.

def compararDicc(dic1, dic2):
    cantDicc1 = len(dic1)
    cantDicc2 = len(dic2)
    
    if cantDicc1 > cantDicc2:
        return f"El Diccionario 1 tiene mas Elementos: ({cantDicc1} vs {cantDicc2})"
    elif cantDicc1 < cantDicc2:
        return f"El Diccionario 2 tiene mas Elementos: ({cantDicc2} vs {cantDicc1})"
    else:
        return "Ambos Diccionarios tienen la misma Cantidad de Elementos."

dicc1 = {
    "nombre": "Ximena",
    "edad": 22,
    "ciudad": "Piedecuesta"
}

dicc2 = {
    "nombre": "Michelle",
    "edad": 17
}

resultado = compararDicc(dicc1, dicc2)
print(resultado)