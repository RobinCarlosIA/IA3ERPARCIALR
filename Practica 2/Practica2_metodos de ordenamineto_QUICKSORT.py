# Ordenamiento QuickSort
# Este método divide la lista en partes más pequeñas usando un pivote y ordena cada parte.

def quicksort(lista):
    # Caso base: si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Elegimos un elemento como pivote (usamos el primer elemento aquí)
    pivote = lista[0]

    # Partimos la lista en tres partes:
    # - Menores: elementos menores que el pivote
    # - Iguales: elementos iguales al pivote
    # - Mayores: elementos mayores que el pivote
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    # Ordenamos las partes menores y mayores recursivamente y las unimos
    return quicksort(menores) + iguales + quicksort(mayores)

# Ejemplo de uso
mi_lista = [8, 3, 1, 7, 0, 10, 2]
print("Lista original:", mi_lista)

# Llamamos a la función para ordenar la lista
lista_ordenada = quicksort(mi_lista)
print("Lista ordenada:", lista_ordenada)
