# 3. Cuál es la función que permite eliminar algún elemento del diccionario.

# Se crea un diccionario con elementos favoritos
cosasFav = {
    "color": "Negro",        # Clave "color" con valor "Negro"
    "comida": "Papas Locas", # Clave "comida" con valor "Papas Locas"
    "deporte": "Baloncesto"  # Clave "deporte" con valor "Baloncesto"
}

# Se elimina el elemento con clave "comida" y se almacena su valor en 'valrElimn'
valrElimn = cosasFav.pop("comida")

# Se imprimen los resultados
print(f"Diccionario: {cosasFav}")  # Se muestra el diccionario después de la eliminación
print(f"Valor eliminado: {valrElimn}")  # Se muestra el valor eliminado
print(f"Diccionario después de la eliminación: {cosasFav}")  # Se verifica nuevamente el diccionario