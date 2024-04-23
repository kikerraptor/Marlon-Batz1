#numeros decendentes y acendentes
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

numeros = [numero1, numero2, numero3]

print("decendente",sorted(numeros, reverse=True))
print("decendente",sorted(numeros))
