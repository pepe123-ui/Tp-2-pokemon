import json

from hash_map import cargar_pokedex
from hash_set import cargar_medallas_iniciales
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
    elif op != "0":
        print("Opción inválida.")


def main():
    print("Bienvenido a Pokémon Huergo")
    nombre = input("Nombre del entrenador: ").strip() or "Ash"

    try:
        pokedex = cargar_pokedex()
        medallas = cargar_medallas_iniciales(cantidad=2)
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
                consulta = input("\n¿Consultar por id? (s/n): ").strip().lower()
                if consulta == "s":
                    id_str = input("Id a consultar: ").strip()
                    entrenador.consultar_pokedex(int(id_str))
            elif opcion == "2":
                entrenador.mostrar_equipo()
            elif opcion == "3":
                entrenador.pc.mostrar()
            elif opcion == "4":
                medallas.mostrar()
            elif opcion == "5":
                id_str = input("Id del Pokémon a capturar: ").strip()
                poke = pokedex.buscar(int(id_str))
                if poke:
                    entrenador.capturar(poke)
                else:
                    print("Id no encontrado en la Pokédex.")
            elif opcion == "6":
                submenu_ordenar_pc(entrenador)
            elif opcion == "7":
                nom = input("Nombre del Pokémon: ").strip()
                entrenador.buscar_en_equipo(nom)
            elif opcion == "8":
                entrenador.sanar_equipo()
            elif opcion == "9":
                entrenador.pc.mostrar()
                idx = int(input("Número en la PC a transferir: "))
                entrenador.transferir_a_oak(idx)
            elif opcion == "10":
                entrenador.deshacer_transferencia()
            elif opcion == "11":
                print("\nGimnasios disponibles:")
                for i, g in enumerate(GIMNASIOS, 1):
                    print(f"  {i}. {g['ciudad']} - {g['lider']}")
                num = int(input("Elegí un gimnasio (1-8): "))
                entrenador.desafiar_gimnasio(num)
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida. Usá números donde corresponda.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
