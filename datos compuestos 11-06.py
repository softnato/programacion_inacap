#datos compuestos

numero_entero = 2
numero_decimal = 2.4
cadena_de_texto_1 = 'esto es una cadena de texto'
dato_verdadero = True



print(type(numero_entero))
print(type(numero_decimal))
print(type(cadena_de_texto_1))
print(type(dato_verdadero))


#listas
'''una lista es una coleccion ORDENADA de elementos de cualquier tipo de datos,
  los elementos se separan por comas'''
# Ademas de ser una coleccion ordenada tambien es "MUTABLE"

lista_1 = ['cadena de texto', 49, True, 43.98,[1,2,3,4,5]]
print(type(lista_1))
print(lista_1)
print(len(lista_1))

# 'len' nos sirve para saber la cantidad de elementos que tiene una lista

print(lista_1[0])

#imprimir y luego colocar corchetes llamo a los elementos de la lista

print(lista_1[3])

lista_1[1] = 'hola'
print(lista_1)

#agregar elemento a la lista

lista_1.append(False)
print(lista_1)

#quitar elemento de la listo 
lista_1.pop() # <--- se quita el ultimo elemento <----
print(lista_1)
lista_1.pop(3) #   <---- añadiento el numero del elemento al indice se borra ese elemento <----
print(lista_1)

# borrar todos los elementos de la lista "clear"

lista_1.clear()
print(lista_1)


#"insert" para insertar un elemento en la lista colocando en el indice el numero donde quieres ingresarlo


lista_1.insert(3,'chao')
print(lista_1)
