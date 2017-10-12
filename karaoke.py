#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")

#Inicializa
    parser = make_parser()  # Crea el parser (leer linea a linea...)
    cHandler = SmallSMILHandler()  # Crea el handler (para manejar el xml)
    parser.setContentHandler(cHandler)  # Relaciona el parser con el handler
    parser.parse(open(sys.argv[1]))
    lista = cHandler.get_tags()

#Escribe
    for etiqueta in lista:
        nombre = etiqueta['name']
        for atributo in etiqueta:
            if etiqueta[atributo] != "" and atributo != 'name':
                nombre += '\t' + atributo + '="' + etiqueta[atributo] + '"'
        print(nombre)
        nombre = ""

#Crear el archivo json
    json.dump([lista], open("karaoke.json", "w"))
