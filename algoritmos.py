def bubble_sort_nombre(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].nombre.lower() > lista[j + 1].nombre.lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def insertion_sort_tipo(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j].tipo.lower() > clave.tipo.lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def quick_sort_poder(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2].poder_combate
    menores = [p for p in lista if p.poder_combate > pivote]
    iguales = [p for p in lista if p.poder_combate == pivote]
    mayores = [p for p in lista if p.poder_combate < pivote]
    return quick_sort_poder(menores) + iguales + quick_sort_poder(mayores)


def busqueda_lineal(equipo, nombre):
    nombre = nombre.lower()
    for i, poke in enumerate(equipo):
        if poke.nombre.lower() == nombre:
            return i
    return -1


def busqueda_binaria(ids_ordenados, objetivo):
    izq, der = 0, len(ids_ordenados) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if ids_ordenados[medio] == objetivo:
            return medio
        if ids_ordenados[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
