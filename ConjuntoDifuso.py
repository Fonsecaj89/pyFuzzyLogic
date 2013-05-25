# -*- coding: utf-8 -*-

class Conjunto:
    """Inicializa el conjunto con sus variables linguisticas,
       luego crea la funciones de pertenencia con el intervalo"""
    def __init__(self,nombre):
        self.nombre = nombre
        self.vl = []

    def obtenerNombre(self):
        return self.nombre

    def asignarVariableLinguistica(self,vl):
        self.vl.append(vl)

    def obteneVariablesLinguisticas(self):
        return self.vl

    def asignarFuncionPertenencia(self,var,tipo,intervalo):
        i = int(var)
        self.vl[i] =  {self.vl[i]:[tipo,intervalo]}

    def obtenerFuncionPertenencia(self,i):
        return self.vl[i]



class Fuzificacion:
    """Se unifican las variables linguisticas por conjunto y se calcula el grado de pertenencia"""
    def __init__(self,entrada):
        pass