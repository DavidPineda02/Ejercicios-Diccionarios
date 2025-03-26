# Método items()

# Se crea un diccionario con los nombres de los aprendices y sus respectivas notas
notasAprend = {
    "Michelle": 8,  
    "Ximena": 57,   
    "David": 87,    
    "Jensen": 90,   
    "Nicolas": 32,  
    "Edwar": 94     
}

# Se define la nota mínima para aprobar
notaMin = 70

# Se crea un diccionario vacío para almacenar los aprobados
aprobados = {}

# Se recorren las notas de los aprendices y se almacenan los que aprobaron
for nombre, nota in notasAprend.items():
    if nota > notaMin:  # Se verifica si la nota es mayor que la nota mínima
        aprobados[nombre] = nota # Se agrega al diccionario 'aprobados' el aprendiz que cumple con la condición usando su nombre como clave y su nota como valor.

# Se imprime un encabezado indicando los aprendices aprobados
print(f"===== Aprendices Aprobados (Nota Mínima {notaMin}) =====\n")

# Se recorren los aprobados y se muestran sus nombres y notas
for aprendiz, nota in aprobados.items():
    print(f"{aprendiz}: {nota}")

# Se imprime una línea de cierre para la lista
print(f"\n==================================================")
