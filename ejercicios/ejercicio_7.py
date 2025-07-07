#escribir un programa que calcule el area y el perimetro de un cuadrado,
#si cuyalquier valor es negativo, se debe entregar un mensaje de error

def area_perimetro_cuadrado() :
    try:
        lado = float(input('ingrese valor del lado: '))
        if lado >= 0:
            print(f'el area del cuadrado de lado {lado} = {lado*lado} ')
            print(f'el perimetro del cuadrado de lado {lado} = {round(lado*4,2)}')
        else :
            print('no se permite ingresar valores negativos')
    except:
        print('valor ingresado no corresponde a un numero...')

area_perimetro_cuadrado()