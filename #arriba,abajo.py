#arriba,abajo
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

if numero1 >= numero2 >= numero3:
        descendente = [numero1, numero2, numero3]
elif numero1 >= numero3 >= numero2:
        descendente = [numero1, numero3, numero2]
elif numero2 >= numero1 >= numero3:
        descendente = [numero2, numero1, numero3]
elif numero2 >= numero3 >= numero1:
        descendente = [numero2, numero3, numero1]
elif numero3 >= numero1 >= numero2:
        descendente = [numero3, numero1, numero2]
else:
        descendente = [numero3, numero2, numero1]

ascendente = [max(numero1, numero2, numero3),
                  numero1 + numero2 + numero3 - min(numero1, numero2, numero3) - max(numero1, numero2, numero3),
                  min(numero1, numero2, numero3)]
print("Descendente:", descendente)
print("Ascendente:", ascendente)

