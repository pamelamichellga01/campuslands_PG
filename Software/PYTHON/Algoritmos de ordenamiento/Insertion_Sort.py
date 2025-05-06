# Algoritmo de ordenamiento por inserción
lista = [5, 2, 9, 1, 5, 6]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

print("Lista ordenada:", insertion_sort(lista))
