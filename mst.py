from grafos import Grafo
from tdas.heap import Heap


def heap_min(arista1, arista2):
    return arista2[2] - arista1[2]


def mst_prim(grafo):
    vertices = grafo.obtener_vertices()
    if len(vertices) == 0:
        return None

    visitados = set()
    heap = Heap(heap_min)
    origen = vertices[0]
    visitados.add(origen)

    arbol = Grafo(pesado=True, dirigido=False, vertices_iniciales=vertices)
    peso_total = 0

    for adyacente in grafo.obtener_adyacente(origen):
        heap.encolar((origen, adyacente, grafo.peso_arista(origen, adyacente)))

    while not heap.esta_vacia():
        v, w, peso = heap.desencolar()
        if w in visitados:
            continue

        visitados.add(w)
        arbol.agregar_arista(v, w, peso)
        peso_total += peso

        for adyacente in grafo.obtener_adyacente(w):
            if adyacente not in visitados:
                heap.encolar((w, adyacente, grafo.peso_arista(w, adyacente)))

    if len(visitados) != len(vertices):
        return None

    return arbol, peso_total
