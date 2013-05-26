# -*- coding: utf-8 *-*
"""
    -Obtener la distribución de las reglas para realizar los cálculos
    -Realizar los calculos and, or ó not
    -Clase Truncamiento y Clase Escalado
    -Crear la lista de nuevas figuras geométricas de acuerdo a cada regla
    -Guardar las figuras geométricas
"""

class Inferencia:

    def __init__(self):
        self.reglas = []
        self.conjunto = []
        self.condiciones = []
        self.actuaciones = []
        self.listaReglas = []



    def procesarReglas(self):

        entonces = False

        for regla in self.reglas:
            rlimp = regla.split(' ')
            for word in rlimp:

                if word == "then":
                    entonces = True


                if not entonces:
                    if word == "if":
                        pass
                    else:
                        self.condiciones.append(word)
                else:
                    if word == "then":
                        pass
                    else:
                        self.actuaciones.append(word)
            while "is" in self.condiciones:
                self.condiciones.remove("is")
            while "is" in self.actuaciones:
                self.actuaciones.remove("is")
            self.listaReglas.append([self.condiciones,self.actuaciones])
            self.condiciones = []
            self.actuaciones = []
            entonces = False



    def agregarConjuntoDifuso(self,fuzzyset):
        self.conjunto.append(fuzzyset)

    def agregarReglas(self,regla):
        self.reglas.append(regla)

    def obtenerCondiciones(self):
        return self.condiciones

    def obtenerActuaciones(self):
        return self.actuaciones

    def motorDifuso(self):
        """Corregir!!!"""
        auxa = False
        auxo = False
        auxn = False
        v1 = ""
        v2 = ""
        con = []

        for lr in self.listaReglas:

            for parte in lr:
                for palabra in parte:
                    if palabra == "and":
                        auxa = True
                    if palabra == "Intencion":
                        break
                    print palabra
                    if auxa:
                        auxa = False
                    else:
                        if v1 == "":
                            v1 = palabra
                        else:
                            v2 = palabra
                            con.append((v1,v2))
                            print min(con)
                            v1 = ""
                            v2 = ""

                #elif "or" in parte[0]:
                    #pass
                #elif "not" in parte[0]:
                    #pass
                #else:
                    #pass


    #def and(self,v1,v2):
        #return min(v1,v2)

    #def or(self,v1,v2):
        #return max(v1,v2)

    #def not(self,v):
        #return 1-v

