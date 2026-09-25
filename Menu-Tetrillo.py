import sys


def mostrar_menu():
    print("\n====================")
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
            print("\n¡Iniciando el juego...")
            # Aquí iría el código principal de tu juego
            break
        elif opcion == "2":
            print("\n--- CONTROLES ---")
            print("Flechas Izq/Der: Mover")
            print("Flecha Arriba  : Rotar")
            print("Flecha Abajo   : Bajar rápido")
            input("\nPresiona Enter para volver...")
        elif opcion == "3":
            print("\n¡Hasta luego!")
            sys.exit()
        else:
            print("\nOpción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()