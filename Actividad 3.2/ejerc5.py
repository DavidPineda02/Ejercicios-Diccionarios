# 5. Función que permite eliminar todos los elementos de un diccionario 

# Se crea un diccionario con información sobre una persona
persona = {
    "nombre": "Ana",                      # Clave "nombre" con el valor "Ana"
    "edad": 28,                            # Clave "edad" con el valor 28
    "ciudad": "Barcelona",                 # Clave "ciudad" con el valor "Barcelona"
    "ocupacion": "Ingeniera",              # Clave "ocupacion" con el valor "Ingeniera"
    "hobbies": ["lectura", "ciclismo", "viajar"],  # Lista de hobbies
    "direccion": {                         # Diccionario anidado con la dirección
        "calle": "Calle de la Paz",
        "numero": 10,
    }
}

# Se imprime el diccionario completo antes de eliminarlo
print("\nDiccionario Completo: ")
print(persona)

# Se vacía el diccionario usando el método clear()
persona.clear()

# Se imprime el diccionario después de eliminar todos sus elementos
print("\nDiccionario Eliminado: ")
print(persona)