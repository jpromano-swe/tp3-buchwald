
def crearKML(nombreArchivo, orden,coordenadas,texto):
    with open(f"{nombreArchivo}", "w", encoding="utf-8") as archivo:
        archivo.write('<?xml version="1.0" encoding="UTF-8"?>')
        archivo.write('<kml xmlns="http://earth.google.com/kml/2.1">')
        archivo.write('<Document>')
        archivo.write(f'<name>{nombreArchivo}</name>')
        for v in orden:
            archivo.write('<Placemark>')
            archivo.write(f'<name>{v}</name>')
            archivo.write('<Point>')
            archivo.write(f'<coordinates>{coordenadas[v][1]}, {coordenadas[v][0]}</coordinates>')
            archivo.write('</Point>')
            archivo.write('</Placemark>')
        for i in range(len(orden)-1):
            actual = orden[i]
            sig = orden[i+1]
            archivo.write('<Placemark>')
            archivo.write('<LineString>')
            archivo.write(f'<coordinates>{coordenadas[actual][1]}, {coordenadas[actual][0]} {coordenadas[sig][1]},{coordenadas[sig][0]}</coordinates>')
            archivo.write('</LineString>')
            archivo.write('</Placemark>')   
        archivo.write('</Document>')
        archivo.write('</kml>')
def exportarKML(nombreArchivo, orden, coordenadas, texto):
    crearKML(nombreArchivo,orden,coordenadas,texto)