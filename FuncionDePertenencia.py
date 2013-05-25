# -*- coding: utf-8 -*-
import math
"""
    -Crear cada clase por cada tipo geometrico
    -Inicializar la figura geometrica con sus cordenadas
    -Calcular el área
"""
def trapezoidal(x,a,b,c,d):
    if x<=a:
        vp = 0
    if (x>=a) and (x<=b):
        vp = (x-a)/(b-a)
    if (x>=b) and (x<=c):
        vp = 1
    if (x>=c) and (x<=d):
        vp = (d-x)/(d-c)
    if x>=d:
        vp = 0

def triangular(x,a,b,c):
    if x<=a:
        vp = 0
    if (x>=a) and (x<=b):
        vp = (x-a)/(b-a)
    if (x>=b) and (x<=c):
        vp = (c-x)/(c-b)
    if x>=c:
        vp = 0

def singleton(x,a):
    if x==a:
        vp = 1
    else:
        vp = 0

def gausiana(x,c,y):
    vp = math.exp(-1*(((x-c)/y)**2))
    print vp


def campana(x,a,b,c):
    vp = 1/(1+math.fabs((x-c)/a)**(2*b))

def sigmoide(x,a,b,c):
    vp = 1/(1+math.exp(-a*(x-c)))
    print vp
