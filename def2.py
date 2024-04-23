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

def mostrar_resultados(medida):
    print(f"{medida} pies equivale a:")
    print(f"  - {pies_a_yardas(medida):.2f} yardas")
    print(f"  - {pies_a_centimetros(medida):.2f} centímetros")
    print(f"  - {pies_a_pulgadas(medida):.2f} pulgadas")
    print()
    print(f"{medida} yardas equivale a:")
    print(f"  - {yardas_a_pies(medida):.2f} pies")
    print(f"  - {yardas_a_centimetros(medida):.2f} centímetros")
    print(f"  - {yardas_a_pulgadas(medida):.2f} pulgadas")
    print()
    print(f"{medida} centímetros equivale a:")
    print(f"  - {cm_a_pies(medida):.2f} pies")
    print(f"  - {cm_a_yardas(medida):.2f} yardas")
    print(f"  - {cm_a_pulgadas(medida):.2f} pulgadas")
    print()
    print(f"{medida} pulgadas equivale a:")
    print(f"  - {pulgadas_a_pies(medida):.2f} pies")
    print(f"  - {pulgadas_a_yardas(medida):.2f} yardas")
    print(f"  - {pulgadas_a_centimetros(medida):.2f} centímetros")

def convertir():
    medida = float(input("Ingrese la medida: "))
    mostrar_resultados(medida)

# Realizar la conversión
convertir()