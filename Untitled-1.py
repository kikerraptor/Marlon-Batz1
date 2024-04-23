def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    # Ingresa un PIN
    pin = input("Ingresa un PIN de 8 dígitos sin empezar con 0 y con al menos un número primo: ")

    # Validar el PIN con condicionales
    if not pin.isdigit():
        print("Error: El PIN debe ser numérico.")
    elif len(pin) != 8:
        print("Error: El PIN debe tener exactamente 8 dígitos.")
    elif pin[0] == '0':
        print("Error: El PIN no puede empezar con 0.")
    elif not any(es_primo(int(digito)) for digito in pin):
        print("Error: El PIN debe contener al menos un número primo.")
    else:
        print("PIN válido.")

except ValueError:
    print("Error: Ingresa un PIN numérico de 8 dígitos.")
