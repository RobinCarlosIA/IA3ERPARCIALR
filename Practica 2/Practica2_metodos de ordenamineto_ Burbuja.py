# Ordenamiento Bubble Sort (Ordenamiento por Burbuja)
# Este método compara elementos adyacentes y los intercambia si están en el orden incorrecto.

def bubble_sort(lista):
    """
    Ordena una lista usando el método de Bubble Sort.
    """
    n = len(lista)  # Número de elementos en la lista

    # Recorremos la lista varias veces
    for i in range(n):
        # En cada iteración, comparamos elementos adyacentes
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        # Mostramos cómo se ve la lista después de cada pasada
        print(f"Pasada {i + 1}: {lista}")

    # Devolvemos la lista ordenada
    return lista

# Ejemplo de uso
mi_lista = [5, 3, 8, 6, 2]
print("Lista original:", mi_lista)

# Llamamos a la función para ordenar la lista
print("\nIniciando el ordenamiento Bubble Sort...\n")
lista_ordenada = bubble_sort(mi_lista)
print("\nLista ordenada:", lista_ordenada)
