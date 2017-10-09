#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class ChistesHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.calificacion = ""
        self.pregunta = ""
        self.inPregunta = False
        self.respuesta = ""
        self.inRespuesta = False
        self.variable = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'chiste':
            # De esta manera tomamos los valores de los atributos
            self.calificacion = attrs.get('calificacion', "")
            self.variable.append(self.calificacion)
        elif name == 'pregunta':
            self.inPregunta = True
        elif name == 'respuesta':
            self.inRespuesta = True

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'pregunta':
            self.variable.append(self.pregunta)
            self.pregunta = ""
            self.inPregunta = False
        if name == 'respuesta':
            self.variable.append(self.respuesta)
            self.respuesta = ""
            self.inRespuesta = False

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if self.inPregunta:
            self.pregunta = self.pregunta + char
        if self.inRespuesta:
            self.respuesta += char #Equivale a self.pregunta + char

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser() #Crea el parser (leer linea a linea...)
    cHandler = ChistesHandler() #Crea el handler (para manejar el xml)
    parser.setContentHandler(cHandler) #Relaciona el parser con el handler
    parser.parse(open('chistes2.xml')) #Con el parser abre el documento de chistes
    print(cHandler.variable)
