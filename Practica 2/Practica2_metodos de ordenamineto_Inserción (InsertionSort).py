# Ordenamiento por Inserción (Insertion Sort)
# Este método organiza una lista paso a paso, colocando cada elemento en su posición correcta.

def insertion_sort(lista):
    # Recorremos la lista desde el segundo elemento (porque asumimos que el primero ya está "ordenado").
    for i in range(1, len(lista)):
        # Guardamos el valor actual que queremos insertar en su lugar correcto.
        valor_actual = lista[i]
        # Creamos una variable para comparar con los elementos anteriores.
        j = i - 1

        # Mientras haya elementos en la lista y el valor anterior sea mayor que el actual...
        while j >= 0 and lista[j] > valor_actual:
            # Movemos el elemento hacia la derecha (hacemos espacio para el valor_actual).
            lista[j + 1] = lista[j]
            j -= 1  # Retrocedemos para comparar con el siguiente elemento.

        # Insertamos el valor_actual en el lugar que le corresponde.
        lista[j + 1] = valor_actual

    # Retornamos la lista ya ordenada.
    return lista

# Ejemplo de uso:
mi_lista = [5, 3, 8, 6, 2]
print("Lista original:", mi_lista)

# Llamamos a la función para ordenar la lista.
lista_ordenada = insertion_sort(mi_lista)
print("Lista ordenada:", lista_ordenada)
