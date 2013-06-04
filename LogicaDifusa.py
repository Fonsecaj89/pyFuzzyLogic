# -*- coding: utf-8 -*-
from ConjuntoDifuso import Conjunto, Fuzificacion
from ReglasDifusas import Reglas
from InferenciaDifusa import Inferencia
from Desfusificador import Desfusificador



"""Se crean los conjuntos difusos junto con el intervalo de accion
    Recuerda que debes declarar almenos 2 conjuntos que recibiran los datos iniciales
    y el conjunto de salida"""
def declararConjunto(conjunto,valorInicio,valorFinal):
    c = Conjunto(conjunto)
    c.universo((valorInicio,valorFinal))
    return c


"""Se Asignan las variables difusas pertenecientes a cada Conjunto"""
def variableLinguistica(conjunto,variable):
    conjunto.asignarVariableLinguistica(variable)

"""Se asignan las funciones de pertenencia a cada una de las variables por conjunto,
   las coordenadas son:

   -X para la funcion del tipo Singleton,
   -X,Y para la funcion del tipo Gausiana y del tipo Sigmoide
   -X,Y,Z para la funcion del tipo Triangular y del tipo Campana
   -A,B,C,D para la funcion del tipo Trapezoidal
"""
def asignarFuncionPertenencia(conjunto,indiceVariable,tipoFuncion,coordenadas):
    conjunto.asignarFuncionPertenencia(indiceVariable,tipoFuncion,(coordenadas))


"""Para obtener el tipo de funcion de pertenencia"""
def tipoFuncion(conjunto,indiceVariable,nombreVariable):
    return conjunto.obtenerFuncionPertenencia(indiceVariable)[nombreVariable][0]


"""Para obtener las coordenadas de la funcion de pertenencia"""
def coordenadasFuncion(conjunto,indiceVariable,nombreVariable):
    return conjunto.obtenerFuncionPertenencia(indiceVariable)[nombreVariable][1]


"""Se inicializa la instancia de la clase Reglas"""
def iniReglas():
    reglas = Reglas()
    return reglas


"""Para crear las reglas difusas"""
def crearReglas(instanciaReglas,regla):
    instanciaReglas.crear(regla)


"""Una vez definidos los conjuntos con sus variables difuzas y el universo del conjunto difuso,
   y luego de definir las reglas, se procede transformar el valor de entrado en un valor difuso

   Los valores a utilizar son:
       -El numero a evaluar
       -El conjunto en donde se va a evaluar"""
def fusificar(valor,conjunto):
    vaf = Fuzificacion(valor,conjunto)
    vaf.calcularGradoPertenencia()
    return vaf


"""Se inicializa el motor de inferencia antes de procesar"""
def inicializarMotor():
    motor = Inferencia()
    return motor


"""Se agrega el motor inicializado, el conjunto inicialmente declarado y el conjunto difuso resultado
   de "Fuzificar" """
def agregarAlMotor(instanciaMotor,conjunto,conjuntoDifuso):
    if len(conjuntoDifuso.obtenerEtiquetaResultado()) == 2:
        emin, emax = conjuntoDifuso.obtenerEtiquetaResultado()
        vmin, vmax = conjuntoDifuso.obtenerValorDifuso()
        instanciaMotor.agregarConjuntoDifuso([conjunto.obtenerNombre(),emin,vmin])
        instanciaMotor.agregarConjuntoDifuso([conjunto.obtenerNombre(),emax,vmax])
    else:
        emin = conjuntoDifuso.obtenerEtiquetaResultado()
        vmin = conjuntoDifuso.obtenerValorDifuso()
        instanciaMotor.agregarConjuntoDifuso([conjunto.obtenerNombre(),emin,vmin])


"""Se procesan los datos iniciales y retornara el nombre de la variable linguistica del conjunto de
   salida ganadora y el valor numerico desfusificado"""
def procesar(instanciaReglas,instanciaMotor,conjuntoSalida):

    for regla in instanciaReglas.obtenerReglas():
        instanciaMotor.agregarReglas(regla)

    instanciaMotor.procesarReglas()

    """Activamos el motor de inferencia difusa pasandole el conjunto de salida como parametro"""
    resultado = instanciaMotor.motorDifuso(conjuntoSalida)
    valdes = Desfusificador(resultado)
    resdis = valdes.obtenerValorDesfusificado()
    etiquetaResultado = valdes.obtenerEtiquetaResultado()
    return etiquetaResultado, resdis





