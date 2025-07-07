def calculadora_basica():

    try:          
        num1 = float(input('ingrese primer numero: '))
        num2 = float(input('ingrese segundo numero: '))
        resultado = num1 + num2 
        print(f'{num1} + {num2} = {resultado}')
        resultado = num1 - num2 
        print(f'{num1} - {num2} = {resultado}')
        resultado = num1 * num2 
        print(f'{num1} * {num2} = {resultado}')
        if num2 != 0:
            resultado = num1 / num2 
            print(f'{num1} / {num2} = {resultado}')
        else:
            print('no se puede dividir por cero')
    except:
        print('valor ingresado no corresponde a un numero')

calculadora_basica()
        