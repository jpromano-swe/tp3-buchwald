#!/usr/bin/python3
import sys

from comandos import Comandos
from funciones_aux import cargar_pajek


def main():
    if len(sys.argv) != 2:
        return

    resultado = cargar_pajek(sys.argv[1])
    if resultado is None:
        return

    grafo, coordenadas = resultado
    comandos = Comandos(grafo, coordenadas)

    for linea in sys.stdin:
        linea = linea.strip()
        if linea == "":
            continue
        print(comandos.ejecutar_comando(linea))


if __name__ == "__main__":
    main()
