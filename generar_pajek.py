
def obtener_aristas(grafo):
    aristas = []
    visitados = set()    
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacente(v):
            if w not in visitados:
                aristas.append((grafo.peso_arista(v,w),v,w))
        visitados.add(v)
    return aristas

def crearPajek(recorrido, nombreArchivo):
    with open("{nombreArchivo}.pj", "w", encoding="utf-8") as archivo:
        tamanio = len(recorrido.obtener_vertices())
        archivo.write('{tamanio}')
        for v,lat,lon in recorrido.obtener_vertices():
            archivo.write('{v},{lat},{lon}')
        aristas = obtener_aristas(recorrido)
        tamanio = len(aristas)
        archivo.write('{tamanio}')
        for v,w,d in aristas:
            archivo.write('{v},{w},{d}')
