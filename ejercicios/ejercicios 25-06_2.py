#escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta


contraseña = 'intro_progre'

contraseña_usuario = ''
while contraseña_usuario != contraseña:
    contraseña_usuario = input('ingrese contraseña')
else:
    print('ingreso correcto!')