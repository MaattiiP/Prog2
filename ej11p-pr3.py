def bisiesto (mes):
    if mes % 400 == 0:
        return True
    elif mes % 4 == 0 and mes % 100 != 0:
        return True
    else:
        return False

def mesDias(mes, anio):
    if mes in (1,3,5,7,8,10,12):
        return 31
    elif mes in (4,6,9,11):
        return 30
    elif mes == 2 and bisiesto(anio):
        return 29
    else:
        return 28

def restDiasMes (dia, mes, anio):
    diasRestantes = mesDias(mes,anio) - dia
    return diasRestantes

def restDiasAnio (dia, mes, anio):
    suma = 0
    diasRestantes = restDiasMes(dia, mes, anio)
    if mes != 12:
        for x in range (mes+1, 13):
            suma = suma + mesDias(x, anio)
        return suma + diasRestantes
    else:
        return diasRestantes

def diasTranscurridos(dia,mes,anio):
    sumaDias = 0
    for x in range (1,mes):
        sumaDias += mesDias(x, anio)
    return sumaDias + dia


def difTiempo(dia1,mes1,anio1,dia2,mes2,anio2):
	difAnio = 0
	sumaMeses = 0
	difDias = 0
	if mes1 <= mes2:
		difAnio = anio2 - anio1
		sumaMeses = 0
		for x in range (mes1 + 1,mes2):
			sumaMeses += 1
		if dia2 >= dia1:
			sumaMeses += 1
			if dia1 == dia2:
				difDias = 0
			else:
				for x in range (dia1, dia2):
					difDias += 1
	print("Pasaron",difAnio,"años",sumaMeses,"meses",difDias,"dias")


def aux():
    print(difTiempo(1,2,2016,20,1,2016))

aux()
