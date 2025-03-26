#Función enumerate().

# Se crea un diccionario con frutas y sus respectivos precios
frutas = {
    "manzana": 5000,  # Clave "manzana" con el precio 5000
    "banana": 3000,   # Clave "banana" con el precio 3000
    "naranja": 2000,  # Clave "naranja" con el precio 2000
    "uva": 4000,      # Clave "uva" con el precio 4000
    "fresa": 3000     # Clave "fresa" con el precio 3000
}

print("====== Indice y Clave =======\n")

# Se recorre el diccionario con la función enumerate(), obteniendo el índice y la clave
for indice, clave in enumerate(frutas.keys()):
    print(f"Indice {indice}: Clave '{clave}'")  # Se imprime el índice y la clave correspondiente

print("=\n============================")
