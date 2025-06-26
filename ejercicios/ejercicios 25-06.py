# Escriba una tabla de multiplicar que muestre las tablas de multiplicar del 1 al 10

print()
print('tabls de multiplicar')

for numero in range(1,11) : 
    print()
    print (f'tabla del {numero}')
    print('================')
    for num in range (1,11) :
        print(f'{numero} x {num} = {numero * num}')


print()
print('las tablas de multiplicar con ciclo WHILE')
numero = 1
while numero <= 10:
    print()
    print(f'tabla del {numero}')
    print('============')
    num = 1
    while num <= 10 :
        print(f'{numero} x {num} = {numero * num}')
        num += 1
    numero += 1
    
    
#escribir un programa que pida al usuario dos numeros y muestre su suma, su resta , su multiplicacion y su division
# si el divisor es cero el programa debe mostrar un error




numero_1 =float(input("ingrese el primer numero : "))
numero_2 = float(input("ingrese el segundo numero : "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2

print('============')
print('Suma =', suma)
print('============')
print('resta:', resta)
print('============')
print('multiplicacion:', multiplicacion)
print('============')
if numero_2 == 0 : 
    print ('error : no se puede dividir por cero')
    
else:
    division = numero_1 / numero_2

    print('division:', division)
