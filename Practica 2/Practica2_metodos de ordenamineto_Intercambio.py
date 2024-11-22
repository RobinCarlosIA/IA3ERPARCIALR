# Ordenamiento por Intercambio
# Este método compara todos los elementos de la lista y los intercambia si están desordenados.

def intercambio_sort(lista):
    # Recorremos la lista
    for i in range(len(lista)):
        # Comparar el elemento actual con todos los siguientes
        for j in range(i + 1, len(lista)):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[i] > lista[j]:
                # Intercambiamos los valores
                lista[i], lista[j] = lista[j], lista[i]

    # Devolvemos la lista ya ordenada
    return lista

# Ejemplo de uso
mi_lista = [4, 2, 7, 1, 3]
print("Lista original:", mi_lista)

# Llamamos a la función para ordenar la lista
lista_ordenada = intercambio_sort(mi_lista)
print("Lista ordenada:", lista_ordenada)
