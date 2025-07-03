# Programa que pide dos números y determina cuál es el mayor, el menor o si son iguales

def comparar_numeros(num1, num2):
    if num1 > num2:
        print (f"El número {num1} es mayor que {num2}.")
    elif num1 < num2:
        print ( f"El número {num1} es menor que {num2}.")
    else:
        print ("Los números son iguales.")