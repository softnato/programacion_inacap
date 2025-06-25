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