# Conozca si tiene que declarar el impuesto de renta desde el próximo año, según sus ingresos mensuales, si sus ingresos mensuales son mayores de 3.000.000 se le deberá cobrar 250.000 más la  implementación de un IVA del 18% de los ingresos mensuales, si los ingresos mensuales son menores a 3.000.000 se le cobrara 200.000 más la implementación del IVA aproximadamente del 10% de sus ingresos mensuales. 

def calculoImpuestos(cantIngreso):
    iva = 0  # Variable para almacenar el IVA calculado
    impuestoFijo = 0  # Variable para almacenar el impuesto fijo
    totlImpuesto = 0  # Variable para almacenar el total de impuestos

    # Calcula el IVA y el impuesto fijo según el ingreso
    if cantIngreso > 3000000:  # Si los ingresos superan los 3,000,000
        iva = cantIngreso * 0.18  # Calcula el IVA al 18%
        impuestoFijo = 250000  # Fija el impuesto base en 250,000
    else:  # Si los ingresos son menores o iguales a 3,000,000
        iva = cantIngreso * 0.10  # Calcula el IVA al 10%
        impuestoFijo = 200000  # Fija el impuesto base en 200,000

    # Calcula el total de impuestos sumando el IVA y el impuesto fijo
    totlImpuesto = impuestoFijo + iva

    # Crea un diccionario con los detalles de los impuestos
    diccImpuestos = {
        "ingresos": cantIngreso,  # Guarda los ingresos
        "iva": iva,  # Guarda el IVA calculado
        "impuestoFijo": impuestoFijo,  # Guarda el impuesto fijo
        "totalImpuesto": totlImpuesto  # Guarda el total de impuestos
    }

    return diccImpuestos  # Retorna el diccionario con los detalles

print("======== Declarar Impuestos ========")
cantIngreso = int(input("\nDigite la Cantidad de Ingresos al Mes: "))  # Solicita los ingresos mensuales

# Calcula los impuestos llamando a la función
diccImpuestos = calculoImpuestos(cantIngreso)

# Muestra los resultados de los impuestos calculados
print("\n----- Calculo de Impuestos -----\n")
for clave, valor in diccImpuestos.items():  # Itera sobre el diccionario de impuestos
    print(f"{clave.capitalize()}: {valor:.0f}")  # Muestra cada clave y su valor formateado
print("\n====================================")