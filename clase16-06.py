
### OPERADORES DE COMPARACION ###


#operador equivalente
print('operador eqivalente')
print('5==4')
print(5==4)
print('5==5')
print(5==5)

#operador mayor que, menor que, o igual
print('5>4', 5<4)
print('5>8', 5<8)

print('5>=8', 5<=8)
print('5<=4', 5<=4)

#operedor dintinto de
print('5!=4','=', 5!=4)
print('3!=3', '=', 3!=3)


###OPERADORES LOGICOS###

## Y y O

''' v o v = v
    v o f = v
    f o v = v
    f o f = f '''

''' v y v = v
    v y f = f
    f y f = f
    f y v = f '''

print('v o v', True | True )
print('v o f', True | False)
print('f o v', False | True)
print('f o f', False | False)

print('v y v,', True | True)
print('v y f', True | False)
print('f y v', False | True)
print('f y f', False | False) 