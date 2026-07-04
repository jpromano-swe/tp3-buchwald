def _coordenadas_vertice(coordenadas, vertice):
    latitud, longitud = coordenadas[vertice]
    return f"{latitud}, {longitud}"


def crearKML(nombreArchivo, orden, coordenadas, texto):
    with open(nombreArchivo, "w", encoding="utf-8") as archivo:
        archivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        archivo.write('<kml xmlns="http://earth.google.com/kml/2.1">\n')
        archivo.write("\t<Document>\n")
        archivo.write(f"\t\t<name>{texto}</name>\n\n")

        for v in orden:
            archivo.write("\t\t<Placemark>\n")
            archivo.write(f"\t\t\t<name>{v}</name>\n")
            archivo.write("\t\t\t<Point>\n")
            archivo.write(f"\t\t\t\t<coordinates>{_coordenadas_vertice(coordenadas, v)}</coordinates>\n")
            archivo.write("\t\t\t</Point>\n")
            archivo.write("\t\t</Placemark>\n")

        archivo.write("\n")
        for i in range(len(orden) - 1):
            actual = orden[i]
            siguiente = orden[i + 1]
            archivo.write("\t\t<Placemark>\n")
            archivo.write("\t\t\t<LineString>\n")
            archivo.write(
                f"\t\t\t\t<coordinates>{_coordenadas_vertice(coordenadas, actual)} "
                f"{_coordenadas_vertice(coordenadas, siguiente)}</coordinates>\n"
            )
            archivo.write("\t\t\t</LineString>\n")
            archivo.write("\t\t</Placemark>\n")

        archivo.write("\t</Document>\n")
        archivo.write("</kml>\n")


def exportarKML(nombreArchivo, orden, coordenadas, texto):
    crearKML(nombreArchivo, orden, coordenadas, texto)
