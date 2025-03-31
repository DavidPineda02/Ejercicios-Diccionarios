# Realizar un algoritmo el cual sume los ingresos de una empresa mensualmente, teniendo en cuenta  que se debe saber de qué son las ganancias y se debe pedir al usuario de cuánto dinero total se  obtuvo de esa ganancia, al final se deberá saber si las ganancias son mayores a las ganancias del  año pasado, entonces imprimir en pantalla que se obtuvieron más ganancias y hacer la respectiva  operación para saber de cuanta diferencia fue la ganancia, si las ganancias son menores a las  ganancias del año pasado imprimir en pantalla el faltante de ganancias para completar las ganancias  del año pasado. GANANCIAS: Pedir al usuario que ingrese las ganancias del año pasado. 

def ingresoGanancias():
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    ganancsMensuales = {}  # Diccionario para almacenar las ganancias mensuales

    print("\nDigite las Ganancias Mensuales:\n")
    for mes in meses:  # Itera sobre los 12 meses del año
        while True:  # Bucle para validar que las ganancias sean positivas
            ingreso = int(input(f"Digite las Ganancias de {mes}: "))  # Solicita las ganancias del mes actual
            if ingreso >= 0:  # Verifica que el ingreso sea positivo
                ganancsMensuales[mes] = ingreso  # Guarda las ganancias en el diccionario
                break
            else:
                print("\nDigite un Valor Positivo.")  # Mensaje de error si el valor es negativo
    return ganancsMensuales  # Retorna el diccionario con las ganancias mensuales


def compararGanancs(totlActual, totlPasd):
    if totlActual > totlPasd:  # Si las ganancias actuales son mayores
        diferencia = totlActual - totlPasd
        print(f"\nEste Año se Obtuvieron mas Ganancias.")
        print(f"Diferencia Positiva: ${diferencia}")
        print("\n=================================================")
    elif totlActual < totlPasd:  # Si las ganancias actuales son menores
        faltante = totlPasd - totlActual
        print(f"\nEste Año las Ganancias Fueron Menores.")
        print(f"Faltante para Igualar las Ganancias del Año Pasado: ${faltante}")
        print("\n=================================================")
    else:  # Si las ganancias son iguales
        print("\nLas Ganancias de este Año son Iguales a las del Año Pasado.")
        print("\n=================================================")


print("======== Ganancias Positivas o Negativas ========")
while True:
    # Solicita las ganancias totales del año pasado
    ganancsPasadas = int(input("\nDigite las Ganancias Totales del Año Pasado: "))
    
    if ganancsPasadas >= 0:  # Verifica que las ganancias sean positivas
        # Llama a la función para ingresar las ganancias mensuales del año actual
        ganancsActuales = ingresoGanancias()
        
        # Calcula el total de ganancias del año actual sumando los valores del diccionario
        totlActual = sum(ganancsActuales.values())
        
        # Compara las ganancias del año actual con las del año pasado
        compararGanancs(totlActual, ganancsPasadas)
        break
    else:
        print("\nDigite un Valor Positivo.")  # Mensaje de error si el valor es negativo