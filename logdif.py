# -*- coding: utf-8 -*-
from ConjuntoDifuso import Conjunto, Fuzificacion
from ReglasDifusas import Reglas
from InferenciaDifusa import Inferencia
from Desfusificador import Desfusificador


"""Se crean los conjuntos difusos"""
a = Conjunto("Temperatura")
a.universo((0,6))
b = Conjunto("Clima")
b.universo((0,6))
c = Conjunto("Intencion")
b.universo((0,4))

"""Se Asignan las variables difusas pertenecientes a cada Conjunto"""
a.asignarVariableLinguistica("Frio")
a.asignarVariableLinguistica("Tibio")
a.asignarVariableLinguistica("Caliente")

b.asignarVariableLinguistica("Lluvioso")
b.asignarVariableLinguistica("Nublado")
b.asignarVariableLinguistica("Soleado")

c.asignarVariableLinguistica("Dormir")
c.asignarVariableLinguistica("No_Salir")
c.asignarVariableLinguistica("Pasear")



"""Asignamos a la primera variable del Conjunto 'Temperatura' la funcion de pertenencia del tipo 'Triangulo' con las
   coordenadas (0,1,2)"""
a.asignarFuncionPertenencia(0,"Triangular",(0,1,2))
a.asignarFuncionPertenencia(1,"Trapezoidal",(1,3,4,5))
a.asignarFuncionPertenencia(2,"Triangular",(4,5,6))

b.asignarFuncionPertenencia(0,"Triangular",(0,1,2))
b.asignarFuncionPertenencia(1,"Trapezoidal",(1,3,4,5))
b.asignarFuncionPertenencia(2,"Triangular",(4,5,6))

c.asignarFuncionPertenencia(0,"Triangular",(0,1,2))
c.asignarFuncionPertenencia(1,"Triangular",(1,2,3))
c.asignarFuncionPertenencia(2,"Triangular",(2,3,4))


"""Para obtener el tipo de funcion de pertenencia"""
#print a.obtenerFuncionPertenencia(0)['Frio'][0]


"""Para obtener las coordenadas de la funcion de pertenencia"""
x,y,z = a.obtenerFuncionPertenencia(0)['Frio'][1]
#print x,y,z



#print "Al conjunto", "'"+a.obtenerNombre()+"'", "Pertenecen las siguientes variables ", a.obteneVariablesLinguisticas()
#print "Al conjunto", "'"+b.obtenerNombre()+"'", "Pertenecen las siguientes variables ", b.obteneVariablesLinguisticas()
#print "Seleccionamos la primera variable del conjunto 'Temperatura' ", a.obteneVariablesLinguisticas()[0]
#print "Seleccionamos la segunda variable del conjunto 'Temperatura' ", a.obteneVariablesLinguisticas()[1]



"""Para crear las reglas difusas"""
r = Reglas()
r.crear("if Temperatura is Frio and Clima is Nublado then Intencion is Dormir")
r.crear("if Temperatura is Tibio and Clima is Soleado then Intencion is Pasear")
r.crear("if Temperatura is Caliente and Clima is Soleado then Intencion is No_Salir")

#print r.obtenerReglas()


"""Una vez definidos los conjuntos con sus variables difuzas y el universo del conjunto difuso,
   y luego de definir las reglas, se procede transformar el valor de entrado en un valor difuso

   Los valores a ingresar en Fuzificacion son:
       -El numero a evaluar
       -El conjunto en donde se va a evaluar"""

vda = Fuzificacion(4.85,a)
vda.calcularGradoPertenencia()
print vda.obtenerEtiquetaResultado()
print vda.obtenerValorDifuso()

vdb = Fuzificacion(5.89,b)
vdb.calcularGradoPertenencia()
print vdb.obtenerEtiquetaResultado()
print vdb.obtenerValorDifuso()



"""Luego de fuzificar el valor de entrada, se ingresa al motor de Inferencia Difusa"""
motor = Inferencia()

motor.agregarConjuntoDifuso([a.obtenerNombre(),vda.obtenerEtiquetaResultado(),vda.obtenerValorDifuso()])
motor.agregarConjuntoDifuso([b.obtenerNombre(),vdb.obtenerEtiquetaResultado(),vdb.obtenerValorDifuso()])

for regla in r.obtenerReglas():
    motor.agregarReglas(regla)

motor.procesarReglas()

"""Activamos el motor de inferencia difusa pasandole el conjunto de salida como parametro"""
resultado = motor.motorDifuso(c)

valdes = Desfusificador(resultado)
resdis = valdes.obtenerValorDesfusificado()
etiquetaResultado = c.obtenerFuncionPertenenciaPorValor(resdis)
print "El valor desfusificado de",etiquetaResultado ,"es", resdis

