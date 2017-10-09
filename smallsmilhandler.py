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

        self.variable = []
    
    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            
            #self.width = attrs.get('width', "")
            #self.height = attrs.get('height', "")
            #self.background_color = attrs.get('background_color', "")
            self.variable.append(attrs.get('width', ""))
            self.variable.append(attrs.get('height', ""))
            self.variable.append(attrs.get('background_color', ""))
        elif name == 'region':
            #self.id = attrs.get('id', "")
            #self.top = attrs.get('top', "")
            #self.bottom = attrs.get('bottom', "")
            #self.left = attrs.get('left', "")
            #self.right = attrs.get('right', "")
            self.variable.append(attrs.get('id', ""))
            self.variable.append(attrs.get('top', ""))
            self.variable.append(attrs.get('bottom', ""))
            self.variable.append(attrs.get('left', ""))
            self.variable.append(attrs.get('right', ""))
        elif name == 'img':
            #self.src = attrs.get('src', "")
            #self.region = attrs.get('region', "")
            #self.begin = attrs.get('begin', "")
            #self.dur = attrs.get('dur', "")
            self.variable.append(attrs.get('src', ""))
            self.variable.append(attrs.get('region', ""))
            self.variable.append(attrs.get('begin', ""))
            self.variable.append(attrs.get('dur', ""))
        elif name == 'audio':
            #self.src = attrs.get('src', "")
            #self.begin = attrs.get('begin', "")
            #self.dur = attrs.get('dur', "")
            self.variable.append(attrs.get('src', ""))
            self.variable.append(attrs.get('begin', ""))
            self.variable.append(attrs.get('dur', ""))
        elif name == 'textstream':
            #self.src = attrs.get('src', "")
            #self.region = attrs.get('region', "")
            self.variable.append(attrs.get('src', ""))
            self.variable.append(attrs.get('region', ""))

    def get_tags(self):
        print(self.variable)


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser() #Crea el parser (leer linea a linea...)
    cHandler = SmallSMILHandler() #Crea el handler (para manejar el xml)
    parser.setContentHandler(cHandler) #Relaciona el parser con el handler
    parser.parse(open('karaoke.smil')) #Con el parser abre el documento de chistes
    cHandler.get_tags()
