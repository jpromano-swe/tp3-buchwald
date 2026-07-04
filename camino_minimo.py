from tdas.heap import Heap

def cmp_min(arista1, arista2):
  return arista2[0] - arista1[0]


def camino_minimo(grafo, origen, destino, coordenadas):
  resultado = camino_minimo_dijkstra(grafo, origen, destino, coordenadas)
  if resultado is None:
    return None

  padre, dist = resultado
  if dist[destino] == float("inf"):
    return None

  camino = []
  actual = destino
  while actual is not None:
    camino.append(actual)
    actual = padre[actual]
  camino.reverse()

  return camino, dist[destino]


def camino_minimo_dijkstra(grafo, origen, destino,coordenadas):
  if not grafo.verificar_vertice(origen) or not grafo.verificar_vertice(destino):
    return None
  dist = {}
  padre = {}
  for v in grafo.obtener_vertices():
    dist[v] = float("inf")
  dist[origen] = 0
  padre[origen] = None

  q = Heap(cmp_min)
  q.encolar((0, origen))

  while not q.esta_vacia():
    _, v = q.desencolar()
    if v == destino:
      return padre, dist

    for w in grafo.obtener_adyacente(v):
      distancia_por_aca = dist[v] + grafo.peso_arista(v, w)
      if distancia_por_aca < dist[w]:
        dist[w] = distancia_por_aca
        padre[w] = v
        q.encolar((dist[w], w))
    

  return padre, dist
