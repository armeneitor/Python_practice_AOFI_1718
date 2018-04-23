import time

minuto=60
#Pregunta un numero para la cuenta atras
print ("Dime un numero para el despegue")
var_numero = int(input())
for i in range (1, var_numero+1):
    time.sleep (1)
    print (var_numero-i)
time.sleep(2)
print ("¡DESPEGE")
