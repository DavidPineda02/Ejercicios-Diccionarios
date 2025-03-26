# Función sorted()

# Se crea un diccionario con frutas y sus respectivos precios
frutas = {
    "manzana": 5000,  # Clave "manzana" con el precio 5000
    "banana": 3000,   # Clave "banana" con el precio 3000
    "naranja": 2000,  # Clave "naranja" con el precio 2000
    "uva": 4000,      # Clave "uva" con el precio 4000
    "fresa": 3000     # Clave "fresa" con el precio 3000
}

# Se imprime el diccionario en su orden original
print("====== Diccionario Original ======\n")
for clave in frutas:
    print(f"Clave: {clave.capitalize()} - Valor: {frutas[clave]}")  # Se muestra cada clave y su valor

# Se imprime el diccionario ordenado por claves
print("\n====== Diccionario Ordenado por Claves ======\n")
for clave in sorted(frutas.keys()):  # sorted() ordena las claves alfabéticamente
    print(f"Clave: {clave.capitalize()} - Valor: {frutas[clave]}")
print("\n=============================================")