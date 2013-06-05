# -*- coding: utf-8 -*-
import LogicaDifusa as ld

calorias = ld.declararConjunto("Calorias_Quemadas",0,500)
ld.variableLinguistica(calorias,"Pocas")
ld.variableLinguistica(calorias,"Intermedias")
ld.variableLinguistica(calorias,"Muchas")

ld.asignarFuncionPertenencia(calorias,0,"Triangular",(0,166,332))
ld.asignarFuncionPertenencia(calorias,1,"Triangular",(166,332,499))
ld.asignarFuncionPertenencia(calorias,2,"Trapezoidal_Derecho",(332,500))


sudor = ld.declararConjunto("Sudor_Perdido",0,1000)
ld.variableLinguistica(sudor,"Poco")
ld.variableLinguistica(sudor,"Moderado")
ld.variableLinguistica(sudor,"Excesivo")

ld.asignarFuncionPertenencia(sudor,0,"Triangular",(0,333,665))
ld.asignarFuncionPertenencia(sudor,1,"Triangular",(333,666,999))
ld.asignarFuncionPertenencia(sudor,2,"Trapezoidal_Derecho",(667,1000))



liquido = ld.declararConjunto("Liquido",0,5000)
ld.variableLinguistica(liquido,"Poco")
ld.variableLinguistica(liquido,"Moderado")
ld.variableLinguistica(liquido,"Mucho")

ld.asignarFuncionPertenencia(liquido,0,"Triangular",(0,1666,3319))
ld.asignarFuncionPertenencia(liquido,1,"Triangular",(1666,3320,4999))
ld.asignarFuncionPertenencia(liquido,2,"Trapezoidal_Derecho",(3321,5000))

reglas = ld.iniReglas()
ld.crearReglas(reglas,"if Calorias_Quemadas is Pocas and Sudor_Perdido is Poco then Liquido is Poco")
ld.crearReglas(reglas,"if Calorias_Quemadas is Intermedias and Sudor_Perdido is Poco then Liquido is Poco")
ld.crearReglas(reglas,"if Calorias_Quemadas is Muchas and Sudor_Perdido is Poco then Liquido is Moderado")

ld.crearReglas(reglas,"if Calorias_Quemadas is Pocas and Sudor_Perdido is Moderado then Liquido is Poco")
ld.crearReglas(reglas,"if Calorias_Quemadas is Intermedias and Sudor_Perdido is Moderado then Liquido is Moderado")
ld.crearReglas(reglas,"if Calorias_Quemadas is Muchas and Sudor_Perdido is Moderado then Liquido is Moderado")

ld.crearReglas(reglas,"if Calorias_Quemadas is Pocas and Sudor_Perdido is Excesivo then Liquido is Moderado")
ld.crearReglas(reglas,"if Calorias_Quemadas is Intermedias and Sudor_Perdido is Excesivo then Liquido is Mucho")
ld.crearReglas(reglas,"if Calorias_Quemadas is Muchas and Sudor_Perdido is Excesivo then Liquido is Mucho")


fcalorias = ld.fusificar(80,calorias)
fsudor = ld.fusificar(40,sudor)


motor = ld.inicializarMotor()
ld.agregarAlMotor(motor,calorias,fcalorias)
ld.agregarAlMotor(motor,sudor,fsudor)

resultado = ld.procesar(reglas,motor,liquido)
print resultado


