
def crearKML(nombreArchivo, orden): #refactorizar en menos lineas
    with open("{nombreArchivo}.kml", "w", encoding="utf-8") as archivo:
        archivo.write('<?xml version="1.0" encoding="UTF-8"?>')
        archivo.write('<kml xmlns="http://earth.google.com/kml/2.1">')
        archivo.write('<Document>')
        archivo.write('<name>{nombreArchivo}</name>')
        for v in orden:
            archivo.write('<Placemark>')
            archivo.write('<name>{v[0]}</name>')
            archivo.write('<Point>')
            archivo.write('<coordinates>{v[1]},{v[2]}</coordinates>')
            archivo.write('</Point>')
            archivo.write('</Placemark>')
        for i in range(len(orden)-1):
            actual = orden[i]
            sig = orden[i+1]
            archivo.write('<Placemark>')
            archivo.write('<LineString>')
            archivo.write('<coordinates>{actual[1]},{actual[2]} {sig[1]},{sig[2]}</coordinates>')
            archivo.write('</LineString>')
            archivo.write('</Placemark>')   
        archivo.write('</Document>')
        archivo.write('</kml>')




def exportarKML(orden,nombreArchivo):
    kml = crearKML(nombreArchivo,orden)