_CAPACIDAD_INICIAL = 2
_FACTOR_DE_CRECIMIENTO = 2
_FACTOR_DE_REDUCCION = 4
_ERROR_HEAP_VACIO = "La cola está vacía"

class Heap:
    def __init__(self, funcion_cmp, arreglo_inicial=None):
        self.cmp = funcion_cmp
        
        if arreglo_inicial is None:
            self.datos = [None] * _CAPACIDAD_INICIAL
            self.cantidad = 0
        else:
            # Si te pasaron un arreglo, lo clonás y heapificás en O(n)
            capacidad = max(len(arreglo_inicial), _CAPACIDAD_INICIAL)
            self.datos = [None] * capacidad
            for i in range(len(arreglo_inicial)):
                self.datos[i] = arreglo_inicial[i]
            self.cantidad = len(arreglo_inicial)
            self._heapify()

    def esta_vacia(self):
        return self.cantidad == 0

    def encolar(self, elemento):
        if self.cantidad == len(self.datos):
            self._redimensionar(len(self.datos) * _FACTOR_DE_CRECIMIENTO)
        self.datos[self.cantidad] = elemento
        self.cantidad += 1
        self._upheap(self.cantidad - 1)

    def ver_max(self):
        if self.esta_vacia():
            raise ValueError(_ERROR_HEAP_VACIO)
        return self.datos[0]

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError(_ERROR_HEAP_VACIO)
        return self._desencolar(0, self.cantidad - 1)

    def _desencolar(self, ini, fin):
        maximo = self.datos[ini]
        if self.cantidad == 1:
            self.datos[ini] = None
            self.cantidad -= 1
            return maximo
        self.datos[ini] = self.datos[fin]
        self.datos[fin] = None
        self.cantidad -= 1
        self._downheap(ini)
        if (
            self.cantidad > 0
            and self.cantidad * _FACTOR_DE_REDUCCION <= len(self.datos)
            and len(self.datos) > _CAPACIDAD_INICIAL
        ):
            nueva_capacidad = len(self.datos) // _FACTOR_DE_CRECIMIENTO
            if nueva_capacidad < _CAPACIDAD_INICIAL:
                nueva_capacidad = _CAPACIDAD_INICIAL
            self._redimensionar(nueva_capacidad)
        return maximo

    def _upheap(self, pos):
        if pos != 0:
            padre = (pos - 1) // 2
            if self.cmp(self.datos[pos], self.datos[padre]) > 0:
                self.datos[pos], self.datos[padre] = self.datos[padre], self.datos[pos]
                self._upheap(padre)

    def _downheap(self, pos):
        hijo_izq = 2 * pos + 1
        hijo_der = 2 * pos + 2
        mayor = pos
        if hijo_izq < self.cantidad and self.cmp(self.datos[hijo_izq], self.datos[mayor]) > 0:
            mayor = hijo_izq
        if hijo_der < self.cantidad and self.cmp(self.datos[hijo_der], self.datos[mayor]) > 0:
            mayor = hijo_der
        if mayor != pos:
            self.datos[pos], self.datos[mayor] = self.datos[mayor], self.datos[pos]
            self._downheap(mayor)

    def cantidad_elementos(self):
        return self.cantidad

    def _redimensionar(self, nueva_capacidad):
        nuevos_datos = [None] * nueva_capacidad
        for i in range(self.cantidad):
            nuevos_datos[i] = self.datos[i]
        self.datos = nuevos_datos

    def _heapify(self):
        ultimo_padre = self.cantidad // 2 - 1
        for i in range(ultimo_padre, -1, -1):
            self._downheap(i)

def crear_heap_arr(arreglo, funcion_cmp):
    heap = Heap(funcion_cmp)
    capacidad = max(len(arreglo), _CAPACIDAD_INICIAL)
    heap.datos = [None] * capacidad
    for i in range(len(arreglo)):
        heap.datos[i] = arreglo[i]
    heap.cantidad = len(arreglo)
    heap._heapify()
    return heap

def heatsort(elementos, funcion_cmp):
    heap = crear_heap_arr(elementos, funcion_cmp)
    ordenados = []
    while not heap.esta_vacia():
        ordenados.append(heap.desencolar())
    for i in range(len(elementos)):
        elementos[i] = ordenados[i]


