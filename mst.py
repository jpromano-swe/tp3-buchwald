from tdas import heap
import generar_pajek

def heap_min(v1,v2):     
    return v1[2]-v2[2]


def mst_prim(grafo,destino):
    visitados = set()
    heap = Heap(mst_prim)
    v = grafo.vertice_aleatorio()
    visitados.add(v)
    camino = 0
    for w in grafo.obtener_adyacente(v):
        heap.encolar((v,w,grafo.peso_arista(v,w)))
    recorrido = Grafo(pesado=True,dirigido=False,vertices_iniciales=grafo.obtener_vertices())
    while not heap.esta_vacia():
        v,w,peso = heap.desencolar(func_min_prim)
        if w not in visitados:
            visitados.add(w)
            recorrido.agregar_arista(v,w,peso)
            camino += peso
            for u in grafo.obtener_adyacente(w):
                if u not in visitados:
                    heap.encolar((w,u,grafo.peso_arista(w,u)))
    generar_pajek.crearPajek(recorrido,destino)
    print("Peso total: {camino}")
    return recorrido,camino

