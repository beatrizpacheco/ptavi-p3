#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.label = {'root-layout': ['width', 'height', 'background-color'],
                      'region': ['id', 'top', 'bottom', 'left', 'right'],
                      'img': ['src', 'region', 'begin', 'dur'],
                      'audio': ['src', 'begin', 'dur'],
                      'textstream': ['src', 'region']
                      }

    def startElement(self, name, attrs):
        dic = {}

        if name in self.label:
            dic['name'] = name
            for atributo in self.label[name]:
                dic[atributo] = attrs.get(atributo, "")
            self.lista.append(dic)

    def get_tags(self):
        print(self.lista)


if __name__ == "__main__":
    parser = make_parser()  # Crea el parser (leer linea a linea...)
    cHandler = SmallSMILHandler()  # Crea el handler (para manejar el xml)
    parser.setContentHandler(cHandler)  # Relaciona el parser con el handler
    parser.parse(open('karaoke.smil'))
    cHandler.get_tags()
