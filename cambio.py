def calcular_cambio(total, pago):
    if pago < total:
        return "El pago es insuficiente."
    else:
        cambio = pago - total
        return cambio

# Función para obtener un número válido desde el usuario
def obtener_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero >= 0:
                return numero
            else:
                print("Por favor, ingresa un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Obtener el monto de compra y la cantidad pagada
monto_compra = obtener_numero("Ingresa el monto de compra: Q")
monto_pagado = obtener_numero("Ingresa la cantidad pagada: Q")

# Calcular el cambio y mostrarlo
cambio = calcular_cambio(monto_compra, monto_pagado)
print("El cambio a devolver es: Q", cambio) if isinstance(cambio, float) else print(cambio)