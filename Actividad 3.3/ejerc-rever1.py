# Función reversed()

# Se crea un diccionario con frutas y sus respectivos precios
frutas = {
    "manzana": 5000,  # Clave "manzana" con el precio 5000
    "banana": 3000,   # Clave "banana" con el precio 3000
    "naranja": 2000,  # Clave "naranja" con el precio 2000
    "uva": 4000,      # Clave "uva" con el precio 4000
    "fresa": 3000     # Clave "fresa" con el precio 3000
}

# Se imprime el diccionario en su orden original
print("====== Orden Normal ======\n")
for clave in frutas.keys():  # Se recorre el diccionario obteniendo solo las claves
    print(f"Clave: {clave.capitalize()} - Valor: {frutas[clave]}")  # Se imprime clave y valor

# Se imprime el diccionario en orden inverso
print("\n====== Orden Inverso ======\n")
for clave in reversed(frutas.keys()):  # Se recorre el diccionario en orden inverso
    print(f"Clave: {clave.capitalize()} - Valor: {frutas[clave]}")  # Se imprime clave y valor
print("\n===========================")
