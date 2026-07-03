import random

ERROR_VERTICE_INEXISTENTE = "El vertice no pertenece al grafo"
ERROR_ARISTA_INEXISTENTE = "La arista no pertenece al grafo"
ERROR_VERTICES_INEXISTENTES = "Algun vertice no pertenece al grafo"
ERROR_GRAFO_VACIO = "El grafo está vacio"

class Grafo:
    def __init__(self, dirigido=False, pesado=False, vertices_iniciales=[]):
        self.arista = dict()
        self.vertices = []
        for vertice in vertices_iniciales:
            self.arista[vertice] = {}
            self.vertices.append(vertice)
        self.dirigido = dirigido
        self.pesado = pesado

    def vertice_aleatorio(self):
        if len(self.vertices) == 0:
            raise ValueError(ERROR_GRAFO_VACIO)
        return random.choice(self.vertices)

    def obtener_vertices(self):
        return self.vertices
    
    def agregar_vertice(self, vertice):
        if vertice not in self.arista:
            self.arista[vertice] = {}
            self.vertices.append(vertice)

    def agregar_arista(self, v, w, peso=1):
        if not self.verificar_vertice(v) or not self.verificar_vertice(w):
            raise ValueError(ERROR_VERTICES_INEXISTENTES)
        self.arista[v][w] = peso
        if not self.dirigido:
            self.arista[w][v] = peso

    def peso_arista(self, v, w):
        if not self.verificar_arista(v, w):
            raise ValueError(ERROR_ARISTA_INEXISTENTE)
        return self.arista[v][w]

    def borrar_vertice(self, v):
        if v in self.arista:
            for w in self.arista.values():
                if v in w:
                    w.pop(v)
            self.arista.pop(v)        
            self.vertices.remove(v)

    def borrar_arista(self, v, w):
        if v in self.arista and w in self.arista[v]:
            self.arista[v].pop(w)
        if not self.dirigido and w in self.arista and v in self.arista[w]:
            self.arista[w].pop(v)

    def estan_unidos(self, v, w):
        if not self.verificar_vertice(v) or not self.verificar_vertice(w):
            raise ValueError(ERROR_VERTICES_INEXISTENTES)
        return self.verificar_arista(v, w)
    
    def obtener_adyacente(self, v):
        if v not in self.arista:
            return []
        return list(self.arista[v].keys())

    def verificar_vertice(self, v):
        return v in self.arista
    
    def verificar_arista(self, v, w):
        if v in self.arista:
            return w in self.arista[v]
        return False
    
   