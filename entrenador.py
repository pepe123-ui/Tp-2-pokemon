import random
from estructuras import ListaEnlazada, Cola, Pila
from algoritmos import (
    bubble_sort_nombre,
    insertion_sort_tipo,
    quick_sort_poder,
    busqueda_lineal,
    busqueda_binaria,
)

GIMNASIOS = [
    {"ciudad": "Ciudad Plateada", "lider": "Brock", "medalla": "Medalla Roca"},
    {"ciudad": "Ciudad Celeste", "lider": "Misty", "medalla": "Medalla Cascada"},
    {"ciudad": "Ciudad Carmín", "lider": "Lt. Surge", "medalla": "Medalla Trueno"},
    {"ciudad": "Ciudad Azulona", "lider": "Erika", "medalla": "Medalla Arcoíris"},
    {"ciudad": "Ciudad Fucsia", "lider": "Koga", "medalla": "Medalla Alma"},
    {"ciudad": "Ciudad Azafrán", "lider": "Sabrina", "medalla": "Medalla Pantano"},
    {"ciudad": "Isla Canela", "lider": "Blaine", "medalla": "Medalla Volcán"},
    {"ciudad": "Ciudad Verde", "lider": "Giovanni", "medalla": "Medalla Tierra"},
]


class Entrenador:
    MAX_EQUIPO = 6

    def __init__(self, nombre, pokedex, medallas):
        self.nombre = nombre
        self.pokedex = pokedex
        self.medallas = medallas
        self.equipo = []
        self.pc = ListaEnlazada()
        self.pila_transferencias = Pila(maximo=5)
        self._ids_ordenados = sorted(pokedex.obtener_ids())

    def capturar(self, pokemon):
        if len(self.equipo) < self.MAX_EQUIPO:
            self.equipo.append(pokemon)
            print(f"{pokemon.nombre} se unió al equipo.")
        else:
            self.pc.agregar(pokemon)
            print(f"Equipo lleno. {pokemon.nombre} fue enviado a la PC.")

    def encontrar_pokemon_salvaje(self):
        return self.pokedex.obtener_aleatorio()

    def intentar_capturar(self, pokemon, prob_captura=0.6):
        if pokemon is None:
            print("No hay Pokémon disponibles en la Pokédex.")
            return
        print(f"\n¡Un {pokemon.nombre} salvaje apareció!")
        opcion = input("¿Querés intentar capturarlo? (s/n): ").strip().lower()
        if opcion not in {"s", "si"}:
            print(f"Decidiste dejar escapar a {pokemon.nombre}.")
            return
        print("Lanzás una Pokéball...")
        if random.random() < prob_captura:
            print(f"¡Genial! {pokemon.nombre} fue capturado.")
            self.capturar(pokemon)
        else:
            print(f"¡Oh no! {pokemon.nombre} no se dejó capturar.")

    def mostrar_equipo(self):
        print(f"\n--- Equipo de {self.nombre} ({len(self.equipo)}/{self.MAX_EQUIPO}) ---")
        if not self.equipo:
            print("  (vacío)")
            return
        for i, poke in enumerate(self.equipo, 1):
            print(f"  {i}. {poke}")

    def sanar_equipo(self):
        if not self.equipo:
            print("No hay Pokémon en el equipo.")
            return
        cola = Cola()
        for poke in self.equipo:
            cola.encolar(poke)
        print("\nCentro Pokémon - curando equipo...")
        while not cola.vacia():
            poke = cola.desencolar()
            print(f"  Curando a {poke.nombre}... ¡Listo!")
        print("¡Tu equipo está en perfectas condiciones!")

    def transferir_a_oak(self, indice):
        poke = self.pc.eliminar_en(indice - 1)
        if poke is None:
            print("Índice inválido.")
            return
        self.pila_transferencias.apilar(poke)
        print(f"{poke.nombre} fue transferido al Profesor Oak.")

    def deshacer_transferencia(self):
        poke = self.pila_transferencias.desapilar()
        if poke is None:
            print("No hay transferencias para deshacer.")
            return
        self.pc.agregar(poke)
        print(f"{poke.nombre} regresó a la PC.")

    def desafiar_gimnasio(self, medalla):
        if self.medallas.buscar(medalla):
            print("Ya has ganado esta medalla. No puedes desafiarlo de nuevo.")
            return
        print(f"Desafíando a {medalla}...")
        if random.choice([True, False]):
            print("¡Ganaste la batalla!")   
            self.medallas.agregar(medalla)
            print(f"Has ganado la medalla {medalla}.")
        else:
            print("Perdiste la batalla. Entrená un poco más.")
    def ordenar_pc_por_nombre(self):
        lista = bubble_sort_nombre(self.pc.a_lista())
        self.pc.reconstruir(lista)
        print("PC ordenada alfabéticamente (A-Z).")

    def ordenar_pc_por_tipo(self):
        lista = insertion_sort_tipo(self.pc.a_lista())
        self.pc.reconstruir(lista)
        print("PC ordenada por tipo.")

    def ordenar_pc_por_poder(self):
        lista = quick_sort_poder(self.pc.a_lista())
        self.pc.reconstruir(lista)
        print("PC ordenada por poder de combate (mayor a menor).")

    def buscar_en_equipo(self, nombre):
        pos = busqueda_lineal(self.equipo, nombre)
        if pos >= 0:
            print(f"Encontrado en el equipo: {self.equipo[pos]}")
        else:
            print(f'"{nombre}" no está en el equipo.')

    def consultar_pokedex(self, busqueda):
        busqueda = busqueda.strip()
        if busqueda.isdigit():
            id_buscado = int(busqueda)
            pos = busqueda_binaria(self._ids_ordenados, id_buscado)
            if pos == -1:
                print(f"El id {id_buscado} no está registrado en la Pokédex.")
                return
            poke = self.pokedex.buscar(id_buscado)
        else:
            poke = self.pokedex.buscar_por_nombre(busqueda)
            if poke is None:
                print(f'"{busqueda}" no está registrado en la Pokédex.')
                return
        print(f"Encontrado: {poke}")

    def obtener_pokemon(self, busqueda):
        busqueda = busqueda.strip()
        if busqueda.isdigit():
            return self.pokedex.buscar(int(busqueda))
        return self.pokedex.buscar_por_nombre(busqueda)