#! /usr/bin/python3.4
#-*- coding: utf-8 -*-

"""
domino: No recibe argumentos --> No devuelve valores
        Imprime en pantalla una ficha de domino por linea
"""

def domino ():
    print ("Muestra en pantalla las fichas de domino")
    domUp = 0
    domDown   = 0
    for x in range (0, 7):
        if domDown < domUp:
            domUp = 0
            domDown = domDown + 1
        while domDown >= domUp:
            if domDown == domUp:
                separador = "\n"
            else:
                separador = " "
            print ("[" + str (domDown) + " | " + str(domUp) + "]", end = separador)
            domUp = domUp + 1

domino()
