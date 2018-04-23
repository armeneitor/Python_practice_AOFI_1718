#Cero e inicializo las variables

edad = 0
nombre = ""

#Pregunta la edad
edad = int (input ("Dime tu edad:\n"))

#Comprobamos di el usuario es mayo o menor de edad
if edad > 17:
	nombre = input ("Introduce tu nombre:\n")
	print("Hola ", nombre)
else: 
	print("El programa es sólo para mayores de edad")
print ("Hasta Pronto Fenomeno")