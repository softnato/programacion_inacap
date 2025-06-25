#WHILE evalua una condicion logica y ejecuta sus tareas en caso de ser verdadero


numero = 0

while numero <= 10:
    numero = numero + 1
    if numero % 2 == 0 :
        print(numero)
        

#solicitar un numero al usuario para imprimir una tabla de multiplicar desde 1 hasta 10 de ese numero

numero_str = input('INGRESE UN NUMERO PARA CREAR SU TABLA D EMULTIPLICAR:')
numero_int = int(numero_str)

#resolvemos con  ciclo for
print(f'tabla del {numero_str} mediante ciclo FOR')
for i in range(1,11):
    print(f'{numero_int} * {i} = {numero_int * i}')


print(f'tabla del {numero_str} mediante ciclo while')
numero = 1
while numero <= 10:
    print(f'{numero_int} x {numero} = {numero_int * numero}')
    numero +=1    
    


