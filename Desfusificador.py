# -*- coding: utf-8 *-*
"""
    -Obtener la forma geométrica obtenida de la inferencia
    -Crear la Clase Mandani y Clase del Japonés
    -Centroide por cada tipo de clase
    -Generar valor final
"""

class Desfusificador:

    def __init__(self,trapecio):
        self.trapecio = trapecio
        self.centroide = 0
        self.calcularCentroide()


    def calcularCentroide(self):
        for trap in self.trapecio:
            a,b,c,d,altura = trap

            puntoMedio = (d-a)/2
            intervalo = d-a
            Base = d-a
            area = Base*(altura-((altura**2)/2))
            print area

            self.centroide = self.centroide +((puntoMedio*(intervalo*(area)))/(intervalo*area))
            print self.centroide

    def obtenerValorDesfusificado(self):
        return self.centroide

    def obtenerEtiquetaResultado(self):
        pass