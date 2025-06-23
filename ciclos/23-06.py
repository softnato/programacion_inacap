#ciclo for

#recorrer una lista con for, MUESTRA LOS ELEMENTOS DE LA LISTA!!!!!!!
animales =['perro','canario', 'panda', 'gato', 'capibara']
contador = 0
for elemento in animales:
    contador = contador + 1
    print(f'mi animal es {contador} : {elemento}')
   
    
usuarios = ['aquiles baeza','wendy sulca','delfin quispe']
    
contador = 0
for nombre in usuarios:
        contador = contador + 1
        print(f'usuario {contador}:{nombre}')
        
for i in range(len(usuarios)):
    
    print(f'usuario {i+1}: {usuarios[i]}')
#recorrer un str con for  
cadena = 'introduccion programacion'
for letra in cadena :
    print(letra.upper())