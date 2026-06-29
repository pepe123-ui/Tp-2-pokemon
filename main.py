import json

from hash_map import cargar_pokedex
from hash_set import cargar_medallas_iniciales, HashSet
from entrenador import Entrenador, GIMNASIOS


def menu():
    print("\n" + "=" * 40)
    print("       POKÉMON HUERGO")
    print("=" * 40)
    print("1.  Ver Pokédex")
    print("2.  Ver medallas")
    print("3.  Capturar Pokémon (por id)")
    print("4.  Ver equipo")
    print("5.  Ver PC")
    print("6.  Sanar equipo (Centro Pokémon)")
    print("7.  Transferir Pokémon a Prof. Oak")
    print("8.  Deshacer última transferencia")
    print("9.  Desafiar gimnasio")
    print("10. Ordenar PC por nombre")
    print("11. Ordenar PC por tipo")
    print("12. Ordenar PC por poder de combate")
    print("13. Buscar Pokémon en equipo")
    print("14. Consultar Pokédex (búsqueda binaria)")
    print("15. Demo: intentar medalla duplicada")
    print("0.  Salir")


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
            if opcion == "0":
                print("¡Hasta luego!")
                break
            elif opcion == "1":
                pokedex.mostrar()
            elif opcion == "2":
                medallas.mostrar()
            elif opcion == "3":
                id_str = input("Id del Pokémon a capturar: ").strip()
                poke = pokedex.buscar(int(id_str))
                if poke:
                    entrenador.capturar(poke)
                else:
                    print("Id no encontrado en la Pokédex.")
            elif opcion == "4":
                entrenador.mostrar_equipo()
            elif opcion == "5":
                entrenador.pc.mostrar()
            elif opcion == "6":
                entrenador.sanar_equipo()
            elif opcion == "7":
                entrenador.pc.mostrar()
                idx = int(input("Número en la PC a transferir: "))
                entrenador.transferir_a_oak(idx)
            elif opcion == "8":
                entrenador.deshacer_transferencia()
            elif opcion == "9":
                print("\nGimnasios disponibles:")
                for i, g in enumerate(GIMNASIOS, 1):
                    print(f"  {i}. {g['ciudad']} - {g['lider']}")
                num = int(input("Elegí un gimnasio (1-8): "))
                entrenador.desafiar_gimnasio(num)
            elif opcion == "10":
                entrenador.ordenar_pc_por_nombre()
                entrenador.pc.mostrar()
            elif opcion == "11":
                entrenador.ordenar_pc_por_tipo()
                entrenador.pc.mostrar()
            elif opcion == "12":
                entrenador.ordenar_pc_por_poder()
                entrenador.pc.mostrar()
            elif opcion == "13":
                nom = input("Nombre del Pokémon: ").strip()
                entrenador.buscar_en_equipo(nom)
            elif opcion == "14":
                id_str = input("Id a consultar: ").strip()
                entrenador.consultar_pokedex(int(id_str))
            elif opcion == "15":
                medallas.agregar("Medalla Roca")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida. Usá números donde corresponda.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
