#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fich):
        """
        Inicializa el objeto creando el parser, el handler y la lista
        """
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fich))
        self.list = sHandler.get_tags()

    def __str__(self):
        """
        Recorre la lista de diccionarios y añade a un string
        las etiquetas con sus atributos y sus valores
        """
        str_list = ""
        for dic_label in self.list:
            str_list += dic_label['name']
            for atrib in dic_label:
                if dic_label[atrib] != "" and atrib != 'name':
                    str_list += '\t' + atrib + '="' + dic_label[atrib] + '"'
            str_list += '\n'
        return(str_list)

    def to_json(self, fich_smil, fich_json=None):
        """
        A partir de la lista donde guardo etiquetas con atributos
        y valores me crea un fichero con formato json
        """
        if fich_json is None:
            fich_json = fich_smil.split('.')[0] + '.json'
        json.dump(self.list, open(fich_json, "w"))

    def do_local(self):
        """
        Recorre la lista de diccionarios y descarga aquello que
        esté en remoto, cambiando el valor del atirbuto al
        lugar donde se descargue en local
        """
        for dic_label in self.list:
            for atrib in dic_label:
                if dic_label[atrib][0:7] == "http://":
                    old_atrib = dic_label[atrib]
                    new_atrib = dic_label[atrib].split("/")[-1]
                    urlretrieve(old_atrib, new_atrib)
                    dic_label[atrib] = new_atrib

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python3 karaoke.py file.smil")
    try:
        objeto = KaraokeLocal(sys.argv[1])
    except (ValueError, IndexError, FileNotFoundError):
        sys.exit("Usage: python3 karaoke.py file.smil")
    print(objeto)
    objeto.to_json(sys.argv[1])
    objeto.do_local()
    objeto.to_json(sys.argv[1], 'local.json')
    print(objeto)
