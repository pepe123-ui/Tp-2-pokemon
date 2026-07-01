import json
import random
from Clase import Pokemon


class HashMap:
    def __init__(self, tamaño=20):
        self.tamaño = tamaño
        self.buckets = []
        for i in range(tamaño):
            self.buckets.append([])

    def funcion_hash(self, key):
        return hash(key) % self.tamaño

    def agregar(self, key, value, silencioso=False):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        for par in bucket:
            if par[0] == key:
                if not silencioso:
                    print("La key ya es existente.")
                return False
        bucket.append([key, value])
        if not silencioso:
            print(f"({key}, {value}) se agrego.")
        return True

    def buscar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        for par in bucket:
            if par[0] == key:
                return par[1]
        return None

    def buscar_por_nombre(self, nombre):
        nombre = nombre.strip().lower()
        for bucket in self.buckets:
            for par in bucket:
                if par[1].nombre.lower() == nombre:
                    return par[1]
        return None

    def obtener_ids(self):
        ids = []
        for bucket in self.buckets:
            for par in bucket:
                ids.append(par[0])
        return ids

    def obtener_aleatorio(self):
        entradas = []
        for bucket in self.buckets:
            for par in bucket:
                entradas.append(par[1])
        if not entradas:
            return None
        return random.choice(entradas)

    def mostrar(self):
        print("\n--- Pokédex Nacional ---")
        entradas = []
        for bucket in self.buckets:
            for par in bucket:
                entradas.append(par)
        for key, pokemon in sorted(entradas, key=lambda item: item[0]):
            print(f"  {pokemon}")


def pokedex_nacional(archivo="pokedex.json"):
    pokedex = HashMap()
    with open(archivo, "r", encoding="utf-8") as f:
        datos = json.load(f)
    for item in datos:
        poke = Pokemon(item["id"], item["nombre"], item["tipo"], item["PC"])
        pokedex.agregar(poke.id, poke, silencioso=True)
    return pokedex