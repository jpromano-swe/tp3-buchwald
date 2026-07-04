from grafos import Grafo


def cargar_pajek(archivo):
  grafo = Grafo(pesado=True)
  coordenadas = {}
  try:
    with open(archivo, encoding="utf-8") as pajek:
      cantidad_vertices = int(pajek.readline().strip())
      if not cargar_vertices_pajek(pajek, grafo, coordenadas, cantidad_vertices):
        return None

      cantidad_aristas = int(pajek.readline().strip())
      if not cargar_aristas_pajek(pajek, grafo, cantidad_aristas):
        return None

  except (OSError, ValueError, TypeError):
    return None

  return grafo, coordenadas

def cargar_vertices_pajek(pajek, grafo, coordenadas, cantidad_vertices):
  for _ in range(cantidad_vertices):
    partes = separar_parametros(pajek.readline(), 3)
    if partes is None:
      return False

    nombre, latitud, longitud = partes
    grafo.agregar_vertice(nombre)
    coordenadas[nombre] = (latitud, longitud)

  return True


def cargar_aristas_pajek(pajek, grafo, cantidad_aristas):
  for _ in range(cantidad_aristas):
    partes = separar_parametros(pajek.readline(), 3)
    if partes is None:
      return False

    origen, destino, peso = partes
    grafo.agregar_arista(origen, destino, float(peso))

  return True


def separar_parametros(parametros, cantidad):
  partes = [parte.strip() for parte in parametros.split(",")]

  if len(partes) != cantidad:
    return None
  else:
    for parte in partes:
      if parte == "":
        return None
    return partes

def formatear_recorrido(recorrido, peso_total):
    return f"{' -> '.join(recorrido)}\nTiempo total: {peso_total}"


def cargar_recomendaciones(grafo_mapa, archivo):
    grafo = Grafo(dirigido=True, vertices_iniciales=grafo_mapa.obtener_vertices())

    try:
        with open(archivo, encoding="utf-8") as recomendaciones:
            for linea in recomendaciones:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = separar_parametros(linea, 2)
                if partes is None:
                    return None
                origen, destino = partes
                if not grafo.verificar_vertice(origen) or not grafo.verificar_vertice(destino):
                    return None
                grafo.agregar_arista(origen, destino)
    except OSError:
        return None

    return grafo
