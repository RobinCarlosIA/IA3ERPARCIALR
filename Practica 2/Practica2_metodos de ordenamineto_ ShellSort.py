# Ordenamiento ShellSort
# Este método es una versión mejorada de Insertion Sort, que organiza elementos usando intervalos más grandes y luego los reduce.

def shell_sort(lista):
    """
    Ordena una lista usando el método ShellSort.
    """
    n = len(lista)
    intervalo = n // 2  # Comenzamos con un intervalo grande (la mitad del tamaño de la lista)

    # Mientras el intervalo sea mayor que 0
    while intervalo > 0:
        # Recorremos los elementos desde el intervalo hasta el final
        for i in range(intervalo, n):
            # Guardamos el valor actual
            valor_actual = lista[i]
            j = i

            # Comparamos y movemos elementos en el intervalo
            while j >= intervalo and lista[j - intervalo] > valor_actual:
                lista[j] = lista[j - intervalo]
                j -= intervalo

            # Insertamos el valor actual en su posición correcta
            lista[j] = valor_actual

        # Mostramos la lista después de cada intervalo
        print(f"Intervalo {intervalo}: {lista}")

        # Reducimos el intervalo a la mitad
        intervalo //= 2

    # Devolvemos la lista ordenada
    return lista

# Ejemplo de uso
mi_lista = [12, 34, 54, 2, 3]
print("Lista original:", mi_lista)

# Llamamos a la función para ordenar la lista
print("\nIniciando el ordenamiento ShellSort...\n")
lista_ordenada = shell_sort(mi_lista)
print("\nLista ordenada:", lista_ordenada)
