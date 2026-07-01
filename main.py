import json

from hash_map import pokedex_nacional
from hash_set import medallas_iniciales
from entrenador import Entrenador, GIMNASIOS


def menu():
    print("\n" + "=" * 40)
    print("         POKÉMON HUERGO")
    print("=" * 40)
    print("1.  Ver Pokédex")
    print("2.  Ver Equipo Principal")
    print("3.  Ver PC")
    print("4.  Ver Medallas")
    print("5.  Capturar nuevo Pokémon")
    print("6.  Ordenar PC")
    print("7.  Buscar Pokémon en Equipo")
    print("8.  Enviar Pokémon al Centro Pokémon")
    print("9.  Transferir Pokémon al Profesor Oak")
    print("10. Deshacer última transferencia")
    print("11. Desafiar Líder de Gimnasio")
    print("12. Salir del sistema")


def submenu_ordenar_pc(entrenador):
    print("\n--- Ordenar PC ---")
    print("1. Alfabético (A-Z)")
    print("2. Por Tipo")
    print("3. Por PC (poder de combate)")
    print("0. Volver")
    op = input("Elegí una opción: ").strip()
    if op == "1":
        entrenador.ordenar_pc_por_nombre()
        entrenador.pc.mostrar()
    elif op == "2":
        entrenador.ordenar_pc_por_tipo()
        entrenador.pc.mostrar()
    elif op == "3":
        entrenador.ordenar_pc_por_poder()
        entrenador.pc.mostrar()
    elif op == "0":
        print("Volviendo al menú principal...")
    else:
        print("Opción inválida.")


def pausa():
    input("\nPresioná Enter para volver al menú principal...")


def main():
    print("Bienvenido a Pokémon Huergo")
    nombre = input("Nombre del entrenador: ").strip()

    try:
        pokedex = pokedex_nacional()
        medallas = medallas_iniciales()
    except FileNotFoundError as e:
        print(f"Error: no se encontró {e.filename}")
        return
    except (KeyError, json.JSONDecodeError):
        print("Error al leer los archivos JSON.")
        return

    entrenador = Entrenador(nombre, pokedex, medallas)

    while True:
        menu()
        opcion = input("\nElegí una opción: ").strip()

        try:
            if opcion == "12":
                print("¡Hasta luego!")
                break
            elif opcion == "1":
                pokedex.mostrar()
                consulta = input("\n¿Consultar Pokémon? (s/n): ").strip().lower()
                if consulta == "s":
                    dato = input("Id o nombre a consultar: ").strip()
                    entrenador.consultar_pokedex(dato)
            elif opcion == "2":
                entrenador.mostrar_equipo()
                pausa()
            elif opcion == "3":
                entrenador.pc.mostrar()
                pausa()
            elif opcion == "4":
                medallas.mostrar()
                pausa()
            elif opcion == "5":
                poke = entrenador.encontrar_pokemon_salvaje()
                entrenador.intentar_capturar(poke)
                pausa()
            elif opcion == "6":
                submenu_ordenar_pc(entrenador)
            elif opcion == "7":
                nom = input("Nombre del Pokémon: ").strip()
                entrenador.buscar_en_equipo(nom)
                pausa()
            elif opcion == "8":
                entrenador.sanar_equipo()
                pausa()
            elif opcion == "9":
                entrenador.pc.mostrar()
                idx = int(input("Número en la PC a transferir: "))
                entrenador.transferir_a_oak(idx)
                pausa()
            elif opcion == "10":
                entrenador.deshacer_transferencia()
                pausa()
            elif opcion == "11":
                print("\nGimnasios disponibles:")
                for i, g in enumerate(GIMNASIOS, 1):
                    print(f"  {i}. {g['ciudad']} - {g['lider']}")
                num = int(input("Elegí un gimnasio (1-8): "))
                if 1 <= num <= len(GIMNASIOS):
                    gimnasio = GIMNASIOS[num - 1]
                    entrenador.desafiar_gimnasio(gimnasio["medalla"])
                else:
                    print("Gimnasio inválido.")
                pausa()
            else:
                print("Opción inválida.")
                pausa()
        except ValueError:
            print("Entrada inválida. Usá números donde corresponda.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()