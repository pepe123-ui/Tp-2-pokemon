import json

class HashMap:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.buckets = []
        for i in range(tamaño):
            self.buckets.append([])

    def funcion_hash(self, key):
        return hash(key) % self.tamaño

    def agregar(self, key, value):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        for par in bucket:
            if par[0] == key:
                print("La key ya es existente.")
                return
        bucket.append([key, value])
        print(f"({key}, {value}) se agrego.")

    def buscar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        for par in bucket:
            if par[0] == key:
                return par[1]
        return None

    def mostrar(self):
        print("\n HASH MAP")
        for i in range(self.tamaño):
            print(f"Bucket {i}: {self.buckets[i]}")

def pokedex_nacional():
    pokedex=HashMap()
    with open('pokedex.json', 'r') as archivo:
        pokedex_data = json.load(archivo)
    for pokemon in pokedex_data:
        pokedex.agregar(pokemon['id'], pokemon)
        if  pokemon['id'] in pokedex:
            print(f"Pokemon con ID {pokemon['id']} ya existe en la pokedex.")
    return pokedex