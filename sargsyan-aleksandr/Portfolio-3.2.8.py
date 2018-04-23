import time
Comida=0
Dia=0
Almuerzo={}
Cena={}
Semana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print ("¿Que quieres comer esta semana?")
time.sleep(2)
for Dia in Semana:
		Comida=input("¿Que quieres Almuerzar?\n")
		Almuerzo[Dia]=Comida
		Comida=input("¿Que quieres Cenar?\n")
		Cena[Dia]=Comida
print("Menu de la semana")
time.sleep(2)
for Dia in Semana:		
	print (Dia, "-", "Almuerzo:", Almuerzo[Dia], "Cena:", Cena[Dia])
	time.sleep(2)
