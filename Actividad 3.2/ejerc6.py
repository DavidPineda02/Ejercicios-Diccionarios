# 6. print(direccion_datos.values()) # cual es el uso de esta función incorporar a un ejercicio.  

# Se crea un diccionario con información personal y de dirección
datosPerso = {
    "nombre": "Carlos",                     # Clave "nombre" con el valor "Carlos"
    "calle": "Avenida de la Libertad",      # Clave "calle" con el nombre de la calle
    "número": 25,                           # Clave "número" con el número de la dirección
    "ciudad": "Madrid",                     # Clave "ciudad" con la ciudad de residencia
    "código_postal": "28001",               # Clave "código_postal" con el código postal
    "país": "España"                        # Clave "país" con el nombre del país
}

# Se imprime un mensaje indicando que se mostrarán los valores del diccionario
print("Los valores de la dirección son:")

# Se usa el método values() para obtener solo los valores del diccionario
print(datosPerso.values())