def formatear_numero(numero):
    if numero == int(numero):
        return str(int(numero))
    return str(numero)


def obtener_aristas(grafo):
    aristas = []
    visitados = set()

    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacente(v):
            if w not in visitados:
                aristas.append((v, w, grafo.peso_arista(v, w)))
        visitados.add(v)

    return aristas


def crearPajek(recorrido, nombreArchivo, coordenadas):
    vertices = recorrido.obtener_vertices()
    aristas = obtener_aristas(recorrido)

    with open(nombreArchivo, "w", encoding="utf-8") as archivo:
        archivo.write(f"{len(vertices)}\n")

        for v in vertices:
            latitud, longitud = coordenadas[v]
            archivo.write(f"{v},{latitud},{longitud}\n")

        archivo.write(f"{len(aristas)}\n")

        for v, w, peso in aristas:
            archivo.write(f"{v},{w},{formatear_numero(peso)}\n")
