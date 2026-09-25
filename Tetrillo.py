import os
import random

# --- CONFIGURACIÓN Y PIEZAS ---
ANCHO = 8
ALTO = 10

PIEZAS = [
    [[1, 1, 1, 1]],  # Línea
    [[1, 1], [1, 1]],  # Cuadro
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
]


def crear_tablero():
    return [[" " for _ in range(ANCHO)] for _ in range(ALTO)]


def rotar(pieza):
    return [list(f) for f in zip(*pieza[::-1])]


def hay_choque(tablero, pieza, px, py):
    for y, fila in enumerate(pieza):
        for x, val in enumerate(fila):
            if val:
                nx, ny = px + x, py + y
                if nx < 0 or nx >= ANCHO or ny >= ALTO:
                    return True
                if ny >= 0 and tablero[ny][nx] != " ":
                    return True
    return False


def fijar_pieza(tablero, pieza, px, py):
    for y, fila in enumerate(pieza):
        for x, val in enumerate(fila):
            if val and py + y >= 0:
                tablero[py + y][px + x] = "#"


def limpiar_lineas(tablero):
    nuevo = [fila for fila in tablero if any(c == " " for c in fila)]
    puntos = (ALTO - len(nuevo)) * 100
    while len(nuevo) < ALTO:
        nuevo.insert(0, [" " for _ in range(ANCHO)])
    return nuevo, puntos


def dibujar(tablero, pieza, px, py, puntos):
    os.system("cls" if os.name == "nt" else "clear")
    copia = [fila[:] for fila in tablero]

    for y, fila in enumerate(pieza):
        for x, val in enumerate(fila):
            if val and 0 <= py + y < ALTO and 0 <= px + x < ANCHO:
                copia[py + y][px + x] = "#"

    print(f"PUNTOS: {puntos}")
    print("+" + "-" * (ANCHO * 2) + "+")
    for fila in copia:
        print("|" + " ".join(fila) + "|")
    print("+" + "-" * (ANCHO * 2) + "+")


# --- JUEGO ---
def jugar():
    tablero = crear_tablero()
    puntos = 0
    pieza = random.choice(PIEZAS)
    px, py = ANCHO // 2 - 1, 0

    while True:
        dibujar(tablero, pieza, px, py, puntos)

        print("\nMover: [A] Izq | [D] Der | [W] Rotar | [S] Bajar | [Q] Salir")
        momo = input("Tu movimiento + ENTER: ").lower()

        n_px, n_py, n_pieza = px, py, pieza

        if momo == "a":
            n_px -= 1
        elif momo == "d":
            n_px += 1
        elif momo == "w":
            n_pieza = rotar(pieza)
        elif momo == "s":
            n_py += 1
        elif momo == "q":
            break

        if not hay_choque(tablero, n_pieza, n_px, n_py):
            px, py, pieza = n_px, n_py, n_pieza

        if not hay_choque(tablero, pieza, px, py + 1):
            py += 1
        else:
            fijar_pieza(tablero, pieza, px, py)
            tablero, pts = limpiar_lineas(tablero)
            puntos += pts

            pieza = random.choice(PIEZAS)
            px, py = ANCHO // 2 - 1, 0

            if hay_choque(tablero, pieza, px, py):
                print("\n¡GAME OVER!")
                input("Presiona Enter para volver al menú...")
                break


# --- MENÚ PRINCIPAL ---
def mostrar_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("====================")
    print("      TETRIS        ")
    print("====================")
    print("1. Jugar")
    print("2. Controles")
    print("3. Salir")
    print("====================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("--- CONTROLES ---")
            print("A + Enter : Mover a la izquierda")
            print("D + Enter : Mover a la derecha")
            print("W + Enter : Rotar pieza")
            print("S + Enter : Bajar rápido")
            print("Q + Enter : Salir al menú")
            input("\nPresiona Enter para volver...")
        elif opcion == "3":
            print("\n¡Hasta luego!")
            break


if __name__ == "__main__":
    main()