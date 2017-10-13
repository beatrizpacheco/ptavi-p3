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

    def __str__(self):
        str_lista = ""
        for etiqueta in self.lista:
            str_lista += etiqueta['name']
            for atrib in etiqueta:
                if etiqueta[atrib] != "" and atrib != 'name':
                    str_lista += '\t' + atrib + '="' + etiqueta[atrib] + '"'
            str_lista += '\n'
        return(str_lista)

    def to_json(self, fich_smil, fich_json=None):
        if fich_json is None:
            fich_json = fich_smil.split('.')[0] + '.json'
        json.dump([self.lista], open(fich_json, "w"))

    def do_local(self):
        for etiqueta in self.lista:
            for atrib in etiqueta:
                if etiqueta[atrib][0:7] == "http://":
                    old_atrib = etiqueta[atrib]
                    new_atrib = etiqueta[atrib].split("/")[-1]
                    urlretrieve(old_atrib, new_atrib)

                    old_file = open(sys.argv[1], "r")
                    old_buff = old_file.read()
                    new_buff = old_buff.replace(old_atrib, new_atrib)
                    new_file = open(sys.argv[1], "w")
                    new_file.write(new_buff)
                    old_file.close()
                    new_file.close()

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")
    objeto = KaraokeLocal(sys.argv[1])
    print(objeto.__str__())
    objeto.to_json(sys.argv[1])
    objeto.do_local()
    objeto.to_json(sys.argv[1], 'local.json')

    objeto = KaraokeLocal(sys.argv[1])
    print(objeto.__str__())

    # tengo que cerrar el open de la linea 34??
