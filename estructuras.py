class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar_en(self, indice):
        if self.cabeza is None or indice < 0:
            return None
        if indice == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            return dato
        actual = self.cabeza
        for _ in range(indice - 1):
            if actual.siguiente is None:
                return None
            actual = actual.siguiente
        if actual.siguiente is None:
            return None
        dato = actual.siguiente.dato
        actual.siguiente = actual.siguiente.siguiente
        return dato

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def reconstruir(self, lista):
        self.cabeza = None
        for item in lista:
            self.agregar(item)

    def cantidad(self):
        n = 0
        actual = self.cabeza
        while actual:
            n += 1
            actual = actual.siguiente
        return n

    def mostrar(self):
        print("\n--- PC (Cajas) ---")
        if self.cabeza is None:
            print("  (vacía)")
            return
        actual = self.cabeza
        i = 1
        while actual:
            print(f"  {i}. {actual.dato}")
            actual = actual.siguiente
            i += 1


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def vacia(self):
        return len(self.items) == 0


class Pila:
    def __init__(self, maximo=5):
        self.items = []
        self.maximo = maximo

    def apilar(self, item):
        if len(self.items) >= self.maximo:
            self.items.pop(0)
        self.items.append(item)

    def desapilar(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def vacia(self):
        return len(self.items) == 0
