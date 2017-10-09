#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()  # Crea el parser (leer linea a linea...)
    cHandler = SmallSMILHandler()  # Crea el handler (para manejar el xml)
    parser.setContentHandler(cHandler)  # Relaciona el parser con el handler
    parser.parse(open(sys.argv[1]))
    
    lista = cHandler.get_tags()
    
    for etiqueta in lista:
        print(etiqueta['name'], '\t')
        for atributo in etiqueta:
            if etiqueta[atributo] != "" and atributo != 'name':
                print(atributo, ' = ', etiqueta[atributo])
