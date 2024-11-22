# Ordenamiento de Árbol (Tree Sort)
# Este método usa un árbol binario de búsqueda para organizar los elementos de la lista.

class Nodo:
    # Definimos un nodo para el árbol
    def __init__(self, valor):
        self.valor = valor  # Valor del nodo
        self.izquierda = None  # Nodo hijo izquierdo
        self.derecha = None  # Nodo hijo derecho

# Función para insertar un valor en el árbol
def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)  # Si el nodo está vacío, creamos uno nuevo
    if valor < nodo.valor:
        # Si el valor es menor, lo colocamos en el subárbol izquierdo
        nodo.izquierda = insertar(nodo.izquierda, valor)
    else:
        # Si el valor es mayor o igual, lo colocamos en el subárbol derecho
        nodo.derecha = insertar(nodo.derecha, valor)
    return nodo

# Función para recorrer el árbol en orden (in-order traversal)
def recorrer_en_orden(nodo, lista):
    if nodo is not None:
        recorrer_en_orden(nodo.izquierda, lista)  # Recorrer el subárbol izquierdo
        lista.append(nodo.valor)  # Agregar el valor actual
        recorrer_en_orden(nodo.derecha, lista)  # Recorrer el subárbol derecho

# Función principal de ordenamiento
def tree_sort(lista):
    if not lista:
        return []  # Si la lista está vacía, devolvemos una lista vacía

    # Crear el árbol binario de búsqueda
    raiz = None
    for valor in lista:
        raiz = insertar(raiz, valor)

    # Recorrer el árbol para obtener la lista ordenada
    lista_ordenada = []
    recorrer_en_orden(raiz, lista_ordenada)
    return lista_ordenada

# Ejemplo de uso
mi_lista = [7, 3, 9, 1, 5]
print("Lista original:", mi_lista)

# Llamamos a la función para ordenar la lista
lista_ordenada = tree_sort(mi_lista)
print("Lista ordenada:", lista_ordenada)
