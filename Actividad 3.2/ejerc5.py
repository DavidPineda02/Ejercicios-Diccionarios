# 5. Función que permite eliminar todos los elementos de un diccionario 

persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Barcelona",
    "ocupacion": "Ingeniera",
    "hobbies": ["lectura", "ciclismo", "viajar"],
    "direccion": {
        "calle": "Calle de la Paz",
        "numero": 10,
    }
}

print("\nDiccionario Completo: ")
print(persona)

persona.clear()

print("\nDiccionario Eliminado: ")
print(persona)