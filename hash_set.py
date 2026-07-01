import json


class HashSet:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.buckets = []
        for i in range(tamaño):
            self.buckets.append([])

    def funcion_hash(self, key):
        return hash(key) % self.tamaño

    def agregar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        if key in bucket:
            print(f'"{key}" ya está en el registro de medallas.')
            return False
        bucket.append(key)
        print(f'"{key}" obtenida.')
        return True

    def buscar(self, key):
        indice = self.funcion_hash(key)
        bucket = self.buckets[indice]
        return key in bucket

    def __contains__(self, key):
        return self.buscar(key)

    def __iter__(self):
        for bucket in self.buckets:
            for key in bucket:
                yield key

    def __len__(self):
        return sum(len(bucket) for bucket in self.buckets)

    def __bool__(self):
        return len(self) > 0

    def mostrar(self):
        print("\n--- Medallas obtenidas ---")
        hay = False
        for bucket in self.buckets:
            for medalla in bucket:
                print(f"  - {medalla}")
                hay = True
        if not hay:
            print("  (ninguna)")


def medallas_iniciales(archivo="Medallas.json", cantidad=2):
    medallas = HashSet()
    with open(archivo, "r", encoding="utf-8") as f:
        nombres = json.load(f)
    for nombre in nombres[:cantidad]:
        medallas.agregar(nombre)
    return medallas
