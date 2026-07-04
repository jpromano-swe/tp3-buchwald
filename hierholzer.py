from grafos import Grafo


def viaje_hierholzer(grafo, origen):
    return ciclo_euleriano_hierholzer(grafo, origen)


def obtener_grados(grafo):
    grados = {}
    cantidad_aristas = 0

    for vertice in grafo.obtener_vertices():
        grados[vertice] = len(grafo.obtener_adyacente(vertice))
        cantidad_aristas += grados[vertice]

    return grados, cantidad_aristas // 2


def ciclo_euleriano_hierholzer(grafo, origen):
    if not grafo.verificar_vertice(origen):
        return None
    if getattr(grafo, "dirigido", False):
        return None

    vertices = grafo.obtener_vertices()
    grados, cantidad_aristas = obtener_grados(grafo)
    for vertice in vertices:
        if grados[vertice] % 2 != 0:
            return None

    if cantidad_aristas == 0:
        return [origen], 0
    if grados[origen] == 0:
        return None

    if not es_conexo(grafo, origen, grados):
        return None

    grafo_aux = copiar_grafo(grafo)
    ciclo = _hierholzer(grafo_aux, origen)

    if len(ciclo) == cantidad_aristas + 1:
        return ciclo, _peso_recorrido(grafo, ciclo)
    return None


def dfs(grafo, origen):
    padres = {}
    orden = {}
    visitados = set()
    padres[origen] = None
    orden[origen] = 0
    visitados.add(origen)

    pila = [origen]
    while pila:
        v = pila.pop()
        for w in grafo.obtener_adyacente(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                orden[w] = orden[v] + 1
                pila.append(w)

    return padres, orden


def es_conexo(grafo, origen, grados):
    padres, _ = dfs(grafo, origen)
    for vertice in grafo.obtener_vertices():
        if grados[vertice] > 0 and vertice not in padres:
            return False
    return True


def copiar_grafo(grafo):
    copia = Grafo(
        dirigido=getattr(grafo, "dirigido", False),
        pesado=getattr(grafo, "pesado", False),
        vertices_iniciales=grafo.obtener_vertices()
    )
    for vertice in grafo.obtener_vertices():
        for adyacente in grafo.obtener_adyacente(vertice):
            if getattr(grafo, "dirigido", False) or not copia.verificar_arista(vertice, adyacente):
                copia.agregar_arista(vertice, adyacente, grafo.peso_arista(vertice, adyacente))
    return copia


def _hierholzer(grafo, origen):
    pila = [origen]
    ciclo = []

    while pila:
        v = pila[-1]
        adyacentes = grafo.obtener_adyacente(v)
        if adyacentes:
            w = adyacentes[0]
            grafo.borrar_arista(v, w)
            pila.append(w)
        else:
            ciclo.append(pila.pop())

    ciclo.reverse()
    return ciclo


def _peso_recorrido(grafo, recorrido):
    peso_total = 0
    for i in range(len(recorrido) - 1):
        peso_total += grafo.peso_arista(recorrido[i], recorrido[i + 1])
    return peso_total
