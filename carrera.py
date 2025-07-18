import os

def solicitar_jugadores():
    while True:
        try:
            jugadores = int(input("Ingrese la cantidad de jugadores (2 a 4): "))
            if 2 <= jugadores <= 4:
                return jugadores
            else:
                print("Deben ser entre 2 y 4 jugadores.")
        except ValueError:
            print("Ingrese un número válido.")

def seleccionar_nivel():
    niveles = {
        1: 20,
        2: 30,
        3: 50,
        4: 100
    }
    print("\nSeleccione el nivel de tablero:")
    print("1. Básico (20 posiciones)")
    print("2. Intermedio (30 posiciones)")
    print("3. Avanzado (50 posiciones)")
    print("4. Experto (100 posiciones)")
    while True:
        try:
            nivel = int(input("Ingrese el número de nivel (1 a 4): "))
            if nivel in niveles:
                return niveles[nivel]
            else:
                print(" Opción no válida.")
        except ValueError:
            print(" Ingrese un número válido.")

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def jugar():
    cantidad_jugadores = solicitar_jugadores()
    meta = seleccionar_nivel()
    posiciones = [0] * cantidad_jugadores
    historial_pares = [0] * cantidad_jugadores
    turno = 0

    print(f"\n¡Comienza la Carrera Numérica! Meta: {meta} posiciones\n")

    while True:
        jugador = turno % cantidad_jugadores
        input(f"Turno del Jugador {jugador + 1}. Presiona Enter para lanzar los dados...")
        dado1, dado2 = lanzar_dados()
        print(f" Dados: {dado1} y {dado2}")

        if dado1 == dado2:
            historial_pares[jugador] += 1
            print(f" ¡Par conseguido! Total consecutivos: {historial_pares[jugador]}")
            if historial_pares[jugador] == 3:
                print(f"🎉 Jugador {jugador + 1} ganó por obtener 3 pares consecutivos.")
                break
        else:
            historial_pares[jugador] = 0

        posiciones[jugador] += dado1 + dado2
        print(f" Posición actual Jugador {jugador + 1}: {posiciones[jugador]}/{meta}\n")

        if posiciones[jugador] >= meta:
            print(f" Jugador {jugador + 1} ha llegado a la meta y gana el juego.")
            break

        turno += 1

if __name__ == "__main__":
    jugar()