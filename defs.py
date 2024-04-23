def pies_a_yardas(pies):
    return pies * 0.333333

def pies_a_centimetros(pies):
    return pies * 30.48

def pies_a_pulgadas(pies):
    return pies * 12

def yardas_a_pies(yardas):
    return yardas * 3

def yardas_a_centimetros(yardas):
    return yardas * 91.44

def yardas_a_pulgadas(yardas):
    return yardas * 36

def cm_a_pies(centimetros):
    return centimetros / 30.48

def cm_a_yardas(centimetros):
    return centimetros / 91.44

def cm_a_pulgadas(centimetros):
    return centimetros / 2.54

def pulgadas_a_pies(pulgadas):
    return pulgadas / 12

def pulgadas_a_yardas(pulgadas):
    return pulgadas / 36

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

def mostrar_menu():
    print("1. Pies")
    print("2. Yardas")
    print("3. Centímetros")
    print("4. Pulgadas")

def convertir():
    medida = float(input("Ingrese la medida: "))
    opcion_origen = int(input("Seleccione la medida de origen (1-4): "))
    opcion_destino = int(input("Seleccione la medida de destino (1-4): "))
    
    if opcion_origen == opcion_destino:
        print("La medida de origen y destino son iguales. No es necesaria la conversión.")
        return
    
    if opcion_origen == 1:
        medida_origen = "pies"
    elif opcion_origen == 2:
        medida_origen = "yardas"
    elif opcion_origen == 3:
        medida_origen = "centímetros"
    elif opcion_origen == 4:
        medida_origen = "pulgadas"
        
    if opcion_destino == 1:
        medida_destino = "pies"
    elif opcion_destino == 2:
        medida_destino = "yardas"
    elif opcion_destino == 3:
        medida_destino = "centímetros"
    elif opcion_destino == 4:
        medida_destino = "pulgadas"
    
    if opcion_origen == 1:
        valor_origen = medida
    elif opcion_origen == 2:
        valor_origen = yardas_a_pies(medida)
    elif opcion_origen == 3:
        valor_origen = cm_a_pies(medida)
    elif opcion_origen == 4:
        valor_origen = pulgadas_a_pies(medida)
    
    if opcion_destino == 1:
        resultado = valor_origen
    elif opcion_destino == 2:
        resultado = pies_a_yardas(valor_origen)
    elif opcion_destino == 3:
        resultado = pies_a_centimetros(valor_origen)
    elif opcion_destino == 4:
        resultado = pies_a_pulgadas(valor_origen)
    
    print(f"{medida} {medida_origen} equivale a {resultado:.2f} {medida_destino}")

# Mostrar el menú
print("Conversor de medidas:")
mostrar_menu()

# Realizar la conversión
convertir()