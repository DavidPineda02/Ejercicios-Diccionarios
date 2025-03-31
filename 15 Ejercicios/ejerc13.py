# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes. 

def calculoAhorroAnual():
    # Diccionario para almacenar los ahorros de cada mes
    ahorrosMensuales = {}
    print("========== Ahorro Anual ==========")
    print("\nDigite la Cantidad Ahorrada Cada Mes:")
    
    # Lista de nombres de los meses
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    for mes in meses:  # Itera sobre los 12 meses del año
        while True:  # Bucle para validar la entrada
            cantidad = float(input(f"\n{mes}: "))
            
            if cantidad >= 0:  # Verifica que la cantidad no sea negativa
                break  # Sale del bucle si la cantidad es válida
            else:
                print("\nLa Cantidad Ingresada no puede ser Negativa. Intente de Nuevo.")

        # Guarda el mes y la cantidad ahorrada en el diccionario
        ahorrosMensuales[mes] = cantidad
    
    # Calcula el total ahorrado sumando los valores del diccionario
    totalAhorrado = sum(ahorrosMensuales.values())
    
    # Muestra un resumen de los ahorros mensuales
    print("\nResumen de Ahorros Mensuales:\n")
    for mes, cantidad in ahorrosMensuales.items():  # Itera sobre el diccionario
        print(f"{mes}: ${cantidad:.0f}")  # Muestra el mes y la cantidad ahorrada
    
    # Muestra el total ahorrado al final del año
    print(f"\nTotal Ahorrado al Final del Año: ${totalAhorrado:.0f}")
    print("\n==================================")

# Ejecuta la función principal
calculoAhorroAnual()