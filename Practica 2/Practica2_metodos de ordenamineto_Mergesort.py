# Ordenamiento MergeSort
# Este método divide la lista en mitades, las ordena por separado y luego las une.

def merge_sort(lista):
    # Caso base: si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Ordenamos cada mitad recursivamente
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # Mezclamos las dos mitades ordenadas
    return mezclar(izquierda_ordenada, derecha_ordenada)

def mezclar(izquierda, derecha):
    # Creamos una lista vacía para guardar los elementos ordenados
    resultado = []

    # Usamos dos índices para recorrer ambas mitades
    i = 0  # Índice para la lista izquierda
    j = 0  # Índice para la lista derecha

    # Comparamos los elementos de ambas listas y los agregamos al resultado
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregamos los elementos restantes de la izquierda (si quedan)
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    # Agregamos los elementos restantes de la derecha (si quedan)
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

# Ejemplo de uso
mi_lista = [6, 3, 8, 5, 2, 7, 4, 1]
print("Lista original:", mi_lista)

# Llamamos a la función para ordenar la lista
lista_ordenada = merge_sort(mi_lista)
print("Lista ordenada:", lista_ordenada)
