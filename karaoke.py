#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.lista = cHandler.get_tags()

    def __str__ (self):
        str_lista = ""
        for etiqueta in self.lista:
            str_lista += etiqueta['name']
            for atributo in etiqueta:
                if etiqueta[atributo] != "" and atributo != 'name':
                    str_lista += '\t' + atributo + '="' + etiqueta[atributo] + '"'
            str_lista += '\n'
        return(str_lista)

    def to_json(self, fich_smil, fich_json = None):
        if fich_json == None:
            fich_json = fich_smil.split('.')[0] + '.json'
        json.dump([self.lista], open(fich_json, "w"))


    def do_local(self):
        for etiqueta in self.lista:
            for atributo in etiqueta:
                if etiqueta[atributo][0:7] == "http://":
                    urlretrieve(etiqueta[atributo], etiqueta[atributo].split("/")[-1])

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")
    objeto = KaraokeLocal(sys.argv[1])
    print(objeto.__str__())
    objeto.to_json(sys.argv[1])
    objeto.do_local()
    objeto.to_json(sys.argv[1], 'local.json')
    print(objeto.__str__())
