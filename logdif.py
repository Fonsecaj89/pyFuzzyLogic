# -*- coding: utf-8 -*-
from ConjuntoDifuso import Conjunto

"""Se crean los conjuntos difusos"""
a = Conjunto("Temperatura")
b = Conjunto("Estatura")

"""Se Asignan las variables difusas pertenecientes a cada Conjunto"""
a.asignarVariableLinguistica("Frio")
a.asignarVariableLinguistica("Tibio")
a.asignarVariableLinguistica("Caliente")

b.asignarVariableLinguistica("Bajo")
b.asignarVariableLinguistica("Mediano")
b.asignarVariableLinguistica("Alto")


print "Al conjunto", "'"+a.obtenerNombre()+"'", "Pertenecen las siguientes variables ", a.obteneVariablesLinguisticas()
print "Al conjunto", "'"+b.obtenerNombre()+"'", "Pertenecen las siguientes variables ", b.obteneVariablesLinguisticas()
print "Seleccionamos la primera variable del conjunto 'Temperatura' ", a.obteneVariablesLinguisticas()[0]

"""Asignamos a la primera variable del Conjunto 'Temperatura' la funcion de pertenencia del tipo 'Triangulo' con las
   coordenadas (0,1,2)"""
a.asignarFuncionPertenencia(0,"Triangular",(0,1,2))

"""Para obtener el tipo de funcion de pertenencia"""
print a.obtenerFuncionPertenencia(0)['Frio'][0]

"""Para obtener las coordenadas de la funcion de pertenencia"""
print a.obtenerFuncionPertenencia(0)['Frio'][1]
