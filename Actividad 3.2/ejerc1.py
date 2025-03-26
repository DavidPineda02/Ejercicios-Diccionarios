# 1. Identificar la función que devuelva el número de elementos que tiene un diccionario, dar ejemplos.

# Definimos un diccionario con información personal
myInfo = {
    "nombre": "David",  # Clave "nombre" con valor "David"
    "edad": 19,         # Clave "edad" con valor 19
    "ciudad": "Bucaramanga"  # Clave "ciudad" con valor "Bucaramanga"
}

# Calculamos la cantidad de elementos (pares clave-valor) en el diccionario
numsElemts = len(myInfo)

# Imprimimos la cantidad de elementos en el diccionario
print(f"Cantidad de Elementos: {numsElemts}")