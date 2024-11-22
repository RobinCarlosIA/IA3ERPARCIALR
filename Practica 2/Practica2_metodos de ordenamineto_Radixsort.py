# Ordenamiento RadixSort
# Este método organiza los números por cada dígito, de menor a mayor lugar decimal (unidades, decenas, centenas, etc.).

def radix_sort(lista):
    # Encontramos el número más grande para saber cuántos dígitos tiene
    maximo = max(lista)
    # Inicializamos la posición de dígito (1 para unidades, 10 para decenas, 100 para centenas, etc.)
    posicion = 1

    # Mientras aún queden dígitos por procesar (máximo tiene más dígitos que la posición actual)
    while maximo // posicion > 0:
        # Ordenamos la lista usando el dígito de la posición actual
        lista = contar_y_ordenar(lista, posicion)
        # Pasamos a la siguiente posición (unidades -> decenas -> centenas, etc.)
        posicion *= 10

    return lista

def contar_y_ordenar(lista, posicion):
    # Creamos un "bucket" para cada dígito (0 a 9)
    conteo = [0] * 10
    salida = [0] * len(lista)

    # Contamos cuántos números hay para cada dígito en la posición actual
    for numero in lista:
        digito = (numero // posicion) % 10
        conteo[digito] += 1

    # Ajustamos los conteos para que representen las posiciones finales en el arreglo ordenado
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Colocamos los números en el arreglo de salida en orden, usando el conteo
    for numero in reversed(lista):
        digito = (numero // posicion) % 10
        salida[conteo[digito] - 1] = numero
        conteo[digito] -= 1

    return salida

# Ejemplo de uso
mi_lista = [170, 45, 75, 90, 802, 24, 2, 66]
print("Lista original:", mi_lista)

# Llamamos a la función para ordenar la lista
lista_ordenada = radix_sort(mi_lista)
print("Lista ordenada:", lista_ordenada)
