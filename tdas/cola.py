_ERROR_COLA_VACIA = "La cola esta vacia"


class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None


class ColaEnlazada:

  def __init__(self):
    self.primero = None
    self.ultimo = None

  def esta_vacia(self):
    return self.primero is None

  def ver_primero(self):
    if self.esta_vacia():
      raise ValueError(_ERROR_COLA_VACIA)

    return self.primero.dato

  def encolar(self, elem):
    nuevo_nodo = Nodo(elem)

    if self.esta_vacia():
      self.primero = nuevo_nodo
    else:
      self.ultimo.siguiente = nuevo_nodo

    self.ultimo = nuevo_nodo

  def desencolar(self):
    if self.esta_vacia():
      raise ValueError(_ERROR_COLA_VACIA)

    dato = self.primero.dato
    self.primero = self.primero.siguiente

    if self.primero is None:
      self.ultimo = None

    return dato


def crear_cola():
  return ColaEnlazada()
