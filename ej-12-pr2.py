#-*- coding: utf-8 -*-
"""
dominoInfinite: No recibe argumentos --> No devuelve valores
        Pide al usuario ingresar la cantidad de fichas a generar
        Imprime en pantalla las fichas
"""

def dominoInfinite ():
    print ("Muestra en pantalla las fichas de domino")
    cantFichas = int(input("Ingrese el número de las fichas: "))
    domUp = 0
    domDown   = 0
    for x in range (0, cantFichas + 1):
        if domDown < domUp:
            domUp = 0
            domDown = domDown + 1
        while domDown >= domUp:
            print ("[" + str (domDown) + " | " + str(domUp) + "]", end = "\n")
            domUp = domUp + 1

dominoInfinite()
