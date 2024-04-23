# Tamaño del cubo
tamaño = 5

# Crear el cubo
for i in range(tamaño):
    for j in range(tamaño):
        for k in range(tamaño):
            if i == 0 or i == tamaño - 1 or j == 0 or j == tamaño - 1 or k == 0 or k == tamaño - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()