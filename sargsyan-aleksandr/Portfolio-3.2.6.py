var_numero = 0

print ("Dime un numero, yo te dire si es par o impar y si es multiplo de 3")
var_numero=int(input())
if var_numero %2 == 0:
    print ("Es par")
else:
    print ("Es impar")
if var_numero %3 == 0:
    print ("Es multiplo de 3")
else:
    print ("No es multiplo de 3")