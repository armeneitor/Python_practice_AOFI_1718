#Pregunta el primer numero
numero1 = int (input ("Dime un numero mayor que 0:\n"))
if 	numero1 > 0:
	#Pregunta el segundo numero
	numero2 = int (input ("Dime un numero mayor que el primero:\n"))
	if numero2 > numero1:
		#Pregunta el tercer numero
		numero3 = int (input ("Dime un numero menor que el 0:\n"))
		if numero3 < 0:
			print (numero1, " + ",numero2, " + ", numero3, " = ", (numero1+numero2+numero3))
