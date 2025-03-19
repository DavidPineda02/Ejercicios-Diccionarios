# 3. Cuál es la función que permite eliminar algún elemento del diccionario.

cosasFav = {
    "color": "Negro",
    "comida": "Papas Locas",
    "deporte": "Baloncesto"
}

valrElimn = cosasFav.pop("comida")

print(f"Diccionario: {cosasFav}")
print(f"Valor eliminado: {valrElimn}")
print(f"Diccionario después de la eliminación: {cosasFav}")