from grafos import Grafo
from tdas import cola
from cola import ColaEnlazada
import generar_kml
#Adam
def grados_entrada(grafo):
    orden_entrada = {}
    for v in grafo.obtener_vertices():
        orden_entrada[v] = 0
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacente(v):
            orden_entrada[w] += 1
    return orden_entrada

def viajes(grafo):
    entradas = grados_entrada(grafo)
    cola = ColaEnlazada()
    orden_recorrido = []
    for v in grafo.obtener_vertices():
        if entradas[v] == 0:
            cola.encolar(v)
    while not cola.esta_vacia():
        v = cola.desencolar()
        orden_recorrido.append(v)
        for w in grafo.obtener_adyacente(v):
            entradas[w] -= 1
            if entradas[w] == 0:
                cola.encolar(w)
    return orden_recorrido
    

