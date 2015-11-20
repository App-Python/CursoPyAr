#! /usr/bin/env python3
# programa ejectable en Unix/Linux
# -*- coding: utf-8 -*-
'''
Created on 19/11/2015

@author: hernan
'''
cuadrados = [1, 4, 9, 16, 25]
print(cuadrados)
print(cuadrados[0])  # índices retornan un ítem
print(cuadrados[-1])
print(cuadrados[-3:])  # rebanadas retornan una nueva lista
print(cuadrados[:])
print()
# Las listas también soportan operaciones como concatenación:
cuadrados = cuadrados + [36, 49, 64, 81, 100]
print(cuadrados)
print()
# A diferencia de las cadenas de texto, que son immutable, las listas son un tipo mutable, es posible cambiar un su contenido:~
cubos = [1, 8, 27, 65, 125]  # hay algo mal aquí
c = 4 ** 3  # el cubo de 4 es 64, no 65!
cubos[3] = c
print(cubos)
print()
# También podés agregar nuevos ítems al final de la lista, usando el método append()
cubos.append(216)
cubos.append(7 ** 3)
cubos.append(8 ** 3)
print(cubos)
print()
# es posible asignar a una rebanada, y esto incluso puede cambiar la longitud de la lista o vaciarla totalmente:
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)
# reemplazar algunos valores
letras[2:5] = ['C', 'D', 'E']
print(letras)
letras[5:7] = []
print(letras)
print()

# La función predefinida len() también sirve para las listas:
letras = ['a', 'b', 'c', 'd']
print ("La cantidad de elementos en la lista es: " + str(len(letras)))
print()

# Es posible anidar listas (crear listas que contengan otras listas), por ejemplo:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0][1])  # haciendo print a un elemento de la lista mas interna
print()

# podemos escribir una subsecuencia inicial de la serie de Fibonacci así:
a, b = 0, 1
print(a)
while b < 100:
    print(b)
    a, b = b, a + b
    
# cualquier entero distinto de cero es verdadero; cero es falso.
ff = 10
while ff:
    print(ff)
    ff = ff - 1
    
i = 256 * 256
print ("El valor de i es", i)
print ("El valor de i es " + str(i))

# El parámetro nombrado end puede usarse para evitar el salto de linea al final de la salida, o terminar la salida con una cadena diferente
print("Hola", end = " ")
print("mundo.")

a, b = 0, 1
while b < 1000:
    print(b, end = ", ")
    a, b = b, a + b
    
# otros caracteres de escape
print()
print("Hola\u0020Mundo")  # tabla carácter Unicode
print("Hola\u0040Mundo")
print("Hola \u007c Mundo") 

'''
Footnotes
Debido a que ** tiene mayor precedencia que -, -3**2 será interpretado como -(3**2) y eso da como resultado -9. Para evitar esto y obtener 9, podés usar (-3)**2.
'''
