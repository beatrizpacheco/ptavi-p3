#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.list = []
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
            self.list.append(dic)

    def get_tags(self):
        return(self.list)

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
