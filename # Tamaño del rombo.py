# Tamaño del rombo
tamaño = 123


# Parte de arriba del rombo
for i in range(tamaño):
    print(" " * (tamaño - i - 1) + "+" * (2 * i + 1))

# Parte de abajo del rombo del rombo
for i in range(tamaño - 2, -1, -1):
    print(" " * (tamaño - i - 1) + "+" * (2 * i + 1))