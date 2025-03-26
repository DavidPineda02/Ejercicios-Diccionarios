#8. Función que permite añadir los elementos de un diccionario a otro. 

# Se crea el primer diccionario con información personal
dicc1 = {
    "nombre": "David",          # Clave "nombre" con el valor "David"
    "edad": 19,                 # Clave "edad" con el valor 19
    "ciudad": "Piedecuesta"      # Clave "ciudad" con el valor "Piedecuesta"
}

# Se crea el segundo diccionario con información adicional
dicc2 = {
    "ocupacion": "Ingeniera",               # Clave "ocupacion" con el valor "Ingeniera"
    "hobbies": ["Baloncesto", "Codificar"], # Clave "hobbies" con una lista de pasatiempos
    "ciudad": "Madrid"                      # Clave "ciudad" con el valor "Madrid"
}

# Se imprimen los diccionarios antes de la actualización
print(f"Diccionario 1 Antes de Actualizar: {dicc1}")
print(f"Diccionario 2: {dicc2}")

# Se actualiza dicc1 con los valores de dicc2
dicc1.update(dicc2)

# Se imprime dicc1 después de la actualización
print(f"\nDiccionario 1 Después de Actualizar: {dicc1}")