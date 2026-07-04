from camino_minimo import camino_minimo
from generar_kml import exportarKML
from generar_pajek import crearPajek
from hierholzer import viaje_hierholzer
from mst import mst_prim
from recorrer_orden_top import viajes

from funciones_aux import (
    cargar_recomendaciones,
    formatear_recorrido,
    separar_parametros,
)


COMANDO_IR = "ir"
COMANDO_ITINERARIO = "itinerario"
COMANDO_VIAJE = "viaje"
COMANDO_REDUCIR_CAMINOS = "reducir_caminos"

ERROR_RECORRIDO = "No se encontro recorrido"


class Comandos:
    def __init__(self, grafo, coordenadas=None):
        self.grafo = grafo
        self.coordenadas = coordenadas if coordenadas is not None else {}

    def ejecutar_comando(self, ingreso):
        partes = ingreso.strip().split(" ", 1)
        comando = partes[0]

        if len(partes) > 1:
            parametros = partes[1]
        else:
            parametros = ""

        if comando == COMANDO_IR:
            return self.ejecutar_ir(parametros)
        if comando == COMANDO_ITINERARIO:
            return self.ejecutar_itinerario(parametros)
        if comando == COMANDO_VIAJE:
            return self.ejecutar_viaje(parametros)
        if comando == COMANDO_REDUCIR_CAMINOS:
            return self.ejecutar_reducir_caminos(parametros)
        return ERROR_RECORRIDO

    def ejecutar_ir(self, parametros):
        partes = separar_parametros(parametros, 3)
        if partes is None:
            return ERROR_RECORRIDO

        origen, destino, archivo = partes
        resultado = camino_minimo(self.grafo, origen, destino)
        if resultado is None:
            return ERROR_RECORRIDO

        recorrido, peso_total = resultado
        exportarKML(archivo, recorrido, self.coordenadas, f"Camino desde {origen} hacia {destino}")
        return formatear_recorrido(recorrido, peso_total)

    def ejecutar_viaje(self, parametros):
        partes = separar_parametros(parametros, 2)
        if partes is None:
            return ERROR_RECORRIDO

        origen, archivo = partes
        resultado = viaje_hierholzer(self.grafo, origen)
        if resultado is None:
            return ERROR_RECORRIDO

        recorrido, peso_total = resultado
        exportarKML(archivo, recorrido, self.coordenadas, f"Viaje desde {origen}")
        return formatear_recorrido(recorrido, peso_total)

    def ejecutar_itinerario(self, parametros):
        archivo = parametros.strip()
        if not archivo:
            return ERROR_RECORRIDO

        grafo_recomendaciones = cargar_recomendaciones(self.grafo, archivo)
        if grafo_recomendaciones is None:
            return ERROR_RECORRIDO

        recorrido = viajes(grafo_recomendaciones)
        if recorrido is None:
            return ERROR_RECORRIDO
        return " -> ".join(recorrido)

    def ejecutar_reducir_caminos(self, parametros):
        archivo = parametros.strip()
        if archivo == "":
            return ERROR_RECORRIDO

        resultado = mst_prim(self.grafo)
        if resultado is None:
            return ERROR_RECORRIDO

        arbol, peso_total = resultado
        crearPajek(arbol, archivo, self.coordenadas)
        return f"Peso total: {formatear_numero(peso_total)}"


def formatear_numero(numero):
    if numero == int(numero):
        return str(int(numero))
    return str(numero)
