# Método items()

# Se crea un diccionario con productos y sus respectivos precios
prod = {
    "manzana": 5000,  # Clave "manzana" con el precio 5000
    "banana": 3000,   # Clave "banana" con el precio 3000
    "naranja": 2000,  # Clave "naranja" con el precio 2000
    "uva": 4000,      # Clave "uva" con el precio 4000
    "fresa": 3000     # Clave "fresa" con el precio 3000
}

print("========= Frutas y Precios ==========\n")

# Se recorre el diccionario y se imprimen las frutas y sus precios
for fruta, precio in prod.items():
    print(f"Fruta: {fruta.capitalize()} - Precio: ${precio}")

print("\n====================================")
