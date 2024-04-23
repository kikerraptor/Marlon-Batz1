def sumar_numeros_mitades(lista):
    # Verificar si la longitud de la lista es par
    if len(lista) % 2 != 0:
        return "Incorrecto: La longitud de la lista no es par"

    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    mitad1 = lista[:mitad]
    mitad2 = lista[mitad:]

    # Calcular la suma de ambas mitades
    suma_mitad1 = sum(mitad1)
    suma_mitad2 = sum(mitad2)

    # Verificar si la suma de las dos mitades es un número par
    if (suma_mitad1 + suma_mitad2) % 2 == 0:
        return f"Suma de las dos mitades: {suma_mitad1 + suma_mitad2}. Mitad 1: {suma_mitad1}, Mitad 2: {suma_mitad2}. ¡Correcto!"
    else:
        return f"Suma de las dos mitades: {suma_mitad1 + suma_mitad2}. Mitad 1: {suma_mitad1}, Mitad 2: {suma_mitad2}. Incorrecto: La suma no es un número par"

# Ingresa una secuencia de números separados por espacios
numeros = input("Ingresa una secuencia de números separados por espacios: ").split()

# Convierte los números a enteros
numeros = [int(numero) for numero in numeros]

# Llama a la función para verificar la suma de las mitades
resultado = sumar_numeros_mitades(numeros)

# Imprime el resultado
print(resultado)