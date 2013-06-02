# -*- coding: utf-8 -*-
import weakref
import FuncionDePertenencia as fp

class Conjunto:
    """Inicializa el conjunto con sus variables linguisticas,
       luego crea la funciones de pertenencia con el intervalo"""

    instances = []
    def __init__(self,nombre):
        self.__class__.instances.append(weakref.proxy(self))
        self.nombre = nombre
        self.vl = []
        self.valIni = 0
        self.valFinal = 0


    def universo(self, intervalo):
        self.valIni, self.valFinal = intervalo

    def obtenerNombre(self):
        return self.nombre

    def asignarVariableLinguistica(self,vl):
        self.vl.append(vl)

    def obteneVariablesLinguisticas(self):
        return self.vl

    def asignarFuncionPertenencia(self,var,tipo,intervalo):
        i = int(var)
        if (min(intervalo) >= self.valIni) or (max(intervalo) <= self.valFinal):
            self.vl[i] =  {self.vl[i]:[tipo,intervalo]}
        else:
            print "El intervalo de la funcion debe estar entre [",self.valIni,",",self.valFinal,"]"

    def obtenerFuncionPertenencia(self,i):
        return self.vl[i]

    def obtenerFuncionPertenenciaPorValor(self,valor):
        for vl in self.vl:
            et = vl.keys()
            if valor in vl[et[0]][1]:
                if min(vl[et[0]][1]) == valor:
                    return et[0]


class Fuzificacion:
    """Se unifican las variables linguisticas por conjunto y se calcula el grado de pertenencia"""
    def __init__(self,entrada,conjunto):
        self.entrada = entrada
        self.conjunto = conjunto
        self.etiquetaMin = ""
        self.valorDifusoMin = 0
        self.etiquetaMax = ""
        self.valorDifusoMax = 0


    """Calcular el grado de pertenencia"""
    def calcularGradoPertenencia(self):
        gdp = []

        for i, v in enumerate(self.conjunto.obteneVariablesLinguisticas()):
            for valLing, funPer in self.conjunto.obteneVariablesLinguisticas()[i].iteritems():

                if (self.entrada >= min(funPer[1])) and (self.entrada <= max(funPer[1])):
                    pcgp = fp.FuncionPertenencia(self.entrada,funPer[0],funPer[1]).determinarFuncion()
                    gdp.append({valLing:pcgp.calcular()})
                else:
                    pass
        if min(gdp).keys()[0] == max(gdp).keys()[0]:
            if min(gdp).get(self.etiquetaMin) == max(gdp).get(self.etiquetaMax):
                self.etiquetaMin = min(gdp).keys()[0]
                self.valorDifusoMin = min(gdp).get(self.etiquetaMin)
        else:
            self.etiquetaMin = min(gdp).keys()[0]
            self.etiquetaMax = max(gdp).keys()[0]
            self.valorDifusoMin = min(gdp).get(self.etiquetaMin)
            self.valorDifusoMax = max(gdp).get(self.etiquetaMax)

    def obtenerEtiquetaResultado(self):
        if self.etiquetaMax == "":
            return self.etiquetaMin
        else:
            return self.etiquetaMin, self.etiquetaMax

    def obtenerValorDifuso(self):
        if self.valorDifusoMax == 0:
            return self.valorDifusoMin
        else:
            return self.valorDifusoMin, self.valorDifusoMax




