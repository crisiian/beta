import random

def solicitar_cantidad_jugadores():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de jugadores (2-4): "))
            if 2 <= cantidad <= 4:
                return cantidad
            else:
                print("Error: Debe ser entre 2 y 4 jugadores.")
        except ValueError:
            print("Error: Ingrese un número válido.")

def mostrar_menu_niveles():
    print("\nNiveles disponibles:")
    print("1. Nivel básico (Tablero de 20 posiciones)")
    print("2. Nivel intermedio (Tablero de 30 posiciones)")
    print("3. Nivel avanzado (Tablero de 50 posiciones)")
    print("4. Nivel experto (Tablero de 100 posiciones)")

def solicitar_nivel():
    while True:
        try:
            nivel = int(input("Seleccione el nivel (1-4): "))
            if 1 <= nivel <= 4:
                return nivel
            else:
                print("Error: Seleccione un nivel entre 1 y 4.")
        except ValueError:
            print("Error: Ingrese un número válido.")

def obtener_meta(nivel):
    niveles = {
        1: 20,
        2: 30,
        3: 50,
        4: 100
    }
    return niveles[nivel]

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def jugar_carrera_numérica():
    print("=== CARRERA NUMÉRICA ===")
    
    # Solicitar cantidad de jugadores
    cantidad_jugadores = solicitar_cantidad_jugadores()
    jugadores = [f"Jugador {i+1}" for i in range(cantidad_jugadores)]
    posiciones = [0] * cantidad_jugadores
    pares_consecutivos = [0] * cantidad_jugadores
    
    # Seleccionar nivel y determinar meta
    mostrar_menu_niveles()
    nivel = solicitar_nivel()
    meta = obtener_meta(nivel)
    
    print(f"\n¡Comienza el juego! Meta: posición {meta}")
    
    turno = 0
    ganador = None
    
    while not ganador:
        jugador_actual = turno % cantidad_jugadores
        nombre_jugador = jugadores[jugador_actual]
        posicion_actual = posiciones[jugador_actual]
        
        input(f"\nTurno de {nombre_jugador} (ENTER para lanzar dados)...")
        dado1, dado2 = lanzar_dados()
        suma = dado1 + dado2
        
        print(f"Resultado de dados: {dado1} y {dado2} (Total: {suma})")
        
        # Verificar si son pares iguales
        if dado1 == dado2:
            pares_consecutivos[jugador_actual] += 1
            print(f"¡Par encontrado! ({pares_consecutivos[jugador_actual]} consecutivos)")
            
            # Verificar si tiene 3 pares consecutivos
            if pares_consecutivos[jugador_actual] >= 3:
                ganador = nombre_jugador
                print(f"¡{nombre_jugador} ha obtenido 3 pares consecutivos!")
                break
        else:
            pares_consecutivos[jugador_actual] = 0
        
        # Mover jugador
        nueva_posicion = posicion_actual + suma
        posiciones[jugador_actual] = nueva_posicion
        
        print(f"{nombre_jugador} avanza de {posicion_actual} a {nueva_posicion}")
        
        # Verificar si llegó a la meta
        if nueva_posicion >= meta:
            ganador = nombre_jugador
            print(f"¡{nombre_jugador} ha llegado a la meta!")
            break
        
        turno += 1
    
    print(f"\n¡FELICITACIONES {ganador}! ¡Has ganado el juego!")

# Iniciar el juego
if __name__ == "__main__":
    jugar_carrera_numérica()