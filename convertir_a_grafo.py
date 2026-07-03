from grafos import Grafo

def convertir(archivo):
    grafo = Grafo(pesado=True)
    ciudades = {}
    with open(archivo,"r", encoding="utf-8") as arc:
        for ciudad in arc:
            ciudad = ciudad.strip()
            partes = ciudad.split(',')
            if len(partes) == 1:
                continue
            if len(partes) == 3:
                try:
                    prueba = float(partes[1])
                    grafo.agregar_vertice((partes))
                    ciudades[partes[0]] = partes
                except ValueError:
                    grafo.agregar_arista(ciudades[partes[0]],ciudades[partes[1]],float(partes[2]))
        
