def jugar_piedra_papel_tijera(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        return "¡Jugador 1 gana!"
    else:
        return "¡Jugador 2 gana!"

# Mensaje de bienvenida
print("Bienvenido al juego de Piedra, Papel o Tijera para dos jugadores.")

while True:
    # Elección del jugador 1
    jugador1 = input("Jugador 1, elige piedra, papel o tijera (o 'salir' para terminar el juego): ").lower()

    # Salir del juego si el jugador 1 lo desea
    if jugador1 == "salir":
        print("Gracias por jugar. ¡Hasta luego!")
        break

    # Verificar si la elección del jugador 1 es válida
    if jugador1 not in ("piedra", "papel", "tijera"):
        print("Por favor, elige una opción válida.")
        continue

    # Elección del jugador 2
    jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

    # Verificar si la elección del jugador 2 es válida
    if jugador2 not in ("piedra", "papel", "tijera"):
        print("Por favor, elige una opción válida.")
        continue

    # Mostrar las elecciones y el resultado del juego
    print(f"Jugador 1 eligió: (jugador1)")
    print(f"Jugador 2 eligió: (jugador2)")
    print(jugar_piedra_papel_tijera(jugador1, jugador2))

