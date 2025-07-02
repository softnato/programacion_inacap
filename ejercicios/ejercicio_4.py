#crear una funcion que permita convertir temperatura de kelvin a celcius
# c° = k - 273.15


def fahrenheit_celcius(temperatura):
    try:
        resultado = 59 * temperatura - 32
        return resultado
    except:
        print('valor ingresado NO corresponde')

def celcius_kelvin(temperatura):
    try:
        resultado = temperatura + 273
        return resultado
    except:
        print('valor ingresado NO corresponde')

def celcius_fahrenheit(temperatura):
    try:
        resultado = 95* temperatura + 32
        return resultado
    except:
        print('valor ingresado NO corresponde')

def kelvin_celcius(temperatura) :
    try:
     resultado = temperatura - 273.15
     return resultado
    except:
     print('valor ingresado NO corresponde')

def kelvin_fahrenheit(temperatura): 
    try:
        celcius = kelvin_celcius(temperatura)
        resultado = celcius_fahrenheit(celcius)
        return resultado
    except:
        print('valor ingresado NO corresponde')

def fahrenheit_kelvin(temperatura):
    try:
        celcius = fahrenheit_celcius(temperatura)
        resultado = celcius_kelvin(celcius)
        return resultado
    except:
        print('valor ingresado NO corresponde')

def interfaz_usuario():
    print('Sistema conversor de temperaturas')
    print('=================================')
    while True:
        print('¿desde que escala de temperatura desea convertir?')
        print('1.- kelvin')
        print('2.- Celcius')
        print('3.- Fahrenheit')
        escala_inicial = input('seleccione su opcion [1-3] : ')
        print('¿A que escala de temperatura desea convertir?')
        print('1.- kelvin')
        print('2.- Celcius')
        print('3.- Fahrenheit')
        escala_final= input('seleccione su opcion [1-3] : ')
        temperatura_usuario = input('¿Cual es su temperatura?')
        try:
            if temperatura_usuario != None:
                temperatura = float(temperatura_usuario)
                if escala_inicial == '1' and escala_final =='2' :
                    resultado = kelvin_celcius(temperatura)
            print(f'{temperatura_usuario}{escala_inicial} = {resultado} {escala_final}')
        except:
            print('valor ingresado No corresponde....')

interfaz_usuario()
