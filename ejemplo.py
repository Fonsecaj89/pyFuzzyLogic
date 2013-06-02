# -*- coding: utf-8 -*-
import LogicaDifusa as ld

altura = ld.declararConjunto("Altura",0,100)
ld.variableLinguistica(altura,"Baja")
ld.variableLinguistica(altura,"Media")
ld.variableLinguistica(altura,"Alta")

ld.asignarFuncionPertenencia(altura,0,"Triangular",(0,33,66))
ld.asignarFuncionPertenencia(altura,1,"Triangular",(33,66,100))
ld.asignarFuncionPertenencia(altura,2,"Trapezoidal_Derecho",(66,100))


agua = ld.declararConjunto("Agua",0,240)
ld.variableLinguistica(agua,"Poca")
ld.variableLinguistica(agua,"Media")
ld.variableLinguistica(agua,"Mucha")

ld.asignarFuncionPertenencia(agua,0,"Triangular",(0,80,160))
ld.asignarFuncionPertenencia(agua,1,"Triangular",(80,160,240))
ld.asignarFuncionPertenencia(agua,2,"Trapezoidal_Derecho",(100,240))


presion = ld.declararConjunto("Presion",0,150)
ld.variableLinguistica(presion,"Baja")
ld.variableLinguistica(presion,"Media")
ld.variableLinguistica(presion,"Alta")

ld.asignarFuncionPertenencia(presion,0,"Triangular",(0,50,100))
ld.asignarFuncionPertenencia(presion,1,"Triangular",(50,100,150))
ld.asignarFuncionPertenencia(presion,2,"Trapezoidal_Derecho",(100,150))

reglas = ld.iniReglas()
ld.crearReglas(reglas,"if Agua is Poca and Altura is Baja then Presion is Baja")
ld.crearReglas(reglas,"if Agua is Media and Altura is Baja then Presion is Baja")
ld.crearReglas(reglas,"if Agua is Mucha and Altura is Baja then Presion is Media")

ld.crearReglas(reglas,"if Agua is Poca and Altura is Media then Presion is Baja")
ld.crearReglas(reglas,"if Agua is Media and Altura is Media then Presion is Media")
ld.crearReglas(reglas,"if Agua is Mucha and Altura is Media then Presion is Media")

ld.crearReglas(reglas,"if Agua is Poca and Altura is Alta then Presion is Media")
ld.crearReglas(reglas,"if Agua is Media and Altura is Alta then Presion is Alta")
ld.crearReglas(reglas,"if Agua is Mucha and Altura is Alta then Presion is Alta")


fagua = ld.fusificar(70,agua)
faltura = ld.fusificar(45,altura)


motor = ld.inicializarMotor()
ld.agregarAlMotor(motor,agua,fagua)
ld.agregarAlMotor(motor,altura,faltura)

resultado = ld.procesar(reglas,motor,presion)
print resultado


