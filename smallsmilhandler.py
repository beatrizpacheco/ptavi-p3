#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar SMIL
    """
    
    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """

        self.lista = []
    
    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        dic = {}
        
        if name == 'root-layout':
            dic['name'] = name
            dic['width'] = attrs.get('width', "")
            dic['height'] = attrs.get('height', "")
            dic['background_color'] = attrs.get('background_color', "")
            self.lista.append(dic)
        elif name == 'region':
            dic['name'] = name
            dic ['id'] = attrs.get('id', "")
            dic ['top'] = attrs.get('top', "")
            dic ['bottom'] = attrs.get('bottom', "")
            dic ['left'] = attrs.get('left', "")
            dic ['right'] = attrs.get('right', "")
            self.lista.append(dic)
        elif name == 'img':
            dic['name'] = name
            dic ['src'] = attrs.get('src', "")
            dic ['region'] = attrs.get('region', "")
            dic ['begin'] = attrs.get('begin', "")
            dic ['dur'] = attrs.get('dur', "")
            self.lista.append(dic)
        elif name == 'audio':
            dic['name'] = name
            dic ['src'] = attrs.get('src', "")
            dic ['begin'] = attrs.get('begin', "")
            dic ['dur'] = attrs.get('dur', "")
            self.lista.append(dic)
        elif name == 'textstream':
            dic['name'] = name
            dic['src'] = attrs.get('src', "")
            dic ['region'] = attrs.get('region', "")
            self.lista.append(dic)

    def get_tags(self):
        print(self.lista)


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser() #Crea el parser (leer linea a linea...)
    cHandler = SmallSMILHandler() #Crea el handler (para manejar el xml)
    parser.setContentHandler(cHandler) #Relaciona el parser con el handler
    parser.parse(open('karaoke.smil')) #Con el parser abre el documento de chistes
    cHandler.get_tags()
