# Obtener los valores de entrada
primer_valor = int(input("Ingrese el primer valor (multiplicador): "))
segundo_valor = int(input("Ingrese el segundo valor (hasta qué tabla): "))
tercer_valor = int(input("Ingrese el tercer valor (hasta qué número se multiplicará): "))

# Generar la tabla de multiplicación
for tabla in range(1, segundo_valor + 1):
    print(f"Tabla del {tabla}:")
    for numero in range(1, tercer_valor + 1):
        resultado = tabla * numero
        print(f"{tabla} x {numero} = {resultado}")
    print()