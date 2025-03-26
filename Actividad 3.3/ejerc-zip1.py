# Función zip ()

# Se crean dos listas: una con claves (nombres de frutas) y otra con valores (precios)
listClav = ["manzana", "banana", "naranja", "uva", "fresa"]  # Lista de claves
listVal = [5000, 3000, 2000, 4000, 3000]                      # Lista de valores

# Se usa la función zip() para combinar ambas listas y crear un diccionario
diccion = dict(zip(listClav, listVal))  
# zip() empareja los elementos de ambas listas en tuplas y dict() las convierte en un diccionario

# Se imprime la información generada
print("====== Diccionario Creado ======\n")
print(f"Lista Claves: {listClav}")  # Se muestra la lista de claves
print(f"Lista Valores: {listVal}")  # Se muestra la lista de valores
print(f"\nDiccionario: {diccion}")   # Se muestra el diccionario resultante
print("\n================================")
