#8. Función que permite añadir los elementos de un diccionario a otro. 

dicc1 = {
    "nombre": "David",
    "edad": 19,
    "ciudad": "Piedecuesta"
}

dicc2 = {
    "ocupacion": "Ingeniera",
    "hobbies": ["Baloncesto", "Codificar"],
    "ciudad": "Madrid"
}

print(f"Diccionario 1 Antes de Actualizar: {dicc1}")
print(f"Diccionario 2: {dicc2}")

dicc1.update(dicc2)

print(f"\nDiccionario 1 Despues de Actualizar: {dicc1}")