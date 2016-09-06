#!/usr/bin/env python3.4
# -*- encoding: utf-8 -*-

def factorial(n):
	fact = 1 #determinamos el valor de inicialización en 1
	for x in range (1 , n +1):
		fact = fact * x
	return fact
		
def main():
	val = int(input ("cuantos numeros va a ingresar: "))
	for x in range (1 , val + 1):
		v1 = int(input("ingrese un número: "))
		print ("el valor numero: " + str(x) + " " + " y su factorial es: " + str(factorial(v1)))
			
main()
