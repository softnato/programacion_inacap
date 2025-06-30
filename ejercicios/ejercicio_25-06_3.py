#solicitar al usuario  ingresar 5 numeros y
# calcular la suma de esa cantidad de numeros

suma = 0

for i in range (1,6) :
    num = float(input('ingrese numero'))
    suma += num
print (f'{suma}') 