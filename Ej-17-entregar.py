#-*- enconding:utf-8 -*-

"""
Analisis: Lo pedido en la función es que se asocien determinados valores 
	numéricos con una "etiqueta" asociada a temperaturas del ambiente.
Especificacion:
El usuario ingresa un numero, al cual se lo clasifica segun su valor,
y se le asocia una etiqueta de temperatura.
Diseño:
	Pide al usuario un valor y lo almacena en una variable temperatura.
	Si temperatura es inferior a 0 grados se imprime "Helado"
	Si temperatura esta entre 0 y 15 grados se imprime "Frio"
	Si temperatura esta entre 15 y 25 grados se imprime "Agradable"
	Si temperatura es mayor a 25 grados se imprime "Caluroso"
"""

def observar_clima(temperatura):
	"""
	La función toma el valor temperatura y lo clasifica.
	
	args:
		number
	return:
		number
		
	"""
	
	if temperatura < 0:
		return "Helado"
	elif temperatura >= 0 and temperatura < 15:
		return "Frio"
	elif temperatura >= 15 and temperatura < 25:
		return "Agradable"
	else:
		return "Caluroso"

def main():
	"""
	Función principal del programa, pide al usuario una temperatura y llama a la funcion
	observar_clima con ese argumento.
	args: 
		no posee
	return :
		no devuelve valores
	"""
	temperatura = int(input("Ingrese una temperatura: "))
	print (observar_clima(temperatura))

def test_observar_clima():
	""" 
	Funcion de casos de prueba, a evaluarse con pytest
	"""
	assert observar_clima(25) == "Caluroso"
	assert observar_clima(10) == "Frio"
	assert observar_clima(-12) == "Helado"
	assert observar_clima(17) == "Agradable"

test_observar_clima()
