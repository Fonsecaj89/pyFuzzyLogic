# -*- coding: utf-8 -*-
from ConjuntoDifuso import Conjunto


"""Se crean los conjuntos difusos"""
a = Conjunto("Temperatura")
a.universo((0,6))
b = Conjunto("Estatura")

"""Se Asignan las variables difusas pertenecientes a cada Conjunto"""
a.asignarVariableLinguistica("Frio")
a.asignarVariableLinguistica("Tibio")
a.asignarVariableLinguistica("Caliente")

b.asignarVariableLinguistica("Bajo")
b.asignarVariableLinguistica("Mediano")
b.asignarVariableLinguistica("Alto")




"""Asignamos a la primera variable del Conjunto 'Temperatura' la funcion de pertenencia del tipo 'Triangulo' con las
   coordenadas (0,1,2)"""
a.asignarFuncionPertenencia(0,"Triangular",(0,1,2))
a.asignarFuncionPertenencia(1,"Trapezoidal",(1,3,4,5))
a.asignarFuncionPertenencia(2,"Triangular",(4,5,6))

"""Para obtener el tipo de funcion de pertenencia"""
print a.obtenerFuncionPertenencia(0)['Frio'][0]

"""Para obtener las coordenadas de la funcion de pertenencia"""
x,y,z = a.obtenerFuncionPertenencia(0)['Frio'][1]


print "Al conjunto", "'"+a.obtenerNombre()+"'", "Pertenecen las siguientes variables ", a.obteneVariablesLinguisticas()
print "Al conjunto", "'"+b.obtenerNombre()+"'", "Pertenecen las siguientes variables ", b.obteneVariablesLinguisticas()
print "Seleccionamos la primera variable del conjunto 'Temperatura' ", a.obteneVariablesLinguisticas()[0]
print "Seleccionamos la segunda variable del conjunto 'Temperatura' ", a.obteneVariablesLinguisticas()[1]